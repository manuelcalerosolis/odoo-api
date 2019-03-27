#!/usr/bin/env python
# coding: utf-8

from odooApiConector import odooApiConector
from odooCsvReader import odooCsvReader

class odooPartnerImporter():

    def __init__(self):
        self.odooApiConector            = odooApiConector( 'res.partner' )
        self.odooApiConector.database   = 'wathcdog'
        self.odooApiConector.host       = '18.194.232.134'
        self.odooApiConector.user       = 'mcalero@gestool.es'
        self.odooApiConector.password   = 'odoo'

        self.odooCsvReader              = odooCsvReader()
        self.odooCsvReader.file         = 'C:\\Odoo\\hierros-canarias\\proveedores.csv'

    def run(self):
        if self.odooCsvReader.is_open_file:

            for field in self.odooCsvReader.convert_to_val_list():
                # self.odooApiConector.create( field )
                print(field)

            self.odooCsvReader.close_file()

# Iniciamos la clase

odooPartnerImporter().run()







