# -*- coding: utf-8 -*-
def classFactory(iface):
    from .plugin import IGRFMagneticFieldPlugin
    return IGRFMagneticFieldPlugin(iface)
