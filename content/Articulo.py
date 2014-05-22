# -*- coding: utf-8 -*-
#
# File: Articulo.py
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
from Products.BiReference.BiReferenceField import BiReferenceField, BiReferenceWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Nombre del producto",
            description="Ingrese el nombre del producto",
            label_msgid="label_art_title",
            description_msgid="descr_art_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        accessor="Title",
        searchable=True,
    ),
    StringField(
        name='categorias',
        widget=SelectionWidget(
            label="Tipo de producto",
            description="Seleccione un tipo de producto.",
            label_msgid="label_art_categoria",
            description_msgid="descr_art_categoria",
            i18n_domain='PloneRDA',
        ),
        required=True,
        vocabulary=['Aceites y Grasas','Alimentos varios','Alimentos enlatados','Artículos para limpieza','Carnes','Cereales','Frutas y vegetales','Emburtidos','Granos','Harinas','Huevos','Leche','Pastas','Pescados','Quesos','Otros bienes'],
        searchable=True,
    ),
    BooleanField(
        name='regulado',
        widget=BooleanField._properties['widget'](
            label="¿El Producto es regulado?",
            description="Seleccione la casilla si este producto es regulado.",
            label_msgid="label_art_regulado",
            description_msgid="descr_art_regulado",
            i18n_domain='PloneRDA',
        ),
        required=True,
    ),
    FloatField(
        name='precioSugerido',
        widget=FloatField._properties['widget'](
            label="Precio sugerido del producto",
            description="Ingrese el precio sugerido del producto.",
            label_msgid="label_art_regulado",
            description_msgid="descr_art_regulado",
            maxlength=5,
            size=5,
            i18n_domain='PloneRDA',
        ),
        required=True,
        validators=('isDecimal',),
    ),
    FloatField(
        name='precioAlMayor',
        widget=FloatField._properties['widget'](
            label="Precio del producto al mayor",
            description="Ingrese el precio del producto al mayor.",
            label_msgid="label_art_pmvp",
            description_msgid="descr_art_pmvp",
            maxlength=5,
            size=5,
            i18n_domain='PloneRDA',
        ),
        required=False,
        validators=('isDecimal',),
    ),
    ImageField(
        name='foto',
        widget=ImageField._properties['widget'](
            label="Seleccione una foto del Producto",
            description="Debe seleccionar una foto del Producto, el tamaño recomendado es de 110 puntos de largo por 110 puntos de alto.",
            label_msgid="label_art_foto",
            description_msgid="descr_art_foto",
            i18n_domain='PloneRDA',
        ),
        searchable=True,
        original_size=(110,110),
        sizes={'small':(50,50),'medium':(80,80),'large':(100,100)},
        required=False,
        storage=AttributeStorage(),
    ),
    BackReferenceField(
        name='productos',
        widget=BiReferenceWidget(
            visible={ 'view' : 'visible', 'edit' : 'invisible' },
            label="Producto(s) asociado(s) a este articulo",
            label_msgid="label_art_prod",
            description="Listado de producto(s) asociado(s) a este articulo",
            description_msgid="descr_art_prod",
            i18n_domain='PloneRDA',
        ),
        multiValued=True,
        relationship="producto_articulo",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Articulo_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Articulo(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IArticulo)

    meta_type = 'Articulo'
    _at_rename_after_creation = True

    schema = Articulo_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Articulo, PROJECTNAME)
# end of class Articulo

##code-section module-footer #fill in your manual code here
##/code-section module-footer



