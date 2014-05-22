# -*- coding: utf-8 -*-
#
# File: Establecimiento.py
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.PloneRDA.config import *

# additional imports from tagged value 'import'
from Products.ArchAddOn.Fields import *
from Products.ArchAddOn.Widgets import *
from Products.ArchAddOn.Validators import *
from Products.Archetypes.atapi import *
from Products.Archetypes.atapi import DisplayList
from Products.AutocompleteWidget import AutocompleteWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre del establecimiento",
            description="Ingrese el nombre del establecimiento.",
            label_msgid="label_estab_title",
            description_msgid="help_estab_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    StringField(
        name='rif',
        widget=StringField._properties['widget'](
            label="RIF del establecimiento",
            description="Ingrese el RIF del establecimiento.",
            maxlength=14,
            size=10,
            label_msgid="label_estab_rif",
            description_msgid="help_estab_rif",
            i18n_domain='PloneRDA',
        ),
        required=False,
        validators=('isMaxSize',),
    ),
    IntegerField(
        name='tlfs',
        widget=IntegerField._properties['widget'](
            label="Teléfono del establecimiento",
            description="Ingrese el número telefónico del establecimiento.",
            maxlength=12,
            size=10,
            label_msgid="label_estab_tlfs",
            description_msgid="help_estab_tlfs",
            i18n_domain='PloneRDA',
        ),
        searchable=False,
        validators=('isMaxSize',),
    ),
    IntegerField(
        name='fax',
        widget=IntegerField._properties['widget'](
            label="Fax del establecimiento",
            description="Ingrese el número de fax del establecimiento.",
            maxlength=12,
            size=10,
            label_msgid="label_estab_fax",
            description_msgid="descr_estab_fax",
            i18n_domain='PloneRDA',
        ),
        required=False,
        validators=('isMaxSize',),
    ),
    StringField(
        name='parroquia',
        widget=SelectionWidget(
            label="Nombre de la parroquia",
            description="Seleccione la parroquia donde se encuentran ubicado el establecimiento.",
            label_msgid="label_estab_parroquia",
            description_msgid="descr_estab_parroquia",
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
            description="Ingrese el sector donde se encuentran ubicado el establecimiento.",
            label_msgid="label_estab_sector",
            description_msgid="descr_estab_sector",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
    ),
    StringField(
        name='direccion',
        widget=StringField._properties['widget'](
            label="Dirección física",
            description="Ingrese la dirección física del establecimiento.",
            label_msgid="label_estab_direccion",
            description_msgid="descr_estab_direccion",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
    ),
    EmailField(
        name='email',
        default="@",
        widget=EmailWidget(
            label="Correo electrónico del establecimiento",
            description="Ingrese el correo electrónico de contacto del establecimiento",
            label_msgid="label_estab_email",
            description_msgid="descr_estab_email",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isEmail',),
    ),
    ImageField(
        name='logo',
        widget=ImageField._properties['widget'](
            label="Seleccione una logotipo o foto del Establecimiento",
            description="Debe seleccionar una foto del Establecimiento, el tamaño recomendado es de 100 puntos de largo por 100 puntos de alto (110x110 px).",
            label_msgid="label_estab_logo",
            description_msgid="help_estab_logo",
            i18n_domain='PloneRDA',
        ),
        storage=AttributeStorage(),
        searchable=True,
        original_size=(110,110),
        sizes={'small':(50,50),'medium':(80,80),'large':(100,100)},
    ),
    StringField(
        name='horario',
        widget=StringField._properties['widget'](
            label="Horario de atención",
            description="Introduzca el horario de atención al público",
            label_msgid="label_estab_horario",
            description_msgid="descr_estab_horario",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    StringField(
        name='tipo',
        widget=SelectionWidget(
            label="Tipo de establicimiento",
            description="Seleccione la tipo de establicimiento",
            label_msgid="label_estab_tipo",
            description_msgid="help_estab_tipo",
            i18n_domain='PloneRDA',
        ),
        vocabulary=NamedVocabulary("""tipo_establecimiento"""),
        searchable=True,
    ),
    ReferenceField(
        name='productos',
        widget=ReferenceBrowserWidget(
            label='Productos',
            label_msgid='PloneRDA_label_productos',
            i18n_domain='PloneRDA',
        ),
        allowed_types=('Producto',),
        multiValued=1,
        relationship='establecimiento_producto',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Establecimiento_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Establecimiento(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IEstablecimiento)

    meta_type = 'Establecimiento'
    _at_rename_after_creation = True

    schema = Establecimiento_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Establecimiento, PROJECTNAME)
# end of class Establecimiento

##code-section module-footer #fill in your manual code here
##/code-section module-footer



