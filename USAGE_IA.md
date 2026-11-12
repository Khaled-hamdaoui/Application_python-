# Usage de l'IA

Conformément à la section 10 des consignes, toute utilisation substantielle de l'IA pour générer, modifier ou compléter du code ou de l'analyse est déclarée ici. L'équipe reste responsable des analyses et du code remis.

**Règle :** une ligne par usage. La colonne « Ce qui a été vérifié » est remplie par le membre concerné : elle décrit ce qu'il a lui-même contrôlé (relecture, exécution, comparaison avec la source…).

| Date | Membre | Tâche | Ce que l'IA a fait | Ce qui a été vérifié |
|---|---|---|---|---|
| 2026-11-03 | Mamadou Lamine Barry | Organisation du projet | Claude Code : résumé des consignes, plan de réalisation, arborescence, README, requirements.txt, .gitignore | _À compléter par le membre_ |
| 2026-11-03 | Mamadou Lamine Barry | Choix et acquisition des données | Claude Code : recherche de jeux candidats sur Données Québec, script `scripts/telecharger_donnees.py` | Script exécuté avec succès (fichier téléchargé, `SOURCE.txt` généré). _Relecture du code : à compléter_ |
| 2026-11-03 | Mamadou Lamine Barry | Diagnostic de qualité | Claude Code : diagnostic du CSV (lignes de total, région « Error », périmètre variable, valeurs atypiques) et décisions proposées dans `docs/journal_decisions.md` | Somme des installations = total provincial vérifiée par calcul. _Validation des décisions par l'équipe : à compléter_ |
| 2026-11-11 | Mamadou Lamine Barry | Validation des décisions et nettoyage | Claude Code : vérification du PDF du MSSS (unité des durées, RSS 10, périodes) et d'une source MSSS complémentaire pour la RSS 10 ; mise à jour de `docs/journal_decisions.md` (D1 à D6 validées, règle R1 proposée) ; code du nettoyage, des contrôles de totaux et de la sauvegarde de `data/processed/urgences_propre.csv` dans `01_preparation.ipynb` | Notebook exécuté sans erreur ; totaux recalculés égaux au total provincial (contrôle automatique). _Relecture et compréhension : à compléter_ |
| 2026-11-11 | Mamadou Lamine Barry | Diagnostic dans `01_preparation.ipynb` | Claude Code : code des 10 cellules de diagnostic (encodage, dimensions, types, valeurs manquantes, doublons, lignes de total, cohérence, années et périmètre, valeurs atypiques) et rédaction des explications Markdown à partir des résultats d'exécution | Notebook exécuté de bout en bout sans erreur. _Relecture des explications et compréhension du code : à compléter_ |
| 2026-11-11 | Mamadou Lamine Barry | Structure du travail en équipe | Claude Code : notebooks 01/02/final (squelettes), USAGE_IA.md, CLAUDE.md, mise à jour du README | _À compléter par le membre_ |
