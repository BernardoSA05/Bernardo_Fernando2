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

# Backtest SMTO3
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


# Backtest SLCE3
# Backtest 1 ano 
ticker_1slce3 = "SLCE3"
data_ini1 = "2023-04-01"
data_fim1 = "2025-03-31"
df_preco1_slce3 = pegar_preco_corrigido(ticker_1slce3, data_ini1, data_fim1)
preco_ini1_slce3 = df_preco1_slce3[0:1]["fechamento"].iloc[0]
preco_fim1_slce3 = df_preco1_slce3[-1:]["fechamento"].iloc[0]
lucro1_slce3 = (preco_fim1_slce3/preco_ini1_slce3)-1
print("Lucro 1 ano SLCE3: ", lucro1_slce3)
print("Preço inicial 1 ano SLCE3: ", preco_ini1_slce3)
print("Preço final 1 ano SLCE3: ", preco_fim1_slce3)
# Backtest 5 anos
ticker_5slce3 = "SLCE3"
data_ini5 = "2019-04-01"
data_fim5 = "2025-03-31"
df_preco5_slce3 = pegar_preco_corrigido(ticker_5slce3, data_ini5, data_fim5)
preco_ini5_slce3 = df_preco5_slce3[0:1]["fechamento"].iloc[0]
preco_fim5_slce3 = df_preco5_slce3[-1:]["fechamento"].iloc[0]
lucro5_slce3 = (preco_fim5_slce3/preco_ini5_slce3)-1
print("Lucro 5 anos SLCE3: ", lucro5_slce3)
print("Preço inicial 5 anos SLCE3: ", preco_ini5_slce3)
print("Preço final 5 anos SLCE3: ", preco_fim5_slce3)
# Backtest 10 anos
ticker_10slce3 = "SLCE3"
data_ini10 = "2014-04-01"
data_fim10 = "2025-03-31"
df_preco10_slce3 = pegar_preco_corrigido(ticker_10slce3, data_ini10, data_fim10)
preco_ini10_slce3 = df_preco10_slce3[0:1]["fechamento"].iloc[0]
preco_fim10_slce3 = df_preco10_slce3[-1:]["fechamento"].iloc[0]
lucro10_slce3 = (preco_fim10_slce3/preco_ini10_slce3)-1
print("Lucro 10 anos SLCE3: ", lucro10_slce3)
print("Preço inicial 10 anos SLCE3: ", preco_ini10_slce3)
print("Preço final 10 anos SLCE3: ", preco_fim10_slce3)


# Backtest AGRO3
# Backtest 1 ano
ticker_1agro3 = "AGRO3"
data_ini1_agro3 = "2023-04-01"
data_fim1_agro3 = "2025-03-31"
df_preco1_agro3 = pegar_preco_corrigido(ticker_1agro3, data_ini1_agro3, data_fim1_agro3)
preco_ini1_agro3 = df_preco1_agro3[0:1]["fechamento"].iloc[0]
preco_fim1_agro3 = df_preco1_agro3[-1:]["fechamento"].iloc[0]
lucro1_agro3 = (preco_fim1_agro3/preco_ini1_agro3)-1
print("Lucro 1 ano AGRO3: ", lucro1_agro3)
print("Preço inicial 1 ano AGRO3: ", preco_ini1_agro3)
print("Preço final 1 ano AGRO3: ", preco_fim1_agro3)
# Backtest 5 anos
ticker_5agro3 = "AGRO3"
data_ini5_agro3 = "2019-04-01"
data_fim5_agro3 = "2025-03-31"
df_preco5_agro3 = pegar_preco_corrigido(ticker_5agro3, data_ini5_agro3, data_fim5_agro3)
preco_ini5_agro3 = df_preco5_agro3[0:1]["fechamento"].iloc[0]
preco_fim5_agro3 = df_preco5_agro3[-1:]["fechamento"].iloc[0]
lucro5_agro3 = (preco_fim5_agro3/preco_ini5_agro3)-1
print("Lucro 5 anos AGRO3: ", lucro5_agro3)
print("Preço inicial 5 anos AGRO3: ", preco_ini5_agro3)
print("Preço final 5 anos AGRO3: ", preco_fim5_agro3)
# Backtest 10 anos
ticker_10agro3 = "AGRO3"
data_ini10_agro3 = "2014-04-01"
data_fim10_agro3 = "2025-03-31"
df_preco10_agro3 = pegar_preco_corrigido(ticker_10agro3, data_ini10_agro3, data_fim10_agro3)
preco_ini10_agro3 = df_preco10_agro3[0:1]["fechamento"].iloc[0]
preco_fim10_agro3 = df_preco10_agro3[-1:]["fechamento"].iloc[0]
lucro10_agro3 = (preco_fim10_agro3/preco_ini10_agro3)-1
print("Lucro 10 anos AGRO3: ", lucro10_agro3)
print("Preço inicial 10 anos AGRO3: ", preco_ini10_agro3)
print("Preço final 10 anos AGRO3: ", preco_fim10_agro3)


# Backtest TTEN3
# Backtest 1 ano
ticker_1tten3 = "TTEN3"
data_ini1_tten3 = "2023-04-01"
data_fim1_tten3 = "2025-03-31"
df_preco1_tten3 = pegar_preco_corrigido(ticker_1tten3, data_ini1_tten3, data_fim1_tten3)
preco_ini1_tten3 = df_preco1_tten3[0:1]["fechamento"].iloc[0]
preco_fim1_tten3 = df_preco1_tten3[-1:]["fechamento"].iloc[0]
lucro1_tten3 = (preco_fim1_tten3/preco_ini1_tten3)-1
print("Lucro 1 ano TTEN3: ", lucro1_tten3)
print("Preço inicial 1 ano TTEN3: ", preco_ini1_tten3)
print("Preço final 1 ano TTEN3: ", preco_fim1_tten3)
# Backtest 5 anos
ticker_5tten3 = "TTEN3"
data_ini5_tten3 = "2019-04-01"
data_fim5_tten3 = "2025-03-31"
df_preco5_tten3 = pegar_preco_corrigido(ticker_5tten3, data_ini5_tten3, data_fim5_tten3)
preco_ini5_tten3 = df_preco5_tten3[0:1]["fechamento"].iloc[0]
preco_fim5_tten3 = df_preco5_tten3[-1:]["fechamento"].iloc[0]
lucro5_tten3 = (preco_fim5_tten3/preco_ini5_tten3)-1
print("Lucro 5 anos TTEN3: ", lucro5_tten3)
print("Preço inicial 5 anos TTEN3: ", preco_ini5_tten3)
print("Preço final 5 anos TTEN3: ", preco_fim5_tten3)
# Backtest 10 anos
ticker_10tten3 = "TTEN3"
data_ini10_tten3 = "2014-04-01"
data_fim10_tten3 = "2025-03-31"
df_preco10_tten3 = pegar_preco_corrigido(ticker_10tten3, data_ini10_tten3, data_fim10_tten3)
preco_ini10_tten3 = df_preco10_tten3[0:1]["fechamento"].iloc[0]
preco_fim10_tten3 = df_preco10_tten3[-1:]["fechamento"].iloc[0]
lucro10_tten3 = (preco_fim10_tten3/preco_ini10_tten3)-1
print("Lucro 10 anos TTEN3: ", lucro10_tten3)
print("Preço inicial 10 anos TTEN3: ", preco_ini10_tten3)
print("Preço final 10 anos TTEN3: ", preco_fim10_tten3)


# Backtest SOJA3
# Backtest 1 ano
ticker_1soja3 = "SOJA3"
data_ini1_soja3 = "2023-04-01"
data_fim1_soja3 = "2025-03-31"
df_preco1_soja3 = pegar_preco_corrigido(ticker_1soja3, data_ini1_soja3, data_fim1_soja3)
preco_ini1_soja3 = df_preco1_soja3[0:1]["fechamento"].iloc[0]
preco_fim1_soja3 = df_preco1_soja3[-1:]["fechamento"].iloc[0]
lucro1_soja3 = (preco_fim1_soja3/preco_ini1_soja3)-1
print("Lucro 1 ano SOJA3: ", lucro1_soja3)
print("Preço inicial 1 ano SOJA3: ", preco_ini1_soja3)
print("Preço final 1 ano SOJA3: ", preco_fim1_soja3)
# Backtest 5 anos
ticker_5soja3 = "SOJA3"
data_ini5_soja3 = "2019-04-01"
data_fim5_soja3 = "2025-03-31"
df_preco5_soja3 = pegar_preco_corrigido(ticker_5soja3, data_ini5_soja3, data_fim5_soja3)
preco_ini5_soja3 = df_preco5_soja3[0:1]["fechamento"].iloc[0]
preco_fim5_soja3 = df_preco5_soja3[-1:]["fechamento"].iloc[0]
lucro5_soja3 = (preco_fim5_soja3/preco_ini5_soja3)-1
print("Lucro 5 anos SOJA3: ", lucro5_soja3)
print("Preço inicial 5 anos SOJA3: ", preco_ini5_soja3)
print("Preço final 5 anos SOJA3: ", preco_fim5_soja3)
#backtest 10 anos
ticker_10soja3 = "SOJA3"
data_ini10_soja3 = "2014-04-01"
data_fim10_soja3 = "2025-03-31"
df_preco10_soja3 = pegar_preco_corrigido(ticker_10soja3, data_ini10_soja3, data_fim10_soja3)
preco_ini10_soja3 = df_preco10_soja3[0:1]["fechamento"].iloc[0]
preco_fim10_soja3 = df_preco10_soja3[-1:]["fechamento"].iloc[0]
lucro10_soja3 = (preco_fim10_soja3/preco_ini10_soja3)-1
print("Lucro 10 anos SOJA3: ", lucro10_soja3)
print("Preço inicial 10 anos SOJA3: ", preco_ini10_soja3)
print("Preço final 10 anos SOJA3: ", preco_fim10_soja3)


# Backtest RAIZ4
# Backtest 1 ano
ticker_1raiz4 = "RAIZ4"
data_ini1_raiz4 = "2023-04-01"
data_fim1_raiz4 = "2025-03-31"
df_preco1_raiz4 = pegar_preco_corrigido(ticker_1raiz4, data_ini1_raiz4, data_fim1_raiz4)
preco_ini1_raiz4 = df_preco1_raiz4[0:1]["fechamento"].iloc[0]
preco_fim1_raiz4 = df_preco1_raiz4[-1:]["fechamento"].iloc[0]
lucro1_raiz4 = (preco_fim1_raiz4/preco_ini1_raiz4)-1
print("Lucro 1 ano RAIZ4: ", lucro1_raiz4)
print("Preço inicial 1 ano RAIZ4: ", preco_ini1_raiz4)
print("Preço final 1 ano RAIZ4: ", preco_fim1_raiz4)
# Backtest 5 anos
ticker_5raiz4 = "RAIZ4"
data_ini5_raiz4 = "2019-04-01"
data_fim5_raiz4 = "2025-03-31"
df_preco5_raiz4 = pegar_preco_corrigido(ticker_5raiz4, data_ini5_raiz4, data_fim5_raiz4)
preco_ini5_raiz4 = df_preco5_raiz4[0:1]["fechamento"].iloc[0]
preco_fim5_raiz4 = df_preco5_raiz4[-1:]["fechamento"].iloc[0]
lucro5_raiz4 = (preco_fim5_raiz4/preco_ini5_raiz4)-1
print("Lucro 5 anos RAIZ4: ", lucro5_raiz4)
print("Preço inicial 5 anos RAIZ4: ", preco_ini5_raiz4)
print("Preço final 5 anos RAIZ4: ", preco_fim5_raiz4)
# Backtest 10 anos
ticker_10raiz4 = "RAIZ4"
data_ini10_raiz4 = "2014-04-01"
data_fim10_raiz4 = "2025-03-31"
df_preco10_raiz4 = pegar_preco_corrigido(ticker_10raiz4, data_ini10_raiz4, data_fim10_raiz4)
preco_ini10_raiz4 = df_preco10_raiz4[0:1]["fechamento"].iloc[0]
preco_fim10_raiz4 = df_preco10_raiz4[-1:]["fechamento"].iloc[0]
lucro10_raiz4 = (preco_fim10_raiz4/preco_ini10_raiz4)-1
print("Lucro 10 anos RAIZ4: ", lucro10_raiz4)
print("Preço inicial 10 anos RAIZ4: ", preco_ini10_raiz4)
print("Preço final 10 anos RAIZ4: ", preco_fim10_raiz4)




#Ibovespa 1 ano
ticker_ibov ="ibov"
df_ibov1 = pegar_preco_diversos (ticker_ibov, data_ini1, data_fim1)
preco_ini1 = df_ibov1[0:1] ["fechamento"].iloc[0]
preco_fim1 = df_ibov1[-1:] ["fechamento"].iloc[0]
lucro_ibov1 = (preco_fim1/preco_ini1)-1
print("Lucro Ibovespa 1 ano: ", lucro_ibov1)
print("Preço inicial Ibovespa 1 ano: ", preco_ini1)
print("Preço final Ibovespa 1 ano: ", preco_fim1)

#Ibovespa 5 anos
ticker5 ="ibov"
df_ibov5 = pegar_preco_diversos (ticker5, data_ini5, data_fim5)
preco_ini5 = df_ibov5[0:1] ["fechamento"].iloc[0]
preco_fim5 = df_ibov5[-1:] ["fechamento"].iloc[0]
lucro_ibov5 = (preco_fim5/preco_ini5)-1
print("Lucro Ibovespa 5 anos: ", lucro_ibov5)
print("Preço inicial Ibovespa 5 anos: ", preco_ini5)
print("Preço final Ibovespa 5 anos: ", preco_fim5)

#Ibovespa 10 anos
ticker10 ="ibov"
df_ibov10 = pegar_preco_diversos (ticker10, data_ini10, data_fim10)
preco_ini10 = df_ibov10[0:1] ["fechamento"].iloc[0]
preco_fim10 = df_ibov10[-1:] ["fechamento"].iloc[0]
lucro_ibov10 = (preco_fim10/preco_ini10)-1
print("Lucro Ibovespa 10 anos: ", lucro_ibov10)
print("Preço inicial Ibovespa 10 anos: ", preco_ini10)
print("Preço final Ibovespa 10 anos: ", preco_fim10)



# Gráfico de comparação de ações e Ibovespa
import matplotlib.pyplot as plt
# Gráfico de comparação de ações e Ibovespa
df_ibov = df_ibov1[["data", "fechamento"]]
df_ibov = df_ibov.rename(columns={"fechamento": "ibov"})
df_preco = df_preco1[["data", "fechamento"]]
df_preco = df_preco.rename(columns={"fechamento": "SMTO3"})
df_grafico = pd.merge(df_ibov, df_preco, on="data")
df_grafico.plot(x="data", title="Comparação de SMTO3 e Ibovespa", ylabel="Preço (R$)")





# Gráfico de comparação de SMT03 e Ibovespa com dois eixos y
import matplotlib.pyplot as plt
# ...existing code...
# Gráfico de comparação de ações e Ibovespa com dois eixos y e eixo x ajustado
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot para o SMTO3 no eixo esquerdo
ax1.plot(df_grafico["data"], df_grafico["SMTO3"], color="blue", label="SMTO3")
ax1.set_xlabel("Data")
ax1.set_ylabel("SMTO3 (R$)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Cria segundo eixo y para o Ibovespa
ax2 = ax1.twinx()
ax2.plot(df_grafico["data"], df_grafico["ibov"], color="red", label="Ibovespa")
ax2.set_ylabel("Ibovespa (R$)", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Ajuste do eixo x para melhor visualização das datas
fig.autofmt_xdate(rotation=45)
plt.title("Comparação de SMTO3 e Ibovespa")
fig.tight_layout()
plt.show()
# ...existing code...




# Gráfico de comparação de todas ("SLCE3", "AGRO3", "TTEN3", "SOJA3", "RAIZ4", "SMTO3") as ações e Ibovespa com dois eixos y
import matplotlib.pyplot as plt
import pandas as pd

# Define período para os backtests
data_ini = "2023-04-01"
data_fim = "2025-03-31"

# Lista de todas as ações
list_ticker = ["SLCE3", "AGRO3", "TTEN3", "SOJA3", "RAIZ4", "SMTO3"]

# Cria um DataFrame que irá conter os preços de fechamento de todas as ações
df_stocks = pd.DataFrame()

for ticker in list_ticker:
    df_temp = pegar_preco_corrigido(ticker, data_ini, data_fim)[["data", "fechamento"]]
    df_temp = df_temp.rename(columns={"fechamento": ticker})
    if df_stocks.empty:
        df_stocks = df_temp.copy()
    else:
        df_stocks = pd.merge(df_stocks, df_temp, on="data", how="outer")

# Obtém o preço do Ibovespa no mesmo período
df_ibov = pegar_preco_diversos("ibov", data_ini, data_fim)[["data", "fechamento"]]
df_ibov = df_ibov.rename(columns={"fechamento": "Ibovespa"})

# Mescla os dados das ações com os do Ibovespa
df_grafico = pd.merge(df_stocks, df_ibov, on="data", how="inner")
df_grafico["data"] = pd.to_datetime(df_grafico["data"])
df_grafico = df_grafico.sort_values("data")

# Cria o gráfico com dois eixos y
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plota as ações no eixo esquerdo
colors = ['blue', 'green', 'orange', 'purple', 'brown', 'cyan']
for i, ticker in enumerate(list_ticker):
    ax1.plot(df_grafico["data"], df_grafico[ticker], color=colors[i % len(colors)], label=ticker)
ax1.set_xlabel("Data")
ax1.set_ylabel("Preço Ações (R$)")
ax1.tick_params(axis="y")

# Plota o Ibovespa no eixo direito
ax2 = ax1.twinx()
ax2.plot(df_grafico["data"], df_grafico["Ibovespa"], color="red", label="Ibovespa", linewidth=2)
ax2.set_ylabel("Preço Ibovespa (R$)", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Combina as legendas dos dois eixos
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

# Ajusta o eixo x para melhor visualização das datas
fig.autofmt_xdate(rotation=45)
plt.title("Comparação de Ações e Ibovespa")
fig.tight_layout()
plt.show()