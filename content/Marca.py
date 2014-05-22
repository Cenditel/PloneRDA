# -*- coding: utf-8 -*-
#
# File: Marca.py
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

    TextField(
        name='ingrediente',
        widget=TextAreaWidget(
            label='Ingrediente',
            label_msgid='PloneRDA_label_ingrediente',
            i18n_domain='PloneRDA',
        ),
    ),
    TextField(
        name='descripcion',
        widget=TextAreaWidget(
            label='Descripcion',
            label_msgid='PloneRDA_label_descripcion',
            i18n_domain='PloneRDA',
        ),
    ),
    TextField(
        name='aporte_nutricional',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Aporte_nutricional',
            label_msgid='PloneRDA_label_aporte_nutricional',
            i18n_domain='PloneRDA',
        ),
        default_output_type='text/html',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Marca_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Marca(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMarca)

    meta_type = 'Marca'
    _at_rename_after_creation = True

    schema = Marca_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Marca, PROJECTNAME)
# end of class Marca

##code-section module-footer #fill in your manual code here
##/code-section module-footer



