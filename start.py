# -*- coding: utf-8 -*-
import urllib
kn = '23:43:0128004:'
f = 'http://maps.rosreestr.ru/arcgis/rest/services/Cadastre/CadastreSelected/MapServer/exts/GKNServiceExtension/online/parcel/find?cadNum= '
f1 = '*&onlyAttributes=false&Y=json'
url = f.__str__() + kn.__str__() + f1.__str__()
urllib.urlretrieve(url, filename='webpage.html')
