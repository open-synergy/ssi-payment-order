import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-payment-order",
    description="Meta package for open-synergy-ssi-payment-order Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_payment_order',
        'odoo14-addon-ssi_payment_order_bank_cash_voucher',
        'odoo14-addon-ssi_payment_order_cheque_voucher',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
