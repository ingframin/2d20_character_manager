import pdfplumber
import json

pdf_file = "mutant_chronicles_rulebook.pdf"

with pdfplumber.open(pdf_file) as pdf:
    tabs = pdf.pages[50].extract_table()
    tabA = []
    tabB = []
    tabC = []
    tabD = []
    for row in tabs:
        if not row[0].isnumeric():
            continue
        tabA.append({"roll":int(row[0]),"career":row[1]})
        tabB.append({"roll":int(row[0]),"career":row[2]})
        tabC.append({"roll":int(row[0]),"career":row[3]})
        tabD.append({"roll":int(row[0]),"career":row[4]})
    p51 = pdf.pages[51]
    txt = p51.extract_text()
    print(txt)
    # print(tabA)
    # print(tabB)
    # print(tabC)
    # print(tabD)