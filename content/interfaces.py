# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IArticulo(Interface):
    """Marker interface for .Articulo.Articulo
    """

class IEstablecimiento(Interface):
    """Marker interface for .Establecimiento.Establecimiento
    """

class IFabricante(Interface):
    """Marker interface for .Fabricante.Fabricante
    """

class IProducto(Interface):
    """Marker interface for .Producto.Producto
    """

class IComite(Interface):
    """Marker interface for .Comite.Comite
    """

class IOrganizacion(Interface):
    """Marker interface for .Organizacion.Organizacion
    """

class IConsejoComunalFolder(Interface):
    """Marker interface for .ConsejoComunalFolder.ConsejoComunalFolder
    """

##code-section FOOT
##/code-section FOOT