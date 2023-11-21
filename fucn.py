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


def getTotalTerm(terms: list, tipo: dict, moq: dict) -> list:
    days = []
    all = []
    for i in terms:
        if i[6] not in days:
            days.append(i[6])

        if i[1] not in all:
            all.append(i[1])
    unique = []
    for i in sorted(all):
        unique.append([i])

    for i in unique:
        total = 0
        average = 0
        packing = 0
        stock = 0
        for x in terms:
            if x[1] == i[0]:
                total += x[3]
        i.append(tipo[i[0][:-2]])
        i.append(total)
        i.append(len(days))
        average = total / len(days)
        i.append(average)
        stock = average * 2
        i.append(stock)
        if i[0] in moq:
            packing = moq[i[0]]
        else:
            packing = 0
        i.append(packing)
        i.append(round(stock / packing, 3))

    for i in unique:
        if i[1] == "BE.END" or i[7] < 1:
            i.append("Poco Uso/Trasera")
        else:
            i.append("Rack Grande")

    # for i in unique:
    #     print(i)

    return unique


def getCellUnique(terminals: list) -> list:
    cells = []
    unique = []
    for i in terminals:
        if i[-1] != "prensas":
            terminalCelda = f"{i[1]} {i[-1]}"
            if terminalCelda not in cells:
                cells.append(terminalCelda)
        if i[1] not in unique and i[-1] != "prensas":
            unique.append(i[1])

    terms = []
    for i in sorted(unique):
        terms.append([i])

    cellTerms = []
    for i in cells:
        cellTerms.append(i.split(" "))

    for i in terms:
        count = 0
        for b in cellTerms:
            if i[0] == b[0]:
                count += 1
        i.append(count)
    uniqueCellTerminal = []
    for i in terms:
        if i[1] == 1:
            for b in cellTerms:
                if b[0] == i[0]:
                    uniqueCellTerminal.append(b)

    # for i in terms:
    #     print(i)
    for i in uniqueCellTerminal:
        print(i)

    return uniqueCellTerminal
