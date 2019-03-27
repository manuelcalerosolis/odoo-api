#!/usr/bin/env python
# coding: utf-8

import xmlrpc.client
from odooApiConector import odooApiConector

class odooPartnerConector(odooApiConector):

    def __init__(self):
        super().__init__('res.partner')

    def searchActiveCustomers(self):
        return self.search( [[['active', '=', True], ['customer', '=', True]]] )

    def firstActiveCustomers(self):
        return self.search( [[['active', '=', True], ['customer', '=', True]]], {'limit': 1} )

    def searchCountActiveCustomers(self):
        return self.searchCount( [[['active', '=', True], ['customer', '=', True]]] )

    def searchReadActiveCustomers(self):
        return self.searchRead( [[['active', '=', True], ['customer', '=', True]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5} )


# Codigo de ejemplo------------------------------------------------------------

odooApiConector          = odooPartnerConector()

odooApiConector.database = 'wathcdog'
odooApiConector.host     = '18.194.232.134'
odooApiConector.user     = 'mcalero@gestool.es'
odooApiConector.password = 'odoo'

print( odooApiConector.model )
print( odooApiConector.isAccessRights() )
print( odooApiConector.searchActiveCustomers() )
print( odooApiConector.searchCountActiveCustomers() )
print( odooApiConector.fieldsGet() )
print( odooApiConector.read( odooApiConector.firstActiveCustomers() ) )
print( odooApiConector.searchReadActiveCustomers() )

id = odooApiConector.create( [ {'name': "New Partner", } ] )
odooApiConector.writeById( id, { 'name': "Newer partner" } )
odooApiConector.unlink( [id] )



