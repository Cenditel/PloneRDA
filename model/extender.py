# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2007 PloneGov
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# ------------------------------------------------------------------------------
class ModelExtender:
    '''When PloneMeeting is installed by Zope at startup, this class looks among
       Zope products for PloneMeeting sub-products that define additional
       Archetypes schemas for PloneMeeting classes (MeetingItem, Meeting).'''

    def __init__(self, baseSchema, forClass="item"):
        self.baseSchema = baseSchema # The base schema on which the extensions
        # must be applied.
        self.target = forClass

    def run(self):
        '''This method looks for special methods in other Zope products that
           will modify the Meeting, MeetingItem or MeetingFile base schemas
           (changes, field additions,...).'''
        res = self.baseSchema
        # Scan all Zope-products
        import Products
        for productName in dir(Products):
            if not productName.startswith('_'):
                try:
                    exec 'from Products.%s.model.pm_updates import ' \
                         'update_%s_schema' % (productName, self.target)
                    exec 'res = update_%s_schema(res)' % self.target
                except ImportError:
                    pass
        return res
# ------------------------------------------------------------------------------
