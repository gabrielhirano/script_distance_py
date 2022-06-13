import pandas as pd
from num2words import num2words
from unidecode import unidecode

df = pd.read_csv("../dados/afterDados_oti.csv")

print(df["STATUS"].value_counts())



        # Primeiro teste usando o Pelias    //afterDados
# Endereço encontrado        43509
# Endereço NAO encontrado      701

        # Segundo teste usando o Pelias    //afterDadosMelhorado                     
# Endereço encontrado        43864
# Endereço NAO encontrado      346

        # Ultimo teste usando o Pelias   //afterDados_oti           //cada teste teve parametros dentro do arquivo ajustado, e o ultimo teste foi o mais completo.
# Endereço encontrado        43185
# sem numero                   740
# Endereço NAO encontrado      285

        # Usando o sisgeo
# Number                                     33676             
# Cep                                         9581
# Cep não encontrado na base dos Correios      770
# Cep encontrado na base dos Correios          183


























# # df["name"] = df["layer"] + df["street"] + df["housenumber"] + df["district"]
# df["name"] = None;
# # print(df["name"])

# for i in df.index:
#     df["name"][i] = f'{df["layer"][i]} {df["street"][i]} {df["housenumber"][i]} {df["district"][i]}'

# df.to_csv("dados.csv",index=False)







# meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]











# df.drop(columns=['name'],axis=1, inplace=True)

# df.to_csv("dados.csv",index=False)
























# for mes in meses:
#     df["street"].replace(f"1º de {mes}",f"primeiro de {mes}",inplace=True)
#     print(f"de {mes}")


# for mes in meses:
#     for i in range(1,31):
#         df["street"].replace(f"{i} de {mes}",f"{unidecode(num2words(i, lang='pt-br'))} de {mes}",inplace=True)
#         print(f"{i} de {mes}")

# df.to_csv("number_e_meses_pos.csv")