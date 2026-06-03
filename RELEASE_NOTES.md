# RELEASE NOTES — custom_receipts_for_pos

## v18.0.1.0.7 — 2026-06-03
- Ajout du design "Standard / Défaut" (`pos_receipt_design_default`) qui reproduit
  fidèlement le ticket natif Odoo 18 (en-tête société/logo, lignes article avec
  qty/prix/remises/lots, taxes via taxTotals, total, paiements, rendu monnaie,
  QR portail, footer, pied Odoo).
- Fichier : `data/pos_receipt_design0_default_data.xml` (noupdate="1")
- Classé en premier dans la liste data pour apparaître en haut du sélecteur.

## v18.0.1.0.6 — upstream Cybrosys
- Version initiale Cybrosys avec Design 1 et Design 2.
