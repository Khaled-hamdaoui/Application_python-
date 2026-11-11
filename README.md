# Projet final 8PRO409 — Analyse exploratoire des données des urgences du Québec

UQAC · Automne 2026 · Groupe 01 · Chargé de cours : Noureddine Lourimi

## Équipe
| Membre | Rôle principal | Notebook de travail |
|---|---|---|
| Mamadou Lamine Barry | _à compléter_ | _à compléter_ |
| _Membre 1_ | Préparation des données | `notebooks/01_preparation.ipynb` |
| _Membre 2_ | Exploration et visualisations | `notebooks/02_exploration.ipynb` |

## Problématique
- **Question principale :** _à définir (validation le 25 novembre 2026)_
- **Sous-question 1 :** _à définir_
- **Sous-question 2 :** _à définir_
- **Angle choisi :** _à compléter_

## Source des données
| Élément | Valeur |
|---|---|
| Jeu de données | Fichier cumulatif des données des urgences |
| Page Données Québec | https://www.donneesquebec.ca/recherche/dataset/fichier-cumulatif-des-donnees-des-urgences |
| Organisme diffuseur | Ministère de la Santé et des Services sociaux (MSSS) |
| Période couverte | Années financières 2021-2022 à 2026-2027, du 1er avril à la fin de la période 7 |
| Couverture géographique | Québec, par région sociosanitaire, établissement et installation |
| Licence | CC-BY 4.0 |
| Dictionnaire des variables | [`docs/urgences_variables_notes_methodo.pdf`](docs/urgences_variables_notes_methodo.pdf) |

## Structure du dépôt
```
├── CLAUDE.md                   Règles pour l'assistant IA (Claude Code)
├── USAGE_IA.md                 Déclaration de l'usage de l'IA (à tenir à jour)
├── README.md
├── requirements.txt            Dépendances Python
├── Projet_Final_Consignes.pdf  Consignes officielles du cours
├── data/
│   ├── raw/                    Données brutes téléchargées (ne jamais modifier)
│   └── processed/              Données nettoyées produites par les notebooks
├── scripts/
│   └── telecharger_donnees.py  Récupération des données via l'API de Données Québec
├── notebooks/
│   ├── 01_preparation.ipynb    Travail du membre 1 : nettoyage et variables dérivées
│   ├── 02_exploration.ipynb    Travail du membre 2 : statistiques et figures
│   └── analyse_eda.ipynb       Notebook final remis sur Moodle
├── docs/
│   ├── urgences_variables_notes_methodo.pdf  Dictionnaire des variables du MSSS
│   └── journal_decisions.md    Décisions de nettoyage et d'analyse, avec justification
├── figures/                    Figures exportées (PNG / HTML)
├── rapport/                    Synthèse PDF (2 pages max)
└── presentation/               Diapositives de l'exposé
```

## Installation de l'environnement
Prérequis : Python 3.11 ou plus récent et Git.

```bash
git clone https://github.com/Khaled-hamdaoui/Application_python-.git
cd Application_python-
python -m venv .venv
```
Activer l'environnement :
- Windows (PowerShell) : `.venv\Scripts\Activate.ps1`
- Windows (Git Bash) : `source .venv/Scripts/activate`
- macOS / Linux : `source .venv/bin/activate`

Puis installer les dépendances et lancer Jupyter :
```bash
pip install -r requirements.txt
python scripts/telecharger_donnees.py   # seulement si data/raw/ est vide
jupyter notebook notebooks/
```
Le dossier `.venv/` est exclu par `.gitignore` : chaque membre crée le sien.

## Règles de travail en équipe
1. **Toujours faire `git pull` avant de commencer à travailler**, pour partir de la dernière version.
2. Chacun travaille dans **son** notebook ; le contenu validé est reporté dans `analyse_eda.ipynb` par une seule personne à la fois, pour éviter les conflits dans les fichiers `.ipynb`.
3. Commiter souvent, avec des messages clairs en français, puis `git push` à la fin de chaque séance.
4. Ne jamais modifier `data/raw/`.
5. Noter chaque décision dans `docs/journal_decisions.md` et chaque usage de l'IA dans `USAGE_IA.md`.

Cycle type d'une séance :
```bash
git pull
# ... travail ...
git add <fichiers>
git commit -m "Description du changement"
git push
```

## Reproduire l'analyse
Ouvrir `notebooks/analyse_eda.ipynb` et lancer « Restart & Run All » : le notebook doit s'exécuter du début à la fin sans erreur.
