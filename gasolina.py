
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
grafico_gasolina.get_figure().savefig(f"gasolina.png")
