import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# Lectura de datos
def cargar_datos(archivo='Residuos2024.xlsx'):
    """
    Carga los datos desde un archivo Excel.

    Args:
        archivo (str): Nombre del archivo Excel.

    Returns:
        list of list: Lista con los datos cargados.
    """
    try:
        datos = pd.read_excel(archivo)
        return datos.values.tolist()
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    
def transformar_datos(datos):
    """
    Transforma los datos eliminando columnas irrelevantes y agrupando por DEPARTAMENTO y REG_NAT.
    
    Args:
        datos (list of list): Lista de listas con los datos.

    Returns:
        DataFrame: DataFrame con los datos agrupados por DEPARTAMENTO y REG_NAT.
    """
    # Convertir la lista de listas a DataFrame para manipularlo fácilmente
    columnas = ['FECHA_CORTE', 'N_SEC', 'UBIGEO', 'REG_NAT', 'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'POB_TOTAL', 'POB_URBANA', 'POB_RURAL', 'QRESIDUOS_DOM', 'PERIODO']
    df = pd.DataFrame(datos, columns=columnas)

    # Eliminar columnas irrelevantes
    columnas_a_eliminar = ['FECHA_CORTE', 'N_SEC', 'UBIGEO', 'PROVINCIA', 'DISTRITO']
    df = df.drop(columns=columnas_a_eliminar, errors='ignore')

    # Eliminar filas con valores nulos
    df = df.dropna()

    # Agrupar por DEPARTAMENTO y REG_NAT
    df_agrupado = df.groupby(['REG_NAT', 'DEPARTAMENTO', 'PERIODO']).agg({
        'POB_TOTAL': 'sum',
        'POB_URBANA': 'sum',
        'POB_RURAL': 'sum',
        'QRESIDUOS_DOM': 'sum'
    }).reset_index()

    return df_agrupado

def calcular_residuos_por_ano_seleccionado(datos_agrupados, año_seleccionado=None, departamento_seleccionado=None):
    """
    Calcula los residuos totales generados por año y departamento. Si no se selecciona un año específico, calcula el promedio.
    
    Args:
        datos_agrupados (DataFrame): DataFrame con los datos agrupados por DEPARTAMENTO y PERIODO.
        año_seleccionado (int, optional): Año específico seleccionado por el usuario. Si es None, se calcula para todos los años.
        departamento_seleccionado (str, optional): Departamento específico seleccionado por el usuario. Si es None, se calcula para todos los departamentos.
        
    Returns:
        float: Residuos totales para un año seleccionado o el promedio de residuos para todos los años y departamentos.
    """
    if departamento_seleccionado is not None:
        # Filtrar los datos por el departamento seleccionado
        datos_agrupados = round((datos_agrupados[datos_agrupados['DEPARTAMENTO'] == departamento_seleccionado]),2)

    if año_seleccionado is not None:
        # Filtrar los datos por el año seleccionado
        residuos_por_ano = round((datos_agrupados[datos_agrupados['PERIODO'] == año_seleccionado]),2)
        
        # Sumar los residuos de ese año y departamento
        residuos_totales = round((residuos_por_ano['QRESIDUOS_DOM'].sum()),2)
        
        return residuos_totales
    else:
        # Si no se seleccionó un año específico, calcular el promedio de residuos
        residuos_totales = round((datos_agrupados['QRESIDUOS_DOM'].sum()),2)
        total_anos = len(datos_agrupados['PERIODO'].unique())
        
        # Calcular el promedio de residuos
        promedio_residuos = round((residuos_totales / total_anos),2)
        
        return promedio_residuos

def calcular_residuos_por_region(datos_agrupados, regiones_seleccionadas, año_seleccionado=None):
    """
    Calcula los residuos totales generados por las regiones, con la opción de filtrar por año.

    Args:
        datos_agrupados (DataFrame): DataFrame con los datos agrupados por región y departamento.
        regiones_seleccionadas (list): Lista de regiones seleccionadas.
        año_seleccionado (int, optional): Año específico seleccionado. Si es None, no se filtra por año.

    Returns:
        DataFrame o float: Si se selecciona un año, devuelve el valor de residuos para ese año. Si no, no devuelve nada.
    """
    # Filtrar los datos por las regiones seleccionadas
    datos_filtrados = round((datos_agrupados[datos_agrupados['REG_NAT'].isin(regiones_seleccionadas)]),2)

    if año_seleccionado:
        # Filtrar también por el año si se seleccionó un año específico
        datos_filtrados = round((datos_filtrados[datos_filtrados['PERIODO'] == año_seleccionado]),2)

    # Calcular los residuos totales para las regiones seleccionadas
    residuos_totales = round((datos_filtrados['QRESIDUOS_DOM'].sum()),2)

    return residuos_totales
