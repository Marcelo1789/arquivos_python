import requests
import json
import pprint
accuweatherAPIkey ='JGCEG0y8oJ3fUbFBGj9KK5kN6qXkM3uh' 
r = requests.get('http://www.geoplugin.net/json.gp')
if ( r.status_code != 200 ):
    print ('não foi possivel obter a localização')
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']

locationAPIurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=JGCEG0y8oJ3fUbFBGj9KK5kN6qXkM3uh&q=-20.072425%2C-43.409335&language=pt-br"

r2 = requests.get(locationAPIurl)
 
if ( r.status_code != 200 ):
    print ('não foi possivel obter o codigo do local')
else:
     = json.loads(r2.text)
    namelocal = locationresponse ['LocalizedName']+ " , "\
                + locationresponse
