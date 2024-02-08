import pandas as pd

df = pd.read_csv('UEFA Champions League 2004-2021.csv')
df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
print(df['awayscore'].dtype)
print(df['homeScore'].dtype)
#Cambiamos las columnas homeScore y awayscore a tipo numerico
df['homeScore'] = pd.to_numeric(df['homeScore'], errors='coerce')
df['awayscore'] = pd.to_numeric(df['awayscore'], errors='coerce')
print(df['awayscore'].dtype)
print(df['homeScore'].dtype)
#Ordenamos el df segun los equipos que juegan en casa
df.sort_values(by='homeTeam', inplace=True)

print('\n')

# Calcular el resultado del partido (0 para empate, 1 para victoria del equipo local, -1 para victoria del equipo visitante)
df['result'] = df.apply(lambda row: 0 if row['homeScore'] == row['awayscore'] else 1 if row['homeScore'] > row['awayscore'] else -1, axis=1)
# Calcular la diferencia de goles para cada partido
df['goalDifference'] = df.apply(lambda row: row['homeScore'] - row['awayscore'], axis=1)

print(df)

print('\n')

#Filtramos los partidos que ha jugado el real madrid en casa
df_real_madrid = df[df['homeTeam'] == 'Real Madrid']
print(df_real_madrid)
#Calculamos la diferencia de goles promedio del real madrid en casa
print(df_real_madrid['goalDifference'].mean())