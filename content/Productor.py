# -*- coding: utf-8 -*-
#
# File: Productor.py
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
            label="",
            description="",
            label_msgid='PloneRDA_label_title',
            description_msgid='PloneRDA_help_title',
            i18n_domain='PloneRDA',
        ),
    ),
    IntegerField(
        name='direccion',
        widget=IntegerField._properties['widget'](
            label="",
            description="",
            label_msgid='PloneRDA_label_direccion',
            description_msgid='PloneRDA_help_direccion',
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
        name='rif',
        widget=StringField._properties['widget'](
            label="",
            description="",
            maxlength="",
            size="",
            label_msgid='PloneRDA_label_rif',
            description_msgid='PloneRDA_help_rif',
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
        name='paginaweb',
        widget=StringField._properties['widget'](
            label="",
            description="",
            label_msgid='PloneRDA_label_paginaweb',
            description_msgid='PloneRDA_help_paginaweb',
            i18n_domain='PloneRDA',
        ),
        validators=('isURL',),
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label="Correo electrónico del Productor",
            description="",
            label_msgid='PloneRDA_label_email',
            description_msgid='PloneRDA_help_email',
            i18n_domain='PloneRDA',
        ),
        validators=('isEmail',),
    ),
    ImageField(
        name='logo',
        widget=ImageField._properties['widget'](
            label="",
            description="",
            label_msgid='PloneRDA_label_logo',
            description_msgid='PloneRDA_help_logo',
            i18n_domain='PloneRDA',
        ),
        storage=AttributeStorage(),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Productor_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Productor(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProductor)

    meta_type = 'Productor'
    _at_rename_after_creation = True

    schema = Productor_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Productor, PROJECTNAME)
# end of class Productor

##code-section module-footer #fill in your manual code here
##/code-section module-footer



