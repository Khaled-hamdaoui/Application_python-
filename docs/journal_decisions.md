# Journal des décisions

Une ligne par décision de données ou d'analyse (nettoyage, exclusion, variable dérivée, choix de graphique).

| Date | Auteur | Décision | Justification | Impact (lignes, variables) |
|---|---|---|---|---|
| 2026-11-03 | Équipe (proposé par diagnostic) | Exclure les lignes de total (« Total provincial », « Total régional », « Total établissement », permis `"."`) et ne garder que les installations. | Le fichier mélange 4 niveaux d'agrégation. La somme des installations égale exactement le total provincial chaque année : garder les totaux ferait compter les mêmes visites jusqu'à 4 fois. | 949 → 684 lignes (−265). |
| 2026-11-03 | Équipe (proposé par diagnostic) | Renommer la région `"Error"` (RSS 10) en « Nord-du-Québec ». | Erreur d'étiquette dans la source : le code RSS 10 correspond au Nord-du-Québec (établissement Santé Québec Baie-James). | 10 lignes (dont 6 de détail), colonne `region`. |
| 2026-11-03 | Équipe (proposé par diagnostic) | Pour toute comparaison entre années, se limiter aux installations présentes les 6 années (périmètre constant). | 12 installations (Mauricie–Centre-du-Québec, Montréal) sont absentes en 2026-2027 et 5 de Baie-James n'apparaissent que récemment. Le total provincial passe de 2,01 M à 1,86 M visites à cause de ces absences, alors qu'à périmètre constant les visites augmentent (1,79 M → 1,84 M). | 103 installations × 6 ans = 618 lignes pour les analyses temporelles ; les 684 lignes restent utilisables pour une année donnée. |
| 2026-11-03 | Équipe (proposé par diagnostic) | Conserver la valeur manquante de `dms_sur_civiere` / `delai_pec_sur_civiere` (Centre de santé de Radisson, 2026-2027) sans imputation. | L'installation n'a eu aucune visite sur civière : la moyenne n'est pas définie, le vide est logique. | 1 ligne. |
| 2026-11-03 | Équipe (proposé par diagnostic) | Conserver les valeurs atypiques (Hôpital général juif, Albert-Prévost, Gatineau/Hull) et les commenter. | Ce sont des valeurs réelles liées à la taille ou à la mission de l'installation (Albert-Prévost est un hôpital psychiatrique). Piste d'approfondissement : comparer les résultats avec et sans Albert-Prévost. | Aucune ligne retirée. |
| 2026-11-03 | Équipe (proposé par diagnostic) | Interpréter les durées (`dms_*`, `delai_pec_*`) comme des heures. | Le dictionnaire indique seulement « nombres décimaux », mais les seuils de 24 h / 48 h et les valeurs observées (DMS médiane ≈ 7) indiquent des heures. Hypothèse à signaler dans le notebook. | Unités des colonnes de durée. |

## À valider en équipe
Les décisions ci-dessus viennent du diagnostic initial (voir `docs/urgences_variables_notes_methodo.pdf`). L'équipe doit les confirmer, ou les modifier, avant de les appliquer dans le notebook.
