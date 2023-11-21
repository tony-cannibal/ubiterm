import pandas as pd
# import const
import fucn

material = pd.read_excel("MATERIAL.xlsx").values.tolist()
celdas = {k: d for [k, v, d] in pd.read_excel("CELDAS.xlsx").values.tolist()}
moq = {k: g for [k, v, d, r, g] in pd.read_excel("MOQ.xlsx").values.tolist()}
tipo = {k: v for [k, v, d] in pd.read_excel("TIPO.xlsx").values.tolist()}

terminalesM1, terminalesM2 = fucn.getTerminals(material, celdas)

matM1: list = fucn.getTotalTerm(terminalesM1, tipo, moq)
matM2: list = fucn.getTotalTerm(terminalesM2, tipo, moq)

uniqueCellTermsM1 = fucn.getCellUnique(terminalesM1)
uniqueCellTermsM2 = fucn.getCellUnique(terminalesM2)

# print(terminalesM1)

if __name__ == "__main__":
    pass
