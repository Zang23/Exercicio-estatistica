import numpy as np 
import pandas as pd #Manipulação de dados



colunas = ["Datas", "codMoeda", "tipoMoeda", "simboloMoeda", "compraDolar", "vendaDolar", "alt1", "alt2"]



dados = pd.read_csv("CotacoesMoedasPeriodo.csv", sep = ';', encoding='UTF-8',header = None, names=colunas)

dados['Datas'] = dados['Datas'].astype(str).str.zfill(8)
dados['Datas'] = pd.to_datetime(dados['Datas'], format = '%d%m%Y')
dados['Datas'] = dados['Datas'].dt.strftime('%d/%m%/Y')

numeros_float = ["compraDolar", "vendaDolar"]



dados["compraDolar"] = dados["compraDolar"].str.replace(',','.').astype(float) 



clCompraDolar = dados["compraDolar"]

#dados.to_csv(caminho do arquivo)
