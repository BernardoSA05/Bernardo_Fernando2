from modulos import (dataframe, indices_valor_agregado, indices_rentabilidade, 
                     pegar_preco_corrigido, pegar_preco_diversos, indices_basicos, indices_juros)
import pandas as pd

#Escolher a melhor empresa ("ROE" e "EVA")
def main():
    list_ticker = ["SLCE3", "AGRO3", "TTEN3", "SOJA3", "RAIZ4", "SMTO3"]
    list_tri = ["20244T"]
    df_comparacao = pd.DataFrame()
    for ticker in list_ticker:
        for trimestre in list_tri:
            # ticker = "SLCE3"
            # trimestre = "20244T"
            df = dataframe(ticker, trimestre)
            basic_idx = indices_basicos(df)
            juros_idx = indices_juros(basic_idx)
            rentabilidade_idx = indices_rentabilidade(basic_idx)
            comparacao = indices_valor_agregado(basic_idx, juros_idx, rentabilidade_idx)
            df_final = pd.DataFrame()
            df_final["ticker"] = [ticker]
            df_final["roe"] = comparacao["Roe"]
            df_final["eva"] = comparacao["Eva"]
            df_comparacao = pd.concat([df_comparacao, df_final], axis=0, ignore_index=True)
    print(df_comparacao)

if __name__ == '__main__':
    main()

# Comparação de ações
list_ticker = ["SLCE3", "AGRO3", "TTEN3", "SOJA3", "RAIZ4", "SMTO3"]
list_tri = ["20234T"]
df_comparacao = pd.DataFrame ()
# for ticker in list_ticker:
# 	for trimestre in list_tri:
# 		df = dataframe(ticker, trimestre)
# 		comparacao = indices_valor_agregado(df)
# 		df_final = pd. DataFrame()
# 		df_final["ticker"]-[ticker]
# 		df_final["roe"]=comparacao ["roe"]
# 		df_final[ "eva"]=comparacao ["eva"]
# 		df_comparacao= pd.concat([df_comparacao, df_final], axis=0, ignore_index=True)
# print (df_comparacao)

# Backtest 1 ano
ticker1 = "SMTO3"
data_ini1 ="2023-04-01"
data_fim1 ="2025-03-31"
df_preco1 = pegar_preco_corrigido(ticker1, data_ini1, data_fim1)
preco_ini1 = df_preco1[0:1] ["fechamento"].iloc[0]
preco_fim1 = df_preco1[-1:]["fechamento"].iloc[0]
lucro1 = (preco_fim1/preco_ini1)-1
print("Lucro 1 ano: ", lucro1)
print("Preço inicial 1 ano: ", preco_ini1)
print("Preço final 1 ano: ", preco_fim1)

# Backtest 5 anos
ticker5 = "SMTO3"
data_ini5 ="2019-04-01"
data_fim5 ="2025-03-31"
df_preco5 = pegar_preco_corrigido(ticker5, data_ini5, data_fim5)
preco_ini5 = df_preco5[0:1] ["fechamento"].iloc[0]
preco_fim5 = df_preco5[-1:]["fechamento"].iloc[0]
lucro5 = (preco_fim5/preco_ini5)-1
print("Lucro 5 anos: ", lucro5)
print("Preço inicial 5 anos: ", preco_ini5)
print("Preço final 5 anos: ", preco_fim5)

# Backtest 10 anos
ticker10 = "SMTO3"
data_ini10 ="2014-04-01"
data_fim10="2025-03-31"
df_preco10 = pegar_preco_corrigido(ticker10, data_ini10, data_fim10)
preco_ini10 = df_preco10[0:1] ["fechamento"].iloc[0]
preco_fim10 = df_preco10[-1:]["fechamento"].iloc[0]
lucro10 = (preco_fim10/preco_ini10)-1
print("Lucro 10 anos: ", lucro10)
print("Preço inicial 10 anos: ", preco_ini10)
print("Preço final 10 anos: ", preco_fim10)






#Ibovespa
ticker="ibov"
df_ibov = pegar_preco_diversos (ticker, data_ini, data_fim)
preco_ini = df_ibov[0:1] ["fechamento"].iloc[0]
preco_fim = df_ibov[-1:] ["fechamento"].iloc[0]
lucro_ibov = (preco_fim/preco_ini)-1

#GRÁFICO
df_ibov = df_ibov[["data", "fechamento"]]
df_ibov= df_ibov.rename(columns={"fechamento": "ibov" })
df_preco = df_preco[ ["data", "fechamento" ]]
df_preco= df_preco.rename(columns=("fechamento": "SMTO3"))
df_grafico = pd.merge(df_ibov, df_preco)
df_grafico.plot()