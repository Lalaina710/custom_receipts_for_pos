# -*- coding: utf-8 -*-
"""SOPROMER 18.0.1.0.10 - protection des designs de ticket edites a la main.

Les records `pos_receipt_design1` et `pos_receipt_design2_demo` sont livres
dans des fichiers XML SANS noupdate : chaque `-u` reecrit leur
`design_receipt`. Or ce champ est edite a la main en production (ex. note
generale ajoutee au Design 2 sur le 43 le 07/06/2026). Un `-u` effacerait ces
modifications sans avertissement.

- Design 2 : passe en noupdate sans condition (contenu de prod = reference).
- Design 1 : passe en noupdate SEULEMENT si son contenu ne correspond a aucune
  version livree par le module (1.0.8 d'origine ou 1.0.9 avec la ligne RENDU),
  c'est-a-dire s'il a ete modifie a la main. S'il correspond a une version
  livree, il reste modifiable pour que ce `-u` lui applique la version
  courante ; post-migrate.py le passe ensuite en noupdate.

Les fichiers XML ne sont pas passes en noupdate="1" : sur une base ou le
record existe deja, le drapeau en base suffit et le loader l'honore.
"""
import logging

_logger = logging.getLogger(__name__)

MODULE = 'custom_receipts_for_pos'

# md5(design_receipt) des contenus livres par le module pour pos_receipt_design1
SHIPPED_DESIGN1_MD5 = {
    '5a77bcbe11f13801f9aa061d04e608bb',  # <= 18.0.1.0.8 (upstream Cybrosys)
    '9141d0f66c8c4e97d940ba4a7af8bd8b',  # 18.0.1.0.9 (ligne RENDU)
}


def migrate(cr, version):
    if not version:
        return

    cr.execute("""
        UPDATE ir_model_data
           SET noupdate = TRUE
         WHERE module = %s AND name = 'pos_receipt_design2_demo'
           AND noupdate IS NOT TRUE
     RETURNING res_id
    """, (MODULE,))
    if cr.rowcount:
        _logger.info("%s: pos_receipt_design2_demo passe en noupdate", MODULE)

    cr.execute("""
        SELECT d.id, md5(r.design_receipt)
          FROM ir_model_data d
          JOIN pos_receipt r ON r.id = d.res_id
         WHERE d.module = %s AND d.name = 'pos_receipt_design1'
           AND d.model = 'pos.receipt'
    """, (MODULE,))
    row = cr.fetchone()
    if not row:
        return
    imd_id, digest = row
    if digest in SHIPPED_DESIGN1_MD5:
        _logger.info(
            "%s: pos_receipt_design1 = contenu livre (md5 %s), mis a jour par ce -u",
            MODULE, digest)
        return
    cr.execute("UPDATE ir_model_data SET noupdate = TRUE WHERE id = %s", (imd_id,))
    _logger.warning(
        "%s: pos_receipt_design1 modifie a la main (md5 %s) : passe en noupdate, "
        "la ligne RENDU livree par le module ne lui est PAS appliquee",
        MODULE, digest)
