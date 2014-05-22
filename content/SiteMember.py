# -*- coding: utf-8 -*-
#
# File: SiteMember.py
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
        name='nombres',
        widget=StringField._properties['widget'](
            label="Nombres del ciudadano",
            description="Ingrese los nombres del ciudadano",
            label_msgid='PloneRDA_label_nombres',
            description_msgid='PloneRDA_help_nombres',
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
        name='apellidos',
        widget=StringField._properties['widget'](
            label="Apellidos del ciudadano",
            description="Ingrese los apellidos del ciudadano",
            label_msgid='PloneRDA_label_apellidos',
            description_msgid='PloneRDA_help_apellidos',
            i18n_domain='PloneRDA',
        ),
    ),
    ComputedField(
        name='nombre_completo',
        widget=ComputedField._properties['widget'](
            visible={'view':'visible','edit':'invisible'},
            label="Nombre completo del cuidadano",
            description="Nombre completo del cuidadano",
            label_msgid='PloneRDA_label_nombre_completo',
            description_msgid='PloneRDA_help_nombre_completo',
            i18n_domain='PloneRDA',
        ),
        expression="context.getNombres() + \'\' + context.getApellidos()",
    ),
    StringField(
        name='parish',
#        name='parroquia',
        widget=StringField._properties['widget'](
            label="Parish where the citizen lives",
            description="Enter the parish where the citizen lives",
#            label="Parroquia donde vive el ciudadano",
#            description="Ingrese la parroquia donde vive el ciudadano",
            label_msgid='PloneRDA_label_parroquia',
            description_msgid='PloneRDA_help_parroquia',
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
#        name='sector',
        name='area',
        widget=StringField._properties['widget'](
#            label="Sector donde vive el ciudadano",
#            description="Ingrese el Sector donde vive el ciudadano",
            label="Area where people live",
            description="Enter the area where the citizen lives",
            label_msgid='PloneRDA_label_sector',
            description_msgid='PloneRDA_help_sector',
            i18n_domain='PloneRDA',
        ),
    ),
    StringField(
        name='direccion',
        widget=StringField._properties['widget'](
            label="Dirección del ciudadano",
            description="Ingrese la dirección del ciudadano",
            label_msgid='PloneRDA_label_direccion',
            description_msgid='PloneRDA_help_direccion',
            i18n_domain='PloneRDA',
        ),
    ),
    PhotoField(
        name='foto',
        widget=PhotoField._properties['widget'](
            label="Seleccione una foto del cuidadano",
            description="Debe seleccionar una foto del cuidadado, el El tamaño recomendado es de 75 puntos de largo por 100 puntos de alto.",
            label_msgid='PloneRDA_label_foto',
            description_msgid='PloneRDA_help_foto',
            i18n_domain='PloneRDA',
        ),
        original_size=(75,100),
        sizes={'small':(45,45),'medium':(50,50),'large':(99,100)},
    ),
    IntegerField(
        name='cedula',
        widget=IntegerField._properties['widget'](
            label="Cédula de indentidad del rol ciudadano",
            description="Ingrese la cédula de indentidad del rol ciudadano",
            label_msgid='PloneRDA_label_cedula',
            description_msgid='PloneRDA_help_cedula',
            i18n_domain='PloneRDA',
        ),
    ),
    LinesField(
        name='telefonos',
        widget=TextAreaWidget(
            label="Números telefónicos",
            description="Introduzca los números telefónicos",
            label_msgid='PloneRDA_label_telefonos',
            description_msgid='PloneRDA_help_telefonos',
            i18n_domain='PloneRDA',
        ),
        required=False,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

SiteMember_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class SiteMember(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISiteMember)

    meta_type = 'SiteMember'
    _at_rename_after_creation = True

    schema = SiteMember_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declareProtected("view", 'getNombreCompleto')
    def getNombreCompleto(self):
        """
        """

        return '%s %s' % (self.getNombres(),self.getApellidos())


registerType(SiteMember, PROJECTNAME)
# end of class SiteMember

##code-section module-footer #fill in your manual code here
##/code-section module-footer



