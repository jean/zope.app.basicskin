##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""

from zope.interface import Interface, implements

from zope.app.traversing.interfaces import ITraverser

class FakeTraverser:

    implements(ITraverser)

    def __init__(self, *args, **kw): pass

    def traverse(self, *args, **kw):
        return None


class I1(Interface): pass
class I2(I1): pass

class O1:
    implements(I1)

class O2:
    implements(I2)
