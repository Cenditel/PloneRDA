# -*- coding: utf-8 -*-
#
# File: Comite.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.PloneRDA.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre del Comité",
            label_msgid="label_comi_title",
            description="Ingrese el nombre del comité o mesa técnica de trabajo del consejo comunal.",
            description_msgid="help_comi_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    TextField(
        name='descripcion',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Descripción detallada",
            label_msgid="label_comi_descr",
            description="Ingrese la descripción detallada sobre este comité o mesa técnica.",
            description_msgid="help_comi_descr",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    StringField(
        name='miembros',
        widget=StringField._properties['widget'](
            label="Seleccione los miembros del comité",
            label_msgid="label_comi_miembros",
            description="Por favor seleccione los miembros que conforman este comité.",
            description_msgid="help_comi_miembros",
            i18n_domain='PloneRDA',
        ),
        required=True,
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Comite_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Comite(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IComite)

    meta_type = 'Comite'
    _at_rename_after_creation = True

    schema = Comite_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Comite, PROJECTNAME)
# end of class Comite

##code-section module-footer #fill in your manual code here
##/code-section module-footer



