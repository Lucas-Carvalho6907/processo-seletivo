import json

with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

valores = [item['valor'] for item in dados if item['valor'] > 0]

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
    print("Nenhum valor de faturamento encontrado (todos são zero ou o JSON está vazio).")
