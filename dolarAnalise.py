import numpy as np
import pandas as pd

dados = pd.read_csv("CotacoesMoedasPeriodoTratado.csv", sep=";", encoding="utf-8")

mediaCompra = np.mean(dados["compra"])
medianaCompra = np.median(dados["compra"])

mediaVenda = np.mean(dados["venda"])
medianaVenda = np.median(dados["venda"])

print("Média compra: ", round(mediaCompra, 3))
print("Mediana compra:", medianaCompra)

print("Média venda: ", round(mediaVenda, 3))
print("Mediana venda:", medianaVenda) 