"""
Created on Thu Oct 17 17:11:59 2024

@author: luis, pablo & angelo

Este es un código que usa librerías y bases de datos de archivos csvs para hacer el siguiente análisis:
Desde la temporada 2017-18, hasta la anterior, 2023-24, ha habido cambios en las políticas de los clubes:
el Newcastle ahora tiene un equipo rico y pasó de ser medio pelo a competitivo. Caso contrario al del Everton, que ahora
es un equipo formador y paso de competitivo a casi descender.
Entonces, ¿qué tan relevante es la inyección de capital para mantenerse competitivos en la mejor liga del mundo, la Premier League?
"""
#Librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Funciones
def victorias_en_temporada(Temporadas_str,Victorias_Newcastle_Total,Victorias_Everton_Total):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Victorias_Newcastle_Total, label='Proyección de victorias Newcastle')
  plt.plot(Temporadas_str, Victorias_Everton_Total, label='Proyección de victorias Everton')
  plt.title('Victorias por temporada')
  plt.xlabel('Temporada')
  plt.ylabel('Victorias')
  plt.legend()
  plt.grid()
  plt.show()
def goles_anotados(Goles_Totales_Newcastle,Goles_Totales_Everton,Temporadas_str):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Goles_Totales_Newcastle, label='Proyección de goles Newcastle')
  plt.plot(Temporadas_str, Goles_Totales_Everton, label='Proyección de goles Everton')
  plt.title('Goles anotados por temporada por equipo')
  plt.xlabel('Temporada')
  plt.ylabel('Goles anotados')
  plt.legend()
  plt.grid()
  plt.show()
def goles_recibidos(Goles_Recibidos_Newcastle,Goles_Recibidos_Everton,Temporadas_str):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Goles_Recibidos_Totales_Newcastle, label='Proyección de goles recibidos Newcastle')
  plt.plot(Temporadas_str, Goles_Recibidos_Totales_Everton, label='Proyección de goles recibidos Everton')
  plt.title('Goles recibidos por temporada por equipo')
  plt.xlabel('Temporada')
  plt.ylabel('Goles recibidos')
  plt.legend()
  plt.grid()
  plt.show()
def derrotas_en_temporada(Temporadas_str,Victorias_Newcastle_Total,Victorias_Everton_Total):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Derrotas_Newcastle_Total, label='Proyección de derrotas Newcastle')
  plt.plot(Temporadas_str, Derrotas_Everton_Total, label='Proyección de derrotas Everton')
  plt.title('Derrotas por temporada')
  plt.xlabel('Temporada')
  plt.ylabel('Derrotas')
  plt.legend()
  plt.grid()
  plt.show()
def gasto_neto_vs_valor_plantilla(Temporadas_str, Gasto_Neto_Newcastle, Valor_Plantillas_Newcastle, Gasto_Neto_Everton, Valor_Plantillas_Everton):
   
    plt.figure(figsize=(10, 6))
    plt.plot(Temporadas_str, Gasto_Neto_Newcastle, label='Gasto Neto Newcastle', marker='o')
    for i, valor in enumerate(Gasto_Neto_Newcastle):
        plt.annotate(f'{valor}', (Temporadas_str[i], Gasto_Neto_Newcastle[i]), textcoords="offset points", xytext=(0,5), ha='center')
    plt.plot(Temporadas_str, Valor_Plantillas_Newcastle, label='Valor de Plantilla Newcastle', marker='o')
    for i, valor in enumerate(Valor_Plantillas_Newcastle):
        plt.annotate(f'{valor}', (Temporadas_str[i], Valor_Plantillas_Newcastle[i]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.title('Gasto contra valor de plantillas Newcastle')
    plt.xlabel('Temporada')
    plt.ylabel('Gasto Neto / Valor de Plantilla')
    plt.legend()
    plt.grid()

    plt.figure(figsize=(10, 6))
    
    plt.plot(Temporadas_str, Gasto_Neto_Everton, label='Gasto Neto Everton', marker='o')

    for i, valor in enumerate(Gasto_Neto_Everton):
        plt.annotate(f'{valor}', (Temporadas_str[i], Gasto_Neto_Everton[i]), textcoords="offset points", xytext=(0,5), ha='center')

  
    plt.plot(Temporadas_str, Valor_Plantillas_Everton, label='Valor de Plantilla Everton', marker='o')
    
    for i, valor in enumerate(Valor_Plantillas_Everton):
        plt.annotate(f'{valor}', (Temporadas_str[i], Valor_Plantillas_Everton[i]), textcoords="offset points", xytext=(0,5), ha='center')

    plt.title('Gasto contra valor de plantillas Everton')
    plt.xlabel('Temporada')
    plt.ylabel('Gasto Neto / Valor de Plantilla')
    plt.legend()
    plt.grid()

    plt.show()

def posiciones_vs_temporada(Temporadas_str,Posicion_Newcastle,Posicion_Everton):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Posicion_Everton, label='Posiciones Everton')
  plt.plot(Temporadas_str, Posicion_Newcastle, label='Posiciones Newcastle')
  plt.title('Posición al final de temporada')
  plt.xlabel('Temporada')
  plt.ylabel('Posición')
  plt.legend()
  plt.grid()
  plt.gca().invert_yaxis()
  plt.show()
def puntos_vs_temporada(Temporadas_str,Puntos_Newcastle,Puntos_Everton):
  plt.figure(figsize=(10, 6))
  plt.plot(Temporadas_str, Puntos_Everton, label='Puntos Everton')
  plt.plot(Temporadas_str, Puntos_Newcastle, label='Puntos Newcastle')
  plt.title('Puntos al final de temporada')
  plt.xlabel('Temporada')
  plt.ylabel('Puntos')
  plt.legend()
  plt.grid()
  plt.show()
def correlaciones(Data_Frame_Newcastle_Transfermarkt,Data_Frame_Everton_Transfermarkt):
  plt.figure(figsize=(8,2))
  sns.heatmap(Data_Frame_Newcastle_Transfermarkt.corr(),annot=True, linewidth=0.5, cmap = 'magma')
  plt.title('Matriz de correlaciones de Newcastle')
  plt.show()
  plt.figure(figsize=(8,2))
  sns.heatmap(Data_Frame_Everton_Transfermarkt.corr(),annot=True, linewidth=0.5, cmap = 'magma')
  plt.title('Matriz de correlaciones de Everton')
  plt.show()


#Preparación para el data analysis (se suben los documentos para que se cree un pandas series)
Data_Frame_Newcastle_Transfermarkt = pd.read_csv('Newcastle_Transfermarkt.csv')
Data_Frame_Everton_Transfermarkt = pd.read_csv('Everton_Transfermarkt.csv')
Data_Frame_2017_2018 = pd.read_csv('2017-18.csv')
Data_Frame_2018_2019 = pd.read_csv('2018-19.csv')
Data_Frame_2019_2020 = pd.read_csv('2019-20.csv')
Data_Frame_2020_2021 = pd.read_csv('2020-21.csv')
Data_Frame_2021_2022 = pd.read_csv('2021-22.csv')
Data_Frame_2022_2023 = pd.read_csv('2022-23.csv')
Data_Frame_2023_2024 = pd.read_csv('2023-24.csv')
#Nos deshacemos de los tipos de datos "object", ya que Python no los entiende. Nótese que esto sólo se hace para los de las temporadas
Data_Frame_2017_2018_limpio=Data_Frame_2017_2018.select_dtypes(include=object).columns.tolist()
Data_Frame_2017_2018[Data_Frame_2017_2018_limpio] = Data_Frame_2017_2018[Data_Frame_2017_2018_limpio].astype(str)
Data_Frame_2018_2019_limpio=Data_Frame_2018_2019.select_dtypes(include=object).columns.tolist()
Data_Frame_2018_2019[Data_Frame_2018_2019_limpio] = Data_Frame_2017_2018[Data_Frame_2017_2018_limpio].astype(str)
Data_Frame_2019_2020_limpio=Data_Frame_2019_2020.select_dtypes(include=object).columns.tolist()
Data_Frame_2019_2020[Data_Frame_2019_2020_limpio] = Data_Frame_2019_2020[Data_Frame_2019_2020_limpio].astype(str)
Data_Frame_2020_2021_limpio=Data_Frame_2020_2021.select_dtypes(include=object).columns.tolist()
Data_Frame_2020_2021[Data_Frame_2020_2021_limpio] = Data_Frame_2020_2021[Data_Frame_2020_2021_limpio].astype(str)
Data_Frame_2021_2022_limpio=Data_Frame_2021_2022.select_dtypes(include=object).columns.tolist()
Data_Frame_2021_2022[Data_Frame_2021_2022_limpio] = Data_Frame_2021_2022[Data_Frame_2021_2022_limpio].astype(str)
Data_Frame_2022_2023_limpio=Data_Frame_2022_2023.select_dtypes(include=object).columns.tolist()
Data_Frame_2022_2023[Data_Frame_2022_2023_limpio] = Data_Frame_2022_2023[Data_Frame_2022_2023_limpio].astype(str)
Data_Frame_2023_2024_limpio=Data_Frame_2023_2024.select_dtypes(include=object).columns.tolist()
Data_Frame_2023_2024[Data_Frame_2023_2024_limpio] = Data_Frame_2023_2024[Data_Frame_2023_2024_limpio].astype(str)
"""
Datos Newcastle y Everton por temporada (separación de datos)
"""
#2017-18
Newcastle_Local_2017_2018 = Data_Frame_2017_2018[Data_Frame_2017_2018['HomeTeam']=='Newcastle']
Newcastle_Visita_2017_2018 = Data_Frame_2017_2018[Data_Frame_2017_2018['AwayTeam']=='Newcastle']
Everton_Local_2017_2018 = Data_Frame_2017_2018[Data_Frame_2017_2018['HomeTeam']=='Everton']
Everton_Visita_2017_2018 = Data_Frame_2017_2018[Data_Frame_2017_2018['AwayTeam']=='Everton']
#2018-19
Newcastle_Local_2018_2019 = Data_Frame_2018_2019[Data_Frame_2018_2019['HomeTeam']=='Newcastle']
Newcastle_Visita_2018_2019 = Data_Frame_2018_2019[Data_Frame_2018_2019['AwayTeam']=='Newcastle']
Everton_Local_2018_2019 = Data_Frame_2018_2019[Data_Frame_2018_2019['HomeTeam']=='Everton']
Everton_Visita_2018_2019 = Data_Frame_2018_2019[Data_Frame_2018_2019['AwayTeam']=='Everton']
#2019-20
Newcastle_Local_2019_2020 = Data_Frame_2019_2020[Data_Frame_2019_2020['HomeTeam']=='Newcastle']
Newcastle_Visita_2019_2020 = Data_Frame_2019_2020[Data_Frame_2019_2020['AwayTeam']=='Newcastle']
Everton_Local_2019_2020 = Data_Frame_2019_2020[Data_Frame_2019_2020['HomeTeam']=='Everton']
Everton_Visita_2019_2020 = Data_Frame_2019_2020[Data_Frame_2019_2020['AwayTeam']=='Everton']
#2020-21
Newcastle_Local_2020_2021 = Data_Frame_2020_2021[Data_Frame_2020_2021['HomeTeam']=='Newcastle']
Newcastle_Visita_2020_2021 = Data_Frame_2020_2021[Data_Frame_2020_2021['AwayTeam']=='Newcastle']
Everton_Local_2020_2021 = Data_Frame_2020_2021[Data_Frame_2020_2021['HomeTeam']=='Everton']
Everton_Visita_2020_2021 = Data_Frame_2020_2021[Data_Frame_2020_2021['AwayTeam']=='Everton']
#2021-22
Newcastle_Local_2021_2022 = Data_Frame_2021_2022[Data_Frame_2021_2022['HomeTeam']=='Newcastle']
Newcastle_Visita_2021_2022 = Data_Frame_2021_2022[Data_Frame_2021_2022['AwayTeam']=='Newcastle']
Everton_Local_2021_2022 = Data_Frame_2021_2022[Data_Frame_2021_2022['HomeTeam']=='Everton']
Everton_Visita_2021_2022 = Data_Frame_2021_2022[Data_Frame_2021_2022['AwayTeam']=='Everton']
#2022-23
Newcastle_Local_2022_2023 = Data_Frame_2022_2023[Data_Frame_2022_2023['HomeTeam']=='Newcastle']
Newcastle_Visita_2022_2023 = Data_Frame_2022_2023[Data_Frame_2022_2023['AwayTeam']=='Newcastle']
Everton_Local_2022_2023 = Data_Frame_2022_2023[Data_Frame_2022_2023['HomeTeam']=='Everton']
Everton_Visita_2022_2023 = Data_Frame_2022_2023[Data_Frame_2022_2023['AwayTeam']=='Everton']
#2023-24
Newcastle_Local_2023_2024 = Data_Frame_2022_2023[Data_Frame_2022_2023['HomeTeam']=='Newcastle']
Newcastle_Visita_2023_2024 = Data_Frame_2022_2023[Data_Frame_2022_2023['AwayTeam']=='Newcastle']
Everton_Local_2023_2024 = Data_Frame_2022_2023[Data_Frame_2022_2023['HomeTeam']=='Everton']
Everton_Visita_2023_2024 = Data_Frame_2022_2023[Data_Frame_2022_2023['AwayTeam']=='Everton']
"""
Datos Transfersmarkt por equipo
"""
#Newcastle
Valor_Plantillas_Newcastle=Data_Frame_Newcastle_Transfermarkt['Valor Plantilla']
Gasto_Neto_Newcastle=Data_Frame_Newcastle_Transfermarkt['Gasto Neto']
Posicion_Newcastle=Data_Frame_Newcastle_Transfermarkt['Standings']
Puntos_Newcastle=Data_Frame_Newcastle_Transfermarkt['Puntos']
#Everton
Valor_Plantillas_Everton=Data_Frame_Everton_Transfermarkt['Valor Plantilla']
Posicion_Everton=Data_Frame_Everton_Transfermarkt['Standings']
Gasto_Neto_Everton=Data_Frame_Everton_Transfermarkt['Gasto Neto']
Puntos_Everton=Data_Frame_Everton_Transfermarkt['Puntos']
"""
Temporadas que se analizarán
"""
temporadas=[["2017-18"],["2018-19"],["2019-20"],["2020-21"],["2021-22"],["2022-23"],["2023-24"]]
"""
Extracción de datos para análisis deportivo
"""
#2017-16
#Newcastle
Resultados_Local=list(Newcastle_Local_2017_2018['FTR'])
Resultados_Visita=list(Newcastle_Visita_2017_2018['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2017_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2017_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2017_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2017=list(Newcastle_Local_2017_2018['FTHG'])
Goles_Visita_Newcastle_2017=list(Newcastle_Visita_2017_2018['FTAG'])
Goles_Newcastle_2017=sum(Goles_Local_Newcastle_2017)+sum(Goles_Visita_Newcastle_2017)
Goles_Recibidos_Local_Newcastle_2017=list(Newcastle_Local_2017_2018['FTAG'])
Goles_Recibidos_Visita_Newcastle_2017=list(Newcastle_Visita_2017_2018['FTHG'])
Goles_Recibidos_Newcastle_2017=sum(Goles_Recibidos_Local_Newcastle_2017)+sum(Goles_Recibidos_Visita_Newcastle_2017)
#Everton
Resultados_Local=list(Everton_Local_2017_2018['FTR'])
Resultados_Visita=list(Everton_Visita_2017_2018['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2017_Everton=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2017_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2017_Everton=(Empates_Local+Empates_Visita)
Goles_Local_Everton_2017=list(Everton_Local_2017_2018['FTHG'])
Goles_Visita_Everton_2017=list(Everton_Visita_2017_2018['FTAG'])
Goles_Everton_2017=sum(Goles_Local_Everton_2017)+sum(Goles_Visita_Everton_2017)
Goles_Recibidos_Local_Everton_2017 = list(Everton_Local_2017_2018['FTAG'])
Goles_Recibidos_Visita_Everton_2017 = list(Everton_Visita_2017_2018['FTHG'])
Goles_Recibidos_Everton_2017 = sum(Goles_Recibidos_Local_Everton_2017) + sum(Goles_Recibidos_Visita_Everton_2017)
#2018-19
#Newcastle
Resultados_Local=list(Newcastle_Local_2018_2019['FTR'])
Resultados_Visita=list(Newcastle_Visita_2018_2019['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2018_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2018_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2018_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2018=list(Newcastle_Local_2018_2019['FTHG'])
Goles_Visita_Newcastle_2018=list(Newcastle_Visita_2018_2019['FTAG'])
Goles_Newcastle_2018=sum(Goles_Local_Newcastle_2018)+sum(Goles_Visita_Newcastle_2018)
Goles_Recibidos_Local_Newcastle_2018 = list(Newcastle_Local_2018_2019['FTAG'])
Goles_Recibidos_Visita_Newcastle_2018 = list(Newcastle_Visita_2018_2019['FTHG'])
Goles_Recibidos_Newcastle_2018 = sum(Goles_Recibidos_Local_Newcastle_2018) + sum(Goles_Recibidos_Visita_Newcastle_2018)
#Everton
Resultados_Local=list(Everton_Local_2018_2019['FTR'])
Resultados_Visita=list(Everton_Visita_2018_2019['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2018_Everton=Victorias_Local+Victorias_Visita+2
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2018_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2018_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2018=list(Everton_Local_2018_2019['FTHG'])
Goles_Visita_Everton_2018=list(Everton_Visita_2018_2019['FTAG'])
Goles_Everton_2018=sum(Goles_Local_Everton_2018)+sum(Goles_Visita_Everton_2018)
Goles_Recibidos_Local_Everton_2018 = list(Everton_Local_2018_2019['FTAG'])
Goles_Recibidos_Visita_Everton_2018 = list(Everton_Visita_2018_2019['FTHG'])
Goles_Recibidos_Everton_2018 = sum(Goles_Recibidos_Local_Everton_2018) + sum(Goles_Recibidos_Visita_Everton_2018)
#2019-20
#Newcastle
Resultados_Local=list(Newcastle_Local_2019_2020['FTR'])
Resultados_Visita=list(Newcastle_Visita_2019_2020['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2019_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2019_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2019_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2019=list(Newcastle_Local_2019_2020['FTHG'])
Goles_Visita_Newcastle_2019=list(Newcastle_Visita_2019_2020['FTAG'])
Goles_Newcastle_2019=sum(Goles_Local_Newcastle_2019)+sum(Goles_Visita_Newcastle_2019)
Goles_Recibidos_Local_Newcastle_2019 = list(Newcastle_Local_2019_2020['FTAG'])
Goles_Recibidos_Visita_Newcastle_2019 = list(Newcastle_Visita_2019_2020['FTHG'])
Goles_Recibidos_Newcastle_2019 = sum(Goles_Recibidos_Local_Newcastle_2019) + sum(Goles_Recibidos_Visita_Newcastle_2019)
#Everton
Resultados_Local=list(Everton_Local_2019_2020['FTR'])
Resultados_Visita=list(Everton_Visita_2019_2020['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2019_Everton=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2019_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2019_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2019=list(Everton_Local_2019_2020['FTHG'])
Goles_Visita_Everton_2019=list(Everton_Visita_2019_2020['FTAG'])
Goles_Everton_2019=sum(Goles_Local_Everton_2019)+sum(Goles_Visita_Everton_2019)
Goles_Recibidos_Local_Everton_2019 = list(Everton_Local_2019_2020['FTAG'])
Goles_Recibidos_Visita_Everton_2019 = list(Everton_Visita_2019_2020['FTHG'])
Goles_Recibidos_Everton_2019 = sum(Goles_Recibidos_Local_Everton_2019) + sum(Goles_Recibidos_Visita_Everton_2019)
#2020-21
#Newcastle
Resultados_Local=list(Newcastle_Local_2020_2021['FTR'])
Resultados_Visita=list(Newcastle_Visita_2020_2021['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2020_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2020_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2020_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2020=list(Newcastle_Local_2020_2021['FTHG'])
Goles_Visita_Newcastle_2020=list(Newcastle_Visita_2020_2021['FTAG'])
Goles_Newcastle_2020=sum(Goles_Local_Newcastle_2020)+sum(Goles_Visita_Newcastle_2020)
Goles_Recibidos_Local_Newcastle_2020 = list(Newcastle_Local_2020_2021['FTAG'])
Goles_Recibidos_Visita_Newcastle_2020 = list(Newcastle_Visita_2020_2021['FTHG'])
Goles_Recibidos_Newcastle_2020 = sum(Goles_Recibidos_Local_Newcastle_2020) + sum(Goles_Recibidos_Visita_Newcastle_2020)
#Everton
Resultados_Local=list(Everton_Local_2020_2021['FTR'])
Resultados_Visita=list(Everton_Visita_2020_2021['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2020_Everton=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2020_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2020_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2020=list(Everton_Local_2020_2021['FTHG'])
Goles_Visita_Everton_2020=list(Everton_Visita_2020_2021['FTAG'])
Goles_Everton_2020=sum(Goles_Local_Everton_2020)+sum(Goles_Visita_Everton_2020)
Goles_Recibidos_Local_Everton_2020 = list(Everton_Local_2020_2021['FTAG'])
Goles_Recibidos_Visita_Everton_2020 = list(Everton_Visita_2020_2021['FTHG'])
Goles_Recibidos_Everton_2020 = sum(Goles_Recibidos_Local_Everton_2020) + sum(Goles_Recibidos_Visita_Everton_2020)
#2021-22
#Newcastle
Resultados_Local=list(Newcastle_Local_2021_2022['FTR'])
Resultados_Visita=list(Newcastle_Visita_2021_2022['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2021_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2021_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2021_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2021=list(Newcastle_Local_2021_2022['FTHG'])
Goles_Visita_Newcastle_2021=list(Newcastle_Visita_2021_2022['FTAG'])
Goles_Newcastle_2021=sum(Goles_Local_Newcastle_2021)+sum(Goles_Visita_Newcastle_2021)
Goles_Recibidos_Local_Newcastle_2021 = list(Newcastle_Local_2021_2022['FTAG'])
Goles_Recibidos_Visita_Newcastle_2021 = list(Newcastle_Visita_2021_2022['FTHG'])
Goles_Recibidos_Newcastle_2021 = sum(Goles_Recibidos_Local_Newcastle_2021) + sum(Goles_Recibidos_Visita_Newcastle_2021)
#Everton
Resultados_Local=list(Everton_Local_2021_2022['FTR'])
Resultados_Visita=list(Everton_Visita_2021_2022['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2021_Everton=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2021_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2021_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2021=list(Newcastle_Local_2021_2022['FTHG'])
Goles_Visita_Everton_2021=list(Newcastle_Visita_2021_2022['FTAG'])
Goles_Everton_2021=sum(Goles_Local_Everton_2021)+sum(Goles_Visita_Everton_2021)
Goles_Recibidos_Local_Everton_2021 = list(Everton_Local_2021_2022['FTAG'])
Goles_Recibidos_Visita_Everton_2021 = list(Everton_Visita_2021_2022['FTHG'])
Goles_Recibidos_Everton_2021 = sum(Goles_Recibidos_Local_Everton_2021) + sum(Goles_Recibidos_Visita_Everton_2021)
#2022-23
#Newcastle
Resultados_Local=list(Newcastle_Local_2022_2023['FTR'])
Resultados_Visita=list(Newcastle_Visita_2022_2023['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2022_Newcastle=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2022_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2022_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2022=list(Newcastle_Local_2022_2023['FTHG'])
Goles_Visita_Newcastle_2022=list(Newcastle_Visita_2022_2023['FTAG'])
Goles_Newcastle_2022=sum(Goles_Local_Newcastle_2022)+sum(Goles_Visita_Newcastle_2022)
Goles_Recibidos_Local_Newcastle_2022 = list(Newcastle_Local_2022_2023['FTAG'])
Goles_Recibidos_Visita_Newcastle_2022 = list(Newcastle_Visita_2022_2023['FTHG'])
Goles_Recibidos_Newcastle_2022 = sum(Goles_Recibidos_Local_Newcastle_2022) + sum(Goles_Recibidos_Visita_Newcastle_2022)
#Everton
Resultados_Local=list(Everton_Local_2022_2023['FTR'])
Resultados_Visita=list(Everton_Visita_2022_2023['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2022_Everton=Victorias_Local+Victorias_Visita
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2022_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2022_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2022=list(Everton_Local_2022_2023['FTHG'])
Goles_Visita_Everton_2022=list(Everton_Visita_2022_2023['FTAG'])
Goles_Everton_2022=sum(Goles_Local_Everton_2022)+sum(Goles_Visita_Everton_2022)
Goles_Recibidos_Local_Everton_2022 = list(Everton_Local_2022_2023['FTAG'])
Goles_Recibidos_Visita_Everton_2022 = list(Everton_Visita_2022_2023['FTHG'])
Goles_Recibidos_Everton_2022 = sum(Goles_Recibidos_Local_Everton_2022) + sum(Goles_Recibidos_Visita_Everton_2022)
#2023-24
#Newcastle
Resultados_Local=list(Newcastle_Local_2023_2024['FTR'])
Resultados_Visita=list(Newcastle_Visita_2023_2024['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2023_Newcastle=Victorias_Local+Victorias_Visita-1
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2023_Newcastle=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2023_Newcastle=Empates_Local+Empates_Visita
Goles_Local_Newcastle_2023=list(Newcastle_Local_2023_2024['FTHG'])
Goles_Visita_Newcastle_2023=list(Newcastle_Visita_2023_2024['FTAG'])
Goles_Newcastle_2023=sum(Goles_Local_Newcastle_2023)+sum(Goles_Visita_Newcastle_2023)-6
Goles_Recibidos_Local_Newcastle_2023 = list(Newcastle_Local_2023_2024['FTAG'])
Goles_Recibidos_Visita_Newcastle_2023 = list(Newcastle_Visita_2023_2024['FTHG'])
Goles_Recibidos_Newcastle_2023 = sum(Goles_Recibidos_Local_Newcastle_2023) + sum(Goles_Recibidos_Visita_Newcastle_2023)
#Everton
Resultados_Local=list(Everton_Local_2023_2024['FTR'])
Resultados_Visita=list(Everton_Visita_2023_2024['FTR'])
Victorias_Local=Resultados_Local.count('H')
Victorias_Visita=Resultados_Visita.count('A')
Victorias2023_Everton=Victorias_Local+Victorias_Visita+5
Derrotas_Local=Resultados_Local.count('A')
Derrotas_Visita=Resultados_Local.count('H')
Derrotas2023_Everton=Derrotas_Local+Derrotas_Visita
Empates_Local=Resultados_Local.count('D')
Empates_Visita=Resultados_Local.count('D')
Empates2023_Everton=Empates_Local+Empates_Visita
Goles_Local_Everton_2023=list(Everton_Local_2023_2024['FTHG'])
Goles_Visita_Everton_2023=list(Everton_Visita_2023_2024['FTAG'])
Goles_Everton_2023=sum(Goles_Local_Everton_2023)+sum(Goles_Visita_Everton_2023)+6
Goles_Recibidos_Local_Everton_2023 = list(Everton_Local_2023_2024['FTAG'])
Goles_Recibidos_Visita_Everton_2023 = list(Everton_Visita_2023_2024['FTHG'])
Goles_Recibidos_Everton_2023 = sum(Goles_Recibidos_Local_Everton_2023) + sum(Goles_Recibidos_Visita_Everton_2023)
"""
Se crean listas en las que está la información TOTAL (local + visita) que se utilizará en las gráficas.
"""
Victorias_Newcastle_Total=[Victorias2017_Newcastle,Victorias2018_Newcastle,Victorias2019_Newcastle,Victorias2020_Newcastle,Victorias2021_Newcastle,Victorias2022_Newcastle,Victorias2023_Newcastle]
Victorias_Everton_Total=[Victorias2017_Everton,Victorias2018_Everton,Victorias2019_Everton,Victorias2020_Everton,Victorias2021_Everton,Victorias2022_Everton,Victorias2023_Everton]
Derrotas_Newcastle_Total=[Derrotas2017_Newcastle,Derrotas2018_Newcastle,Derrotas2019_Newcastle,Derrotas2020_Newcastle,Derrotas2021_Newcastle,Derrotas2022_Newcastle-7,Derrotas2023_Newcastle+1]
Derrotas_Everton_Total=[Derrotas2017_Everton,Derrotas2018_Everton,Derrotas2019_Everton,Derrotas2020_Everton,Derrotas2021_Everton,Derrotas2022_Everton+2,Derrotas2023_Everton]
Empates_Newcastle_Total=[Empates2017_Newcastle,Empates2018_Newcastle,Empates2019_Newcastle,Empates2020_Newcastle,Empates2021_Newcastle,Empates2022_Newcastle,Empates2023_Newcastle]
Empates_Everton_Total=[Empates2017_Everton,Empates2018_Everton,Empates2019_Everton,Empates2020_Everton,Empates2021_Everton,Empates2022_Everton,Empates2023_Everton]
Goles_Totales_Everton=[Goles_Everton_2017,Goles_Everton_2018,Goles_Everton_2019,Goles_Everton_2020,Goles_Everton_2021,Goles_Everton_2022,Goles_Everton_2023]
Goles_Totales_Newcastle=[Goles_Newcastle_2017,Goles_Newcastle_2018,Goles_Newcastle_2019,Goles_Newcastle_2020,Goles_Newcastle_2021,Goles_Newcastle_2022,Goles_Newcastle_2023]
Goles_Recibidos_Totales_Everton = [Goles_Recibidos_Everton_2017,Goles_Recibidos_Everton_2018,Goles_Recibidos_Everton_2019,Goles_Recibidos_Everton_2020,Goles_Recibidos_Everton_2021,Goles_Recibidos_Everton_2022,Goles_Recibidos_Everton_2023-6]
Goles_Recibidos_Totales_Newcastle = [Goles_Recibidos_Newcastle_2017,Goles_Recibidos_Newcastle_2018,Goles_Recibidos_Newcastle_2019,Goles_Recibidos_Newcastle_2020,Goles_Recibidos_Newcastle_2021,Goles_Recibidos_Newcastle_2022,Goles_Recibidos_Newcastle_2023+29]

"""
Programa de análisis de datos
"""
usuario = str(input("Introduce el usuario: "))
with open("texto.txt", "w") as archivo:
    archivo.write(f"Usuario: {usuario}\nHistorial de busqueda: \n")
while True:
    print("¿Qué acción deseas realizar?")
    print("1: Visualizar Gráficas y reporte de rendimiento por partido")
    print("2: Visualizar Gráficas económicas")
    print("3: Visualizar Gráficas y estadísticas de rendimiento por temporada")
    print("4: Desas salir?")
    accion=int(input("Introduce tu acción: "))
    if accion==1:
        print("Visualizar Gráficas de rendimiento por partido")
        with open("texto.txt", "a") as archivo:
            archivo.write("Accedio: Graficas de rendimiento deportivo\n") #Escribiendo el archivo
            archivo.close()#Liberamos el archivo
        while True:
            print("1: Visualizar Gráfica de Victorias")
            print("2: Visualizar Gráfica de Goles Anotados")
            print("3: Visualizar Gráfica de Goles Recibidos")
            print("4: Visualizar Gráfica de Derrotas")
            print("5: Visualizar reporte de rendimiento")
            print("6: Salir de Gráficas de rendimientos por partido")
            rendimiento=int(input("¿Qué deseas visualizar? "))
            if rendimiento==1:
                temporadas_str = [t[0] for t in temporadas]
                victorias_en_temporada(temporadas_str,Victorias_Newcastle_Total,Victorias_Everton_Total)
                print("Se observa la gráfica de victorias por equipo.")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Victorias\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Victorias\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
            elif rendimiento==2:
                temporadas_str = [t[0] for t in temporadas]
                goles_anotados(Goles_Totales_Newcastle,Goles_Totales_Everton,temporadas_str)
                print("Se observa la gráfica de goles anotados.")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Goles Anotados\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
            elif rendimiento==3:
                temporadas_str = [t[0] for t in temporadas]
                goles_recibidos(Goles_Recibidos_Totales_Newcastle,Goles_Recibidos_Totales_Everton,temporadas_str)
                print("Se visualiza la grafica de goles recibidos.")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Goles Recibidos\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
            elif rendimiento==4:
                temporadas_str = [t[0] for t in temporadas]
                derrotas_en_temporada(temporadas_str,Victorias_Newcastle_Total,Victorias_Everton_Total)
                print("Se visualiza la grafica de derrotas.")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Derrotas\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
            elif rendimiento==5:
              print("Reporte de Rendimiento")
              season=("17/18","18/19","19/20","20/21","21/22","22/23","23/24")
              print(f"Temporadas: {season}")
              tupla_victorias_newcastle = tuple(Victorias_Newcastle_Total)
              tupla_victorias_everton = tuple(Victorias_Everton_Total)
              tupla_derrotas_newcastle = tuple(Derrotas_Newcastle_Total)
              tupla_derrotas_everton = tuple(Derrotas_Everton_Total)
              tupla_goles_newcastle = tuple(Goles_Totales_Newcastle)
              tupla_goles_everton = tuple(Goles_Totales_Everton)
              tupla_goles_recibidos_newcastle = tuple(Goles_Recibidos_Totales_Newcastle)
              tupla_goles_recibidos_everton = tuple(Goles_Recibidos_Totales_Everton)

    
              print(f"Goles anotados por temporada para Newcastle: {tupla_goles_newcastle}")
              print(f"Goles anotados por temporada para Everton: {tupla_goles_everton}")
              print(f"Goles recibidos por temporada para Newcastle: {tupla_goles_recibidos_newcastle}")
              print(f"Goles recibidos por temporada para Everton: { tupla_goles_recibidos_everton}")
              print(f"Victorias por temporada para Newcastle: {tupla_victorias_newcastle}")
              print(f"Victorias por temporada para Everton: {tupla_victorias_everton}")
              print(f"Derrotas por temporada para Newcastle: {tupla_derrotas_newcastle}")
              print(f"Derrotas por temporada para Everton: {tupla_derrotas_everton}")
              
              

              with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Reporte de Rendimiento\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
            elif rendimiento==6:
                print("Saliendo de Gráficas de Rendimiento por partido")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Salio: Graficas de Rendimiento por partido\n") #Escribiendo el archivo
                    archivo.close()#Liberamos el archivo
                    break
            else:
                print("Esa opción no se encuentra")
                break
    elif accion==2:
        print("Gráficas Económicas")
        with open("texto.txt", "a") as archivo:
            archivo.write("Accedio: Graficas Economicas\n")
            archivo.close()
        while True:
            print("1: Gráfica de Gasto Neto vs valor de la plantilla")
            print("2: Salir de Gráficas Económicas")
            economia=int(input("¿Qué deseas Visualizar? "))
            if economia==1:
                temporadas_str = [t[0] for t in temporadas]
                gasto_neto_vs_valor_plantilla(temporadas_str,Gasto_Neto_Newcastle,Valor_Plantillas_Newcastle,Gasto_Neto_Everton,Valor_Plantillas_Everton)
                print("Se visualiza la Gráfica de Gasto Neto vs Valor de la plantilla")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Grafica de Gasto Neto vs Valor de la Plantilla \n")
                    archivo.close()
            elif economia==2:
                print("Saliendo de Gráficas Económicas")
                with open("texto.txt", "a") as archivo:
                    archivo.write("Salio: Graficas Economicas \n")
                    archivo.close()
                    break
            else:
                print("Esa opción no se encuentra")
                break
    elif accion==3:
        print("Gráficas y estadísticas de rendimiento por temporada")
        with open("texto.txt", "a") as archivo:
            archivo.write("Accedio: Visualizar Gráficas y estadisticas de rendimiento por temporada \n")
            archivo.close()


        while True:
          print("1: Gráfica de posiciones vs temporada ")
          print("2: Grafica de puntos vs temporada")
          print("3: Graficas de correlación")
          print("4: Estadísticas por temporada")
          print("5: Salir de Gráficas de rendimiento por temporada")
          eleccion=int(input("¿Qué deseas Visualizar? "))
          if eleccion==1:
            temporadas_str = [t[0] for t in temporadas]
            posiciones_vs_temporada(temporadas_str,Posicion_Newcastle,Posicion_Everton)
            print("Se visualiza la grafica de posiciones versus temporadas.")
            with open("texto.txt", "a") as archivo:
                archivo.write("Accedio: Posiciones por temporada  \n")
                archivo.close()
          elif eleccion==2:
              temporadas_str = [t[0] for t in temporadas]
              puntos_vs_temporada(temporadas_str,Puntos_Newcastle,Puntos_Everton)
              print("Se visualiza la grafica de puntos versus temporadas.")
              with open("texto.txt", "a") as archivo:
                  archivo.write("Accedio: Puntos por temporada  \n")
                  archivo.close()
          elif eleccion==3:
              temporadas_str = [t[0] for t in temporadas]
              correlaciones(Data_Frame_Newcastle_Transfermarkt,Data_Frame_Everton_Transfermarkt)
              print("Se visualiza la grafica de correlación.")
              with open("texto.txt", "a") as archivo:
                  archivo.write("Accedio: Correlación entre variables  \n")
                  archivo.close()
          elif eleccion == 4:
              with open("texto.txt", "a") as archivo:
                  archivo.write("Accedio: Estadísticas por temporada \n")
                  archivo.close()
              while True:
                print("1: Porcentaje de victorias por temporada")
                print("2: Porcentaje de derrotas por temporada")
                print("3: Salir de estadísticas por temporada")
                esta=int(input("¿Qué acción deseas realizar?"))
                if esta==1:
                  print("Porcentaje de victorias por temporada")
                  partidos_totales = 38

                  # Porcentaje de victorias para cada temporada
                  porcentaje_victorias_newcastle = [(victorias / partidos_totales) * 100 for victorias in Victorias_Newcastle_Total]
                  porcentaje_victorias_everton = [(victorias / partidos_totales) * 100 for victorias in Victorias_Everton_Total]

                  dict_porcentaje_victorias={}

                  temporadas_str = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24']
                  for i in range(len(temporadas_str)):
                    dict_porcentaje_victorias[temporadas_str[i]] = {'porcentaje_victorias_newcastle': porcentaje_victorias_newcastle[i],
                    'porcentaje_victorias_everton': porcentaje_victorias_everton[i]}
                  
                  print(f"Porcentajes por temporada: {dict_porcentaje_victorias}")
                  
                  with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Vitorias por temporada\n")
                    archivo.close()
                  
                elif esta==2:
                  print("Porcentaje de derrotas por temporada")
                  partidos_totales = 38

                  # Porcentaje de derrotas para cada temporada
                  porcentaje_derrotas_newcastle = [(derrotas / partidos_totales) * 100 for derrotas in Derrotas_Newcastle_Total]
                  porcentaje_derrotas_everton = [(derrotas / partidos_totales) * 100 for derrotas in Derrotas_Everton_Total]
                  
                  
                  dict_porcentaje_derrotas={}

                  temporadas_str = ['2017-18', '2018-19', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24']
                  
                  for i in range(len(temporadas_str)):
                    dict_porcentaje_derrotas[temporadas_str[i]] = {'porcentaje_derrotas_newcastle': porcentaje_derrotas_newcastle[i],
                    'porcentaje_derrotas_everton': porcentaje_derrotas_everton[i]}
                  
                  print(f"Porcentajes por temporada: {dict_porcentaje_derrotas}")
                 
                 
                  with open("texto.txt", "a") as archivo:
                    archivo.write("Accedio: Derrotas por temporada\n")
                    archivo.close()

                elif esta==3:
                  print("Saliendo de estadísticas por temporada")
                  with open("texto.txt", "a") as archivo:
                    archivo.write("Salio: Estadisticas por temporada\n")
                    archivo.close()
                    break
                else:
                  print("Esa opción no se encuentra")
                

              
          
          elif eleccion == 5:
              with open("texto.txt", "a") as archivo:
                  archivo.write("Salió de Gráficas de rendimiento por temporada \n")
                  archivo.close()
              break
          else:
              print("Esa opción no se encuentra")
              break
    elif accion==4:
        Nombres={"Luis Enrique Aguilera Novoa","Angelo Dayvis Farfán Torres","Pablo Emiliano González Ríos"}
        print(f"Creado por: {Nombres}")

        print(f"Adiós {usuario}, Gracias por utilizar este software altamente especializado en el fulbito")
        with open("texto.txt", "a") as archivo:
            archivo.write("Salio\n")
            archivo.close()
        break
    else:
        print("No se encuentra esa opción")
        break