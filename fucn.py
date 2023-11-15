def getTerminals(material: list, celdas: dict) -> tuple[list, list]:
    terminal = []
    for i in material:
        if i[1][0] == "T":
            terminal.append(i)
    for i in terminal:
        if i[0] in celdas:
            i.append(celdas[i[0]])
        else:
            i.append("prensas")
    m1 = []
    m2 = []
    for i in terminal:
        if i[7] == "M1":
            m1.append(i)
        else:
            m2.append(i)
    return m1, m2
