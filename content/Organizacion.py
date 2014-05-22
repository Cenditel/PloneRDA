# -*- coding: utf-8 -*-
#
# File: Organizacion.py
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
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.PloneRDA.config import *

# additional imports from tagged value 'import'
from Products.ArchAddOn.Fields import *
from Products.ArchAddOn.Widgets import *
from Products.ArchAddOn.Validators import *
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre de la organización",
            label_msgid="label_org_title",
            description="Ingrese el nombre de la organización.",
            description_msgid="help_org_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    StringField(
        name='rif',
        widget=StringField._properties['widget'](
            label="RIF de la organización",
            label_msgid="label_org_rif",
            description="Ingrese el Registro de Información Fiscal (RIF) de la organización.",
            description_msgid="help_org_rif",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    TextField(
        name='mision',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Misión organizacional",
            label_msgid="label_org_mision",
            description="Ingrese la misión de la organización.",
            description_msgid="help_org_mision",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    TextField(
        name='vision',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Visión organizacional",
            label_msgid="label_org_vision",
            description="Ingrese la visión de la organización.",
            description_msgid="help_org_vision",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    StringField(
        name='ambito',
        widget=StringField._properties['widget'](
            label="Ambito acción",
            label_msgid="label_org_ambito",
            description="Ingrese el ambito acción organizacional.",
            description_msgid="help_org_ambito",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    StringField(
        name='parroquia',
        widget=SelectionWidget(
            label="Nombre de la parroquia",
            label_msgid="label_org_parroquia",
            description="Ingrese el nombre de la parroquia donde se encuentra ubicado la organización.",
            description_msgid="help_org_parroquia",
            i18n_domain='PloneRDA',
        ),
        vocabulary=NamedVocabulary("""parroquia"""),
        searchable=True,
        required=True,
    ),
    StringField(
        name='sector',
        widget=StringField._properties['widget'](
            label="Nombre del sector",
            label_msgid="label_org_sector",
            description="Ingrese el sector donde se encuentran ubicado esta organización.",
            description_msgid="help_org_sector",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    StringField(
        name='direccion',
        widget=StringField._properties['widget'](
            label="Dirección física",
            label_msgid="label_org_direccion",
            description="Ingrese la dirección física de la organización.",
            description_msgid="help_org_direccion",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    EmailField(
        name='email',
        default="@",
        widget=EmailWidget(
            label="Correo electrónico de la organización.",
            label_msgid="label_org_email",
            description="Ingrese el correo electrónico de contacto de la organización.",
            description_msgid="help_org_email",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isEmail',),
    ),
    LinkField(
        name='paginaweb',
        default="http://",
        widget=LinkWidget(
            label="Dirección de la página Web",
            label_msgid="label_org_pagweb",
            description="Ingrese la dirección de la página Web organización.",
            description_msgid="help_org_pagweb",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isURL',),
    ),
    IntegerField(
        name='tlfs',
        widget=IntegerField._properties['widget'](
            label="Teléfono de la organización",
            label_msgid="label_org_tlfs",
            description="Ingrese el número telefónico de la organización.",
            description_msgid="help_org_tlfs",
            maxlength=12,
            size=10,
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    IntegerField(
        name='fax',
        widget=IntegerField._properties['widget'](
            label="Fax de la organización",
            label_msgid="label_org_fax",
            description="Ingrese el número de fax de la organización.",
            description_msgid="help_org_fax",
            maxlength=12,
            size=10,
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    ImageField(
        name='logo',
        allowable_content_types="('image/jpeg','image/gif','image/png'),",
        widget=ImageField._properties['widget'](
            label="Seleccione una foto o logotipo de la organización",
            label_msgid="label_org_logo",
            description="Puede seleccionar una foto o logotipo de la organización, el tamaño recomendado es de 100 puntos de largo por 100 puntos de alto.",
            description_msgid="help_org_logo",
            i18n_domain='PloneRDA',
        ),
        required=False,
        storage=AttributeStorage(),
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Organizacion_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Organizacion(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IOrganizacion)

    meta_type = 'Organizacion'
    _at_rename_after_creation = True

    schema = Organizacion_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Organizacion, PROJECTNAME)
# end of class Organizacion

##code-section module-footer #fill in your manual code here
##/code-section module-footer



