import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2507"
)
paradas = res.json()
print(paradas)

from folium import Map, Marker

m = Map(location=[paradas[3]["py"], paradas[3]["px"]], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)
m.show_in_browser()












