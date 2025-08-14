import numpy as np
import pandas as pd #Manipulação de dados



colunas = ["data", "codMoeda", "tipoMoeda", "simboloMoeda", "compra", "venda", "alt1", "alt2"]


dados = pd.read_csv("CotacoesMoedasPeriodo.csv", sep = ';', encoding='UTF-8',header = None, names=colunas)

dados['data'] = dados['data'].astype(str).str.zfill(8)
dados['data'] = pd.to_datetime(dados['data'], format = '%d%m%Y')
dados['data'] = dados['data'].dt.strftime("%d/%m/%Y")



colunasFloat = ["compra", "venda"]

dados[colunasFloat] = dados[colunasFloat].apply(
    lambda x: x.str.replace(",", ".").astype(float)
)

colunasString = ["tipoMoeda", "simboloMoeda"]

dados[colunasString] = dados[colunasString].astype(str)

colunasApagar = ["alt1", "alt2"]

dados1 = dados.drop(columns=colunasApagar)

dados1.to_csv("CotacoesMoedasPeriodoTratado.csv", sep=";", encoding="utf-8", index=False)
