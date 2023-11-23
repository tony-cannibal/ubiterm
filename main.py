import pandas as pd
# import const
import func

material: list = pd.read_excel("MATERIAL.xlsx").values.tolist()

celdas: dict = {
    k: d for [k, v, d] in pd.read_excel("CELDAS.xlsx").values.tolist()
}

moq: dict = {
    k: g for [k, v, d, r, g] in pd.read_excel("MOQ.xlsx").values.tolist()
}

tipo: dict = {
    k: v for [k, v, d] in pd.read_excel("TIPO.xlsx").values.tolist()
}

# Separates terminale m1 from m2 and asigns the cell number
terminalesM1, terminalesM2 = func.getTerminals(material, celdas)

matM1: list = func.getTotalTerm(terminalesM1, tipo, moq, 2)
matM2: list = func.getTotalTerm(terminalesM2, tipo, moq, 2)

uniqueCellTermsM1: list = func.getCellUnique(terminalesM1)
uniqueCellTermsM2: list = func.getCellUnique(terminalesM2)

uniqueM1, generalM1 = func.uniqueCellTermList(matM1, uniqueCellTermsM1)

func.giveLocations("general", generalM1)

if __name__ == "__main__":
    pass
