# Projet final 8PRO409 — Analyse exploratoire de données publiques

UQAC · Automne 2026 · Groupe 01 · Chargé de cours : Noureddine Lourimi

## Équipe
- Mamadou Lamine Barry
- _À compléter_
- _À compléter_

## Problématique
- **Question principale :** _à définir (validation le 25 novembre 2026)_
- **Sous-question 1 :** _à définir_
- **Sous-question 2 :** _à définir_
- **Angle choisi :** _territoire, période, population ou indicateur, avec justification_

## Source des données
| Élément | Valeur |
|---|---|
| Jeu de données | _nom_ |
| Page Données Québec | _lien exact_ |
| Organisme diffuseur | _à compléter_ |
| Période couverte | _à compléter_ |
| Couverture géographique | _à compléter_ |
| Licence | _à compléter_ |

## Structure du dépôt
```
data/raw/          Données brutes téléchargées (jamais modifiées)
data/processed/    Données nettoyées produites par le notebook
scripts/           Script de récupération des données
notebooks/         Notebook principal (projet_final.ipynb)
figures/           Figures exportées (PNG / HTML)
rapport/           Synthèse PDF (2 pages max)
presentation/      Diapositives de l'exposé
docs/              Journal des décisions, déclaration IA, déclarations individuelles
```

## Reproduire l'analyse
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (macOS/Linux : source .venv/bin/activate)
pip install -r requirements.txt
python scripts/telecharger_donnees.py   # si les données ne sont pas fournies
jupyter notebook notebooks/projet_final.ipynb
```
Le notebook doit s'exécuter du début à la fin (« Restart & Run All ») sans erreur.

## Utilisation de l'IA
Voir [`docs/declaration_ia.md`](docs/declaration_ia.md).
