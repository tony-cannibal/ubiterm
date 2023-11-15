import pandas as pd
# import const
import fucn

material = pd.read_excel("MATERIAL.xlsx").values.tolist()
celdas = {k: d for [k, v, d] in pd.read_excel("CELDAS.xlsx").values.tolist()}
moq = pd.read_excel("MOQ.xlsx")
tipo = pd.read_excel("TIPO.xlsx")

terminalesM1, terminalesM2 = fucn.getTerminals(material, celdas)

print(terminalesM1)
