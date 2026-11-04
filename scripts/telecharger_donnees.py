"""Télécharge le jeu « Fichier cumulatif des données des urgences » (MSSS)
depuis Données Québec et l'enregistre dans data/raw/.

L'URL du CSV est obtenue via l'API CKAN de Données Québec (package_show),
ce qui évite de coder en dur un lien qui pourrait changer.

Usage (depuis la racine du projet) :
    python scripts/telecharger_donnees.py
"""
from datetime import date
from pathlib import Path

import requests

DATASET_ID = "fichier-cumulatif-des-donnees-des-urgences"
API_URL = "https://www.donneesquebec.ca/recherche/api/3/action/package_show"
PAGE_URL = f"https://www.donneesquebec.ca/recherche/dataset/{DATASET_ID}"

RACINE = Path(__file__).resolve().parents[1]
DOSSIER_RAW = RACINE / "data" / "raw"
FICHIER_SORTIE = DOSSIER_RAW / "Donnees_cumulatives_Urgence.csv"
FICHIER_META = DOSSIER_RAW / "SOURCE.txt"


def trouver_url_csv() -> tuple[str, dict]:
    """Retourne l'URL de la ressource CSV et les métadonnées du jeu."""
    reponse = requests.get(API_URL, params={"id": DATASET_ID}, timeout=60)
    reponse.raise_for_status()
    paquet = reponse.json()["result"]
    for ressource in paquet["resources"]:
        if (ressource.get("format") or "").upper() == "CSV":
            return ressource["url"], paquet
    raise RuntimeError(f"Aucune ressource CSV trouvée pour {DATASET_ID}")


def main() -> None:
    DOSSIER_RAW.mkdir(parents=True, exist_ok=True)
    url, paquet = trouver_url_csv()
    print(f"Téléchargement : {url}")

    # Certains serveurs gouvernementaux refusent les clients sans User-Agent.
    entetes = {"User-Agent": "Mozilla/5.0 (projet etudiant 8PRO409)"}
    reponse = requests.get(url, headers=entetes, timeout=120)
    reponse.raise_for_status()
    FICHIER_SORTIE.write_bytes(reponse.content)

    FICHIER_META.write_text(
        "\n".join(
            [
                f"Jeu de données : {paquet['title']}",
                f"Page Données Québec : {PAGE_URL}",
                f"Organisme : {paquet.get('organization', {}).get('title')}",
                f"Licence : {paquet.get('license_title')}",
                f"Couverture temporelle : {paquet.get('temporal')}",
                f"Fréquence de mise à jour : {paquet.get('update_frequency')}",
                f"Métadonnées modifiées le : {paquet.get('metadata_modified', '')[:10]}",
                f"URL du fichier : {url}",
                f"Téléchargé le : {date.today().isoformat()}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    taille_ko = FICHIER_SORTIE.stat().st_size / 1024
    print(f"Enregistré : {FICHIER_SORTIE} ({taille_ko:.0f} Ko)")
    print(f"Métadonnées : {FICHIER_META}")


if __name__ == "__main__":
    main()
