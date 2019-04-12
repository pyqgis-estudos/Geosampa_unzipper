# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeosampaUnzip
                                 A QGIS plugin
 Extrai o shape do ZIP do Geosampa
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-11
        copyright            : (C) 2019 by Marcelo Baliú Fiamenghi
        email                : ma.baliu@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GeosampaUnzip class from file GeosampaUnzip.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geosampa_unzip import GeosampaUnzip
    return GeosampaUnzip(iface)