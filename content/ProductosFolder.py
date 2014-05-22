# -*- coding: utf-8 -*-
#
# File: ProductosFolder.py
#
# Copyright (c) 2008 by CENDITEL
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Leonardo Caballero <lcaballero@cenditel.gob.ve>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.PloneRDA.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre de carperta de Productos",
            label_msgid="",
            description="Ingrese el nombre de la carperta que almacenará los Productos",
            description_msgid="",
            i18n_domain='PloneRDA',
        ),
        required=True,
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProductosFolder_schema = BaseBTreeFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProductosFolder(BaseBTreeFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProductosFolder)

    meta_type = 'ProductosFolder'
    _at_rename_after_creation = True

    schema = ProductosFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ProductosFolder, PROJECTNAME)
# end of class ProductosFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



