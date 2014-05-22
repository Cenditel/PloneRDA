# -*- coding: utf-8 -*-
#
# File: PloneRDA.py
#
# Copyright (c) 2008 by (c) CENDITEL
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Leonardo J. Caballero G. <lcaballero@cenditel.gob.ve>, Ruben Rangel
<rubenrang@gmail.com>, Maria A. Espinoza <maespinoza@cenditel.gob.ve>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "PloneRDA"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
#setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner'))
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Contributor', 'Member', 'Manager', 'Owner'))
ADD_CONTENT_PERMISSIONS = {
    'Articulo': 'PloneRDA: Add Articulo',
    'Establecimiento': 'PloneRDA: Add Establecimiento',
    'Fabricante': 'PloneRDA: Add Fabricante',
    'Producto': 'PloneRDA: Add Producto',
    'Comite': 'PloneRDA: Add Comite',
    'Organizacion': 'PloneRDA: Add Organizacion',
    'ConsejoComunalFolder': 'PloneRDA: Add ConsejoComunalFolder',
}

#setDefaultRoles('PloneRDA: Add Articulo', ('Anonymous', 'Contributor', 'Editor', 'Member', 'Reader', 'Reviewer', 'Manager', 'Owner'))
#setDefaultRoles('PloneRDA: Add Articulo', ('Manager','Owner'))
'''
setDefaultRoles('PloneRDA: Add Articulo', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add Establecimiento', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add Fabricante', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add Producto', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add Comite', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add Organizacion', ('Contributor', 'Member', 'Manager', 'Owner'))
setDefaultRoles('PloneRDA: Add ConsejoComunalFolder', ('Contributor', 'Member', 'Manager', 'Owner'))
'''
product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
#DEPENDENCIES = ['ATVocabularyManager','ATBackRef','BiReference','DataGridField','ATReferenceBrowserWidget']
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.PloneRDA.AppConfig import *
except ImportError:
    pass
