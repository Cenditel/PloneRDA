# -*- coding: utf-8 -*-
#
# File: ConsejoComunalFolder.py
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
            label="Nombre del Consejo Comunal",
            label_msgid="label_cc_title",
            description="Ingrese el nombre del Consejo Comunal",
            description_msgid="help_cc_title",
            i18n_domain='PloneRDA',
        ),
        required=True,
        searchable=True,
    ),
    StringField(
        name='parroquia',
        widget=SelectionWidget(
            label="Nombre de la parroquia",
            label_msgid="label_cc_parroquia",
            description="Seleccione la parroquia donde se encuentran ubicado este consejo comunal",
            description_msgid="help_cc_parroquia",
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
            label_msgid="label_cc_sector",
            description="Ingrese el sector donde se encuentran ubicado este consejo comunal",
            description_msgid="help_cc_sector",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    StringField(
        name='direccion',
        widget=StringField._properties['widget'](
            label="Dirección física",
            label_msgid="label_cc_direccion",
            description="Ingrese la dirección física del establecimiento donde normalmente se reunen",
            description_msgid="help_cc_direccion",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),
    EmailField(
        name='email',
        default="@",
        widget=EmailWidget(
            label="Correo electrónico del consejo comunal",
            label_msgid="label_cc_email",
            description="Ingrese el correo electrónico de contacto del consejo comunal.",
            description_msgid="help_cc_email",
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
        validators=('isEmail',),
    ),
    IntegerField(
        name='tlfs',
        widget=IntegerField._properties['widget'](
            label="Teléfono(s) para contactos",
            label_msgid="label_cc_tlfs",
            description="Ingrese teléfono(s) para contactos del consejo comunal.",
            description_msgid="help_cc_tlfs",
            maxlength=12,
            size=10,
            i18n_domain='PloneRDA',
        ),
        required=False,
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ConsejoComunalFolder_schema = BaseBTreeFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ConsejoComunalFolder(BaseBTreeFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IConsejoComunalFolder)

    meta_type = 'ConsejoComunalFolder'
    _at_rename_after_creation = True

    schema = ConsejoComunalFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(ConsejoComunalFolder, PROJECTNAME)
# end of class ConsejoComunalFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



