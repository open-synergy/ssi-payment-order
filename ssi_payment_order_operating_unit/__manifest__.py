# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Payment Order + Operating Unit",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "contributors": [
        "Andhitia Rama <andhitia.r@gmail.com>",
    ],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_payment_order",
        "ssi_operating_unit_mixin",
    ],
    "data": [
        "security/res_group/payment_order.xml",
        "security/ir_rule/payment_order.xml",
        "view/payment_order.xml",
        "security/res_group/payment_request.xml",
        "security/ir_rule/payment_request.xml",
        "view/payment_request.xml",
        "security/res_group/batch_payment_request.xml",
        "security/ir_rule/batch_payment_request.xml",
        "view/batch_payment_request.xml",
    ],
}
