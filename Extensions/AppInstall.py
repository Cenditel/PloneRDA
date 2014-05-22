from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName
from Products.ATVocabularyManager.utils.vocabs import createSimpleVocabs

def install(self):
    """let's install the countries vocab"""
    vocabs = {}
    vocabs['tipo_establecimiento'] = (
        ('0001', u'Cadenas'),
        ('0002', u'Independientes'),
        ('0003', u'Autoservicios'),
    )
    portal = getToolByName(self,'portal_url').getPortalObject()
    atvm = getToolByName(portal, ATVOCABULARYTOOL)
    createSimpleVocabs(atvm, vocabs)
