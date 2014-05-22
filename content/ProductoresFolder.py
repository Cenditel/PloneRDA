# -*- coding: utf-8 -*-
#
# File: ProductoresFolder.py
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
            label='Title',
            label_msgid='PloneRDA_label_title',
            i18n_domain='PloneRDA',
        ),
        content_icon="folder_icon.png",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ProductoresFolder_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ProductoresFolder(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProductoresFolder)

    meta_type = 'ProductoresFolder'
    _at_rename_after_creation = True

    schema = ProductoresFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ProductoresFolder, PROJECTNAME)
# end of class ProductoresFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



