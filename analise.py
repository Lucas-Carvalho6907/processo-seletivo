import xml.etree.ElementTree as ET

with open("dados.xml", "r", encoding="utf-8") as f:
    conteudo_xml = f.read()

root = ET.fromstring(conteudo_xml)

valores = [float(row.find("valor").text) for row in root.findall("row") if float(row.find("valor").text) > 0]

if valores:
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_da_media = len([v for v in valores if v > media])

    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Média mensal (sem dias zerados): R${media:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
else:
    print("Nenhum valor de faturamento encontrado (todos são zero ou o XML está vazio).")
