import requests
import pandas as pd
import re

# addres = "rua um"
# typeLogradouro = "RUA"
# link = f"http://geoteste:4000/v1/search?text={addres}&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15&layers={typeLogradouro}"
# resposta = requests.get(link)
# dados = resposta.json()
df = pd.read_csv("../dados/empresas.csv")
df["response"] = "Endereço NAO encontrado"

for i in df.index:
    if len(re.findall("[0-9]", df["st_numero"][i])) == 0:
        df["response"][i] = "sem numero"

    else:
        # addres = f'{df["st_tipo_logradouro"][i]} {df["st_logradouro"][i]} {df["st_numero"][i]} {df["st_bairro"][i]}'
        addres = df["endedreco_completo"][i]
        typeLogradouro = df["st_tipo_logradouro"][i]
        link = f"http://geoteste:4000/v1/autocomplete?text={addres}&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15&layers={typeLogradouro}"
        resposta = requests.get(link)
        dados = resposta.json()
       
        if(len(dados['features']) != 0):
            df['response'][i] = "Endereço encontrado"
            df["X_PELIAS"][i] = dados['features'][0]["geometry"]["coordinates"][0]
            df["Y_PELIAS"][i] = dados['features'][0]["geometry"]["coordinates"][1]
            print(i)
        # else:
        #     address_no_bairro = f'{df["st_tipo_logradouro"][i]} {df["st_logradouro"][i]} {df["st_numero"][i]}'
        #     link = f"http://geoteste:4000/v1/search?text={address_no_bairro}&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15&layers={typeLogradouro}"
        #     resposta = requests.get(link)
        #     dados = resposta.json()
        #     print(address_no_bairro)
        #     print(typeLogradouro)
        #     print(resposta)
        #     print(dados)
        #     print(dados['features'])
        #     if(len(dados['features']) != 0):
        #         df['response'][i] = "Endereço encontrado"
        #         df["X_PELIAS"][i] = dados['features'][0]["geometry"]["coordinates"][0]
        #         df["Y_PELIAS"][i] = dados['features'][0]["geometry"]["coordinates"][1]
        #         print(i)

df.to_csv("afterDados_autocomplete.csv",index=False)

 #RUA POTIRA 40 ICAIVERA
#http://geoteste:4000/v1/autocomplete?text=RUA POTIRA 40 ICAIVERA&size=1&focus.point.lat=-19.94150&focus.point.lon=-44.19809&boundary.circle.lat=-19.94150&boundary.circle.lon=-44.198091&boundary.circle.radius=15