# CLAUDE.md

Instructions pour Claude Code (et tout assistant IA) qui travaille dans ce dépôt.

## Contexte
Projet final du cours 8PRO409 (UQAC, automne 2026) : analyse exploratoire (EDA) en équipe du jeu « Fichier cumulatif des données des urgences » du MSSS, publié sur Données Québec. Consignes : `Projet_Final_Consignes.pdf`. Remise sur Moodle le 9 décembre 2026 avant 8 h. Aucun modèle de machine learning n'est attendu.

## Équipe
| Membre | Nom | Rôle principal |
|---|---|---|
| Membre 1 | Mamadou Lamine Barry | Données et qualité (`01_preparation.ipynb`, journal des décisions) |
| Membre 2 | Khaled Hamdaoui | Analyse et figures (`02_exploration.ipynb`, `figures/`) |
| Membre 3 | Émilie Gagnon | Interprétation et synthèse (§6–7 du notebook final, `rapport/`) |
| Membre 4 | Khadiatou Sow | Coordination et présentation (assemblage d'`analyse_eda.ipynb`, `presentation/`) |

Chaque membre indique son rôle et les fichiers qu'il peut modifier dans un fichier `CLAUDE.local.md` à la racine. Ce fichier est propre à chaque poste, lu automatiquement par Claude Code et exclu de Git par `.gitignore`.

## Langue
Tout le contenu (Markdown, commentaires, noms de variables descriptifs, messages de commit) est rédigé en français.

## Structure
- `data/raw/` : données brutes telles que téléchargées. **Ne jamais modifier.**
- `data/processed/` : données nettoyées, produites uniquement par les notebooks.
- `scripts/telecharger_donnees.py` : récupération des données via l'API CKAN de Données Québec.
- `notebooks/01_preparation.ipynb` (membre 1, Mamadou Lamine Barry), `notebooks/02_exploration.ipynb` (membre 2, Khaled Hamdaoui) : notebooks de travail.
- `notebooks/analyse_eda.ipynb` : notebook final remis, assemblé par le membre 4 (Khadiatou Sow). Il doit être autonome et s'exécuter du début à la fin.
- `docs/` : dictionnaire des variables du MSSS (`urgences_variables_notes_methodo.pdf`) et journal des décisions (`journal_decisions.md`).
- `USAGE_IA.md` : déclaration de l'usage de l'IA.

## Règles de travail
- Ne pas modifier le notebook d'un autre membre sans qu'on le demande.
- Chemins relatifs à la racine du projet (variable `RACINE` dans les notebooks), jamais de chemins absolus.
- Bibliothèques autorisées : celles de `requirements.txt` (pandas, numpy, matplotlib, seaborn, plotly). Le notebook final doit contenir au moins une figure Matplotlib, une Seaborn et une Plotly.
- Chaque décision de nettoyage ou d'analyse est ajoutée à `docs/journal_decisions.md` avec sa justification.
- **Après toute aide substantielle de l'IA, ajouter une ligne dans `USAGE_IA.md`** (date, membre, tâche, ce que l'IA a fait). Laisser la colonne « Ce qui a été vérifié » au membre.
- L'IA explique et propose ; les étudiants doivent comprendre, vérifier et pouvoir défendre tout le code et toutes les interprétations à l'oral.

## Particularités des données (voir `docs/journal_decisions.md`)
- **Pour l'analyse, utiliser `data/processed/urgences_propre.csv`** (684 lignes × 36 colonnes, produit par `01_preparation.ipynb`, décisions D1 à D6 appliquées, variables dérivées V1 à V8 incluses) :
  `pd.read_csv(RACINE / "data" / "processed" / "urgences_propre.csv", dtype={"no_permis_installation": str})`.
- Le CSV brut est en UTF-8 avec BOM (`encoding="utf-8-sig"`). Il mélange des lignes de total et des lignes d'installation : dans le fichier propre, seules les installations sont gardées (D1).
- La région RSS 10, étiquetée `"Error"` dans la source, est renommée « Nord-du-Québec » dans le fichier propre (D2).
- Le périmètre change selon l'année : 12 installations sont absentes en 2026-2027, dont toute la Mauricie et Centre-du-Québec. Toutes les années sont gardées, avec la colonne booléenne **`perimetre_constant`** (vraie pour les 103 installations présentes les 6 années). **Toute comparaison entre années filtre `df[df["perimetre_constant"]]`** (D3).
- Une seule valeur manquante (Radisson 2026-2027, 0 visite sur civière) : ne pas l'imputer (D4). Les valeurs atypiques sont réelles et conservées (D5).
- Les durées (`dms_*`, `delai_pec_*`) sont interprétées comme des heures : hypothèse à signaler, car le PDF du MSSS ne précise pas l'unité (D6).
- Les années couvrent seulement les périodes financières 1 à 7 (du 1er avril à environ la mi-octobre, date de fin estimée), pas l'année complète.
- **Variables dérivées** (en %, sauf V1 ; construction validée le 2026-11-11 ; le choix des variables présentées dans l'analyse revient au membre 2) :
  - `annee_debut` (V1) : année de début de l'année financière, en entier ;
  - `part_75ans_plus_pct` (V2), `part_sante_mentale_pct` (V3), `part_civiere_pct` (V4), `taux_pec_pct` (V5) : rapportées à `nb_visites_total` ;
  - `taux_civiere_24h_pct` (V6), `taux_civiere_48h_pct` (V7) : rapportés à `nb_visites_sur_civiere`, avec un NaN pour Radisson 2026-2027 ;
  - `variation_visites_pct` (V8) : variation par rapport à l'année précédente, même installation, NaN la première année de présence.
  Pour agréger une part ou un taux, il faut le recalculer à partir des sommes des comptes, jamais faire la moyenne des pourcentages.
- **Point O1 (tranché le 2026-11-11, option (d))** : Paul-Gilbert (+676 %), Chauveau (+81 %) en 2022-2023 et Chibougamau (+490 %) en 2026-2027 ont une première année qui semble partielle. Paul-Gilbert et Chauveau sont dans le périmètre constant. **Toute comparaison entre années est présentée avec deux années de départ** : 2021-2022 et 2022-2023, à périmètre constant (filtrer sur `annee_debut`). L'année de départ peut inverser le sens de l'évolution des durées et du taux de séjours ≥ 24 h : cette double présentation sert de contrôle complémentaire. Les données ne sont pas modifiées.
- **Règle R1 (validée le 2026-11-11)** : pour agréger une durée, utiliser une moyenne pondérée, jamais une moyenne simple. `dms_*` est pondérée par le nombre de visites correspondant (`nb_visites_total`, `nb_visites_ambulatoire`, `nb_visites_sur_civiere`). `delai_pec_*` est pondéré par le nombre d'usagers pris en charge correspondant (`nb_usagers_pec_*`). Avec ces poids, on retrouve exactement les valeurs provinciales officielles.

## Git
- `git pull` avant de commencer à travailler, commit et push à la fin de chaque séance.
- Messages de commit courts, en français, au présent.
- Ne jamais commiter `.venv/` ni de fichiers temporaires.
