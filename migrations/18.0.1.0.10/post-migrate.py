# -*- coding: utf-8 -*-
"""SOPROMER 18.0.1.0.10 - fige le Design 1 apres sa mise a jour.

pre-migrate.py a laisse `pos_receipt_design1` modifiable quand il portait un
contenu livre, pour que ce `-u` lui applique la version courante. Une fois les
donnees chargees, on le passe en noupdate : les prochains `-u` ne reecriront
plus un design eventuellement edite a la main.
"""
import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    cr.execute("""
        UPDATE ir_model_data
           SET noupdate = TRUE
         WHERE module = 'custom_receipts_for_pos'
           AND name = 'pos_receipt_design1'
           AND noupdate IS NOT TRUE
    """)
    if cr.rowcount:
        _logger.info("custom_receipts_for_pos: pos_receipt_design1 passe en noupdate")
