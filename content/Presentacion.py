# -*- coding: utf-8 -*-
#
# File: Presentacion.py
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
        name='peso',
        widget=StringField._properties['widget'](
            label='Peso',
            label_msgid='PloneRDA_label_peso',
            i18n_domain='PloneRDA',
        ),
    ),
    IntegerField(
        name='unidades',
        widget=IntegerField._properties['widget'](
            maxlength=8,
            size=4,
            label='Unidades',
            label_msgid='PloneRDA_label_unidades',
            i18n_domain='PloneRDA',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Presentacion_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Presentacion(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPresentacion)

    meta_type = 'Presentacion'
    _at_rename_after_creation = True

    schema = Presentacion_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Presentacion, PROJECTNAME)
# end of class Presentacion

##code-section module-footer #fill in your manual code here
##/code-section module-footer



