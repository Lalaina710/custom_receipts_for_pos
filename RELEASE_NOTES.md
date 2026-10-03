# RELEASE NOTES — custom_receipts_for_pos

## v18.0.1.0.10 — 2026-10-03
Ticket par défaut (branche `t-else` de `static/src/xml/order_receipt.xml`,
utilisée par tous les PdV sans design personnalisé, dont les 18 PdV RT) :
- FIX arrondi (H1) : upstream testait `'order_rounding' in taxTotals`, toujours
  vrai en v18, donc « Arrondi 0,00 / A payer » sur chaque ticket. Condition et
  valeurs natives Odoo 18 : `props.data.show_rounding`,
  `order_sign * order_rounding`, `order_sign * (order_total + order_rounding)`.
- FIX signe des remboursements (H2) : TOTAL, Arrondi et A payer multipliés par
  `taxTotals.order_sign` comme le natif (les taxTotals sont en valeur absolue,
  un remboursement s'imprimait en positif). Les sous-totaux HT et les montants
  de TVA sont signés aussi (le natif ne le fait pas) pour un ticket de
  remboursement cohérent.
- i18n : libellé du rendu en source anglaise « Change given », traduit
  « Rendu » ; « To Pay » traduit « A payer » (même traduction que
  `point_of_sale`, pas de conflit dans le dictionnaire JS commun). Nouveau
  fichier `i18n/fr.po`. Rendu visuel inchangé en français.
- Protection noupdate (migrations/18.0.1.0.10) :
  - pre-migrate : `pos_receipt_design2_demo` passe en noupdate sans condition ;
    `pos_receipt_design1` passe en noupdate seulement si son contenu ne
    correspond à aucune version livrée (md5 1.0.8 ou 1.0.9), c'est-à-dire s'il a
    été modifié à la main (il n'est alors pas mis à jour, warning dans le log).
  - post-migrate : `pos_receipt_design1` passe en noupdate après mise à jour.
  - Les fichiers XML restent sans noupdate (le drapeau en base suffit).
- Connu, non corrigé (H3) : Design 1 en réimpression imprime le numéro et la
  date de la commande EN COURS (`props.receipt` = `pos.get_order()`), pas ceux
  de la commande réimprimée.

## v18.0.1.0.9 — 2026-10-03
- FIX ticket sans monnaie rendue. Les PdV sans design personnalisé
  (`is_custom_receipt` décoché, cas des 18 PdV RT) passent par la branche
  `t-else` de `static/src/xml/order_receipt.xml`, qui remplace le ticket natif.
  Upstream y testait `order_change` (variable inexistante, toujours faux) et
  lisait `taxTotals.order_change` (clé absente en v18) : la ligne de rendu ne
  s'affichait jamais. Remplacée par la source native Odoo 18 :
  `props.data.show_change` / `props.data.order_change`, libellé « Rendu ».
  Affichage seulement si le rendu est non nul (comportement natif), y compris
  en réimpression depuis la liste des commandes.
- Design 1 (`pos_receipt_design1`) : ajout de la ligne « RENDU » sous le TOTAL,
  même source `props.data`. Record non `noupdate` : un `-u` réécrit son
  `design_receipt` (vérifié identique au XML sur les bases RT avant upgrade).

## v18.0.1.0.8 — 2026-06-04
- Bouton « Note générale » dans le menu Actions du POS
  (`control_buttons_general_note.js/.xml`) : écrit `order.general_note`,
  imprimé sur le ticket via `props.data.generalNote`.
- FIX ticket blanc : `design_receipt` stocké avec des `
` littéraux casse la
  compilation OWL (`t-else` séparé de `t-if` par du texte).
- ACL `pos.receipt` durcie : utilisateurs internes en lecture seule,
  `point_of_sale.group_pos_manager` en écriture (le design est du code exécuté
  chez tous les caissiers).

## v18.0.1.0.7 — 2026-06-03
- Ajout du design "Standard / Défaut" (`pos_receipt_design_default`) qui reproduit
  fidèlement le ticket natif Odoo 18 (en-tête société/logo, lignes article avec
  qty/prix/remises/lots, taxes via taxTotals, total, paiements, rendu monnaie,
  QR portail, footer, pied Odoo).
- Fichier : `data/pos_receipt_design0_default_data.xml` (noupdate="1")
- Classé en premier dans la liste data pour apparaître en haut du sélecteur.

## v18.0.1.0.6 — upstream Cybrosys
- Version initiale Cybrosys avec Design 1 et Design 2.
