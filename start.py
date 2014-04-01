import urllib
kn = ’23:43:0102005′
f = ‘http://maps.rosreestr.ru/ArcGIS/rest/services/CadastreNew/Cadastre/MapServer/exts/GKNServiceExtension/online/parcel/find?cadNum= ‘
f1 = ‘:%&onlyAttributes=false&y=json’
url = f.__str__() + kn.__str__() + f1.__str__()
urllib.urlretrieve(url, filename=’webpage.html’)
