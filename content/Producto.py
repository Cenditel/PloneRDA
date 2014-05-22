# -*- coding: utf-8 -*-
#
# File: Producto.py
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
from Products.DataGridField import DataGridField, DataGridWidget
from Products.ATBackRef.BackReferenceField import BackReferenceField, BackReferenceWidget
from Products.PloneRDA.config import *

# additional imports from tagged value 'import'
from Products.Archetypes.atapi import *
from Products.Archetypes.atapi import DisplayList
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from Products.CMFCore.utils import getToolByName
from Products.BiReference.BiReferenceField import BiReferenceField, BiReferenceWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre del producto",
            description="Ingrese el nombre del producto.",
            label_msgid="label_prod_title",
            description_msgid="help_prod_marca",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    StringField(
        name='marca',
        widget=StringField._properties['widget'](
            label="Marca del producto",
            description="Ingrese la Marca del producto.",
            label_msgid="label_prod_marca",
            description_msgid="help_prod_marca",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
    ),
    TextField(
        name='descripcion',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Descripción detallada",
            description="Ingrese la descripción detallada del producto.",
            label_msgid="label_prod_descr_detall",
            description_msgid="help_prod_descr_detall",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    TextField(
        name='ingrediente',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Lista de ingredientes",
            description="Ingrese la lista de ingredientes del producto.",
            label_msgid="label_prod_ingredientes",
            description_msgid="help_prod_ingredientes",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    TextField(
        name='aporteNutricional',
        allowable_content_types="('text/plain','text/structured','text/html',),",
        widget=TextAreaWidget(
            label="Descripción de aportes nutricional.",
            description="Si lo desea puede colaborar ingresando las lista de aportes nutricionales de forma detallada del producto.",
            label_msgid="label_prod_aporte_nutri",
            description_msgid="help_prod_aporte_nutri",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
        validators=('isTidyHtmlWithCleanup',),
    ),
    DataGridField(
        name='presentacion',
        widget=DataGridWidget(
            label="Presentación del producto",
            description="Ingrese la Presentación del producto",
            label_msgid="label_prod_presentacion",
            description_msgid="help_prod_presentacion",
            auto_insert="True",
            i18n_domain='PloneRDA',
        ),
        required=True,
        columns={'Cantidad' : Column("Cantidad"),'Unidades' : Column("Unidades"),},
    ),
    ImageField(
        name='foto',
        widget=ImageField._properties['widget'](
            label="Seleccione una foto del Producto.",
            description="Debe seleccionar una foto del Producto, el tamaño recomendado es de 100 puntos de largo por 100 puntos de alto (110x110 px).",
            label_msgid="label_prod_foto",
            description_msgid="help_prod_foto",
            i18n_domain='PloneRDA',
        ),
        storage=AttributeStorage(),
        original_size=(110,110),
        searchable=True,
        sizes={'small':(50,50),'medium':(80,80),'large':(100,100)},
    ),
    BackReferenceField(
        name='establecimientos',
        widget=BiReferenceWidget(
            visible={ 'view' : 'visible', 'edit' : 'invisible' },
            label="Establecimiento donde se encuentra el producto",
            label_msgid="label_prod_estab",
            description="Lista de establecimiento donde se encuentra el producto.",
            description_msgid="help_prod_estab",
            i18n_domain='PloneRDA',
        ),
        multiValued=True,
        relationship="establecimiento_producto",
    ),
    ReferenceField(
        name='articulos',
        widget=ReferenceBrowserWidget(
            label='Articulos',
            label_msgid='PloneRDA_label_articulos',
            i18n_domain='PloneRDA',
        ),
        allowed_types=('Articulo',),
        multiValued=1,
        relationship='producto_articulo',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Producto_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Producto(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IProducto)

    meta_type = 'Producto'
    _at_rename_after_creation = True

    schema = Producto_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Producto, PROJECTNAME)
# end of class Producto

##code-section module-footer #fill in your manual code here
##/code-section module-footer



