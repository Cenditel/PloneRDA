# -*- coding: utf-8 -*-
#
# File: Fabricante.py
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
from Products.PloneRDA.config import *

# additional imports from tagged value 'import'
from Products.ArchAddOn.Fields import *
from Products.ArchAddOn.Widgets import *
from Products.ArchAddOn.Validators import *
from Products.BiReference.BiReferenceField import BiReferenceField, BiReferenceWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre del Fabricante",
            description="Ingrese el nombre del Fabricante",
            label_msgid="label_fab_title",
            description_msgid="help_fab_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    StringField(
        name='direccion',
        widget=StringField._properties['widget'](
            label="Dirección física",
            description="Ingrese la dirección física del Fabricante",
            label_msgid="label_fab_direccion",
            description_msgid="help_fab_direccion",
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
        name='rif',
        widget=StringField._properties['widget'](
            label="RIF del fabricante",
            description="Ingrese el Registro de Información Fiscal (RIF) del fabricante.",
            maxlength=12,
            size=10,
            label_msgid="label_fab_rif",
            description_msgid="help_fab_rif",
            i18n_domain='PloneRDA',
        ),
    ),
    LinkField(
        name='paginaweb',
        default="http://",
        widget=LinkWidget(
            label="Dirección de la página Web",
            description="Ingrese la dirección de la página Web del fabricante.",
            label_msgid="label_fab_pagweb",
            description_msgid="help_fab_pagweb",
            i18n_domain='PloneRDA',
        ),
        validators=('isURL',),
    ),
    EmailField(
        name='email',
        default="@",
        widget=EmailWidget(
            label="Correo electrónico del fabricante",
            description="Dirección de correo electrónico del fabricante.",
            label_msgid="label_fab_email",
            description_msgid="help_fab_email",
            i18n_domain='PloneRDA',
        ),
        validators=('isEmail',),
    ),
    ImageField(
        name='logo',
        widget=ImageField._properties['widget'](
            label="Seleccione una foto o logotipo del fabricante",
            description="Debe seleccionar una foto o logotipo del fabricante, el tamaño recomendado es de 100 puntos de largo por 100 puntos de alto.",
            label_msgid="label_fab_logo",
            description_msgid="help_fab_logo",
            i18n_domain='PloneRDA',
        ),
        storage=AttributeStorage(),
        original_size=(110,110),
        sizes={'small':(50,50),'medium':(80,80),'large':(100,100)},
    ),
    BackReferenceField(
        name='productos',
        widget=BiReferenceWidget(
            label="Producto(s) elaborados(s) por este fabricante",
            label_msgid="",
            description="Listado de producto(s) elaborados(s) por este fabricante.",
            description_msgid="",
            visible={ 'view' : 'visible', 'edit' : 'invisible' },
            i18n_domain='PloneRDA',
        ),
        multiValued=True,
        relationship="producto_fabricante",
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
        relationship='fabricante_producto',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Fabricante_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Fabricante(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFabricante)

    meta_type = 'Fabricante'
    _at_rename_after_creation = True

    schema = Fabricante_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Fabricante, PROJECTNAME)
# end of class Fabricante

##code-section module-footer #fill in your manual code here
##/code-section module-footer



