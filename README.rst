.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

POS Receipt Design
==================
Option to select the customised Receipts for each POS

Company
-------
* `Cybrosys Techno Solutions <https://cybrosys.com/>`__

Credits
-------
Developer:  (V14) Syamili K,
            (V15) Sajna Sherin T,
            (V16 & V17) Sadique Kottekkat
            (V18) Sreerag PM
Contact: odoo@cybrosys.com

Contacts
--------
* Mail Contact : odoo@cybrosys.com
* Website : https://cybrosys.com

Bug Tracker
-----------
Bugs are tracked on GitHub Issues. In case of trouble, please check there if your issue has already been reported.

Maintainer
==========
.. image:: https://cybrosys.com/images/logo.png
   :target: https://cybrosys.com

This module is maintained by Cybrosys Technologies.

For support and more information, please visit `Our Website <https://cybrosys.com/>`__

SOPROMER patches
================
* 18.0.1.0.7 : design "Standard / Défaut" (copie du ticket natif Odoo 18).
* 18.0.1.0.8 : bouton "Note générale", correctif ticket blanc, ACL durcie.
* 18.0.1.0.9 : monnaie rendue ("Rendu") affichée sur le ticket par défaut
  (PdV sans design personnalisé) et sur le Design 1, via
  ``props.data.show_change`` / ``props.data.order_change`` (source native,
  correcte aussi en réimpression). Voir RELEASE_NOTES.md.
* 18.0.1.0.10 : ticket par défaut aligné sur le natif Odoo 18 pour l'arrondi
  (affiché seulement s'il existe) et le signe des remboursements (TOTAL,
  A payer, sous-totaux et TVA négatifs) ; libellés traduits via
  ``i18n/fr.po`` ; Design 1 et Design 2 passés en noupdate par migration
  (un ``-u`` n'écrase plus un design édité à la main).

Limite connue (non corrigée)
----------------------------
* Design 1 en réimpression (liste des commandes) : le numéro et la date
  imprimés sont ceux de la commande EN COURS, pas de la commande réimprimée
  (le design lit ``props.receipt``, calculé sur ``pos.get_order()``). Les
  lignes, totaux et le rendu sont corrects (ils lisent ``props.data``).
* Design 1 et Design 2 étant en noupdate, une future évolution de leur contenu
  livrée par le module devra passer par un script de migration.

Further information
===================
HTML Description: `<static/description/index.html>`__
