import pandas as pd

# Carregar os dados do arquivo CSV

jogos = pd.read_csv("jogos.csv", delimiter=";")
df = pd.DataFrame(jogos)
def obter_resultados_do_time(time, ano):
    # Filtrar jogos em que o time foi mandante ou visitante no ano especificado
    jogos_time = df[((df['Mandante'] == time) | (df['Visitante'] == time)) & (pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.year == ano)]

    # Adicionar coluna 'resultado' com base no mandante ou visitante
    jogos_time.loc[jogos_time['Mandante'] == time, 'Resultado'] = jogos_time.apply(lambda row: 'Vitória' if (row['Rodada'] == 1) and (row['Mandante'] == time) else 'Derrota' if (row['Rodada'] == 2) and (row['Mandante'] == time) else 'Vitória' if (row['Rodada'] == 2) and (row['Visitante'] == time) else 'Derrota' if (row['Rodada'] == 1) and (row['Visitante'] == time) else 'Empate', axis=1)

    # Tratar valores NaN na coluna 'Resultado'
    jogos_time['Resultado'] = jogos_time['Resultado'].fillna('')

    # Selecionar apenas as colunas desejadas
    jogos_time = jogos_time[['Data', 'Horário', 'Mandante', 'Visitante', 'Resultado']]

    # Converter DataFrame para uma representação de string
    string_representation = jogos_time.to_string(index=False)

    return string_representation


