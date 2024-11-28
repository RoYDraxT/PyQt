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
    Transforma los datos eliminando columnas irrelevantes y agrupando por DEPARTAMENTO.
    
    Args:
        datos (list of list): Lista de listas con los datos.

    Returns:
        list of list: Lista de listas con los datos agrupados por DEPARTAMENTO.
    """
    # Convertir la lista de listas a DataFrame para manipularlo fácilmente
    columnas = ['FECHA_CORTE', 'N_SEC', 'UBIGEO', 'REG_NAT', 'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO', 'POB_TOTAL', 'POB_URBANA', 'POB_RURAL', 'QRESIDUOS_DOM', 'PERIODO']
    df = pd.DataFrame(datos, columns=columnas)

    columnas_a_eliminar = ['FECHA_CORTE', 'N_SEC', 'UBIGEO', 'PROVINCIA', 'DISTRITO']
    df = df.drop(columns=columnas_a_eliminar, errors='ignore')

    df = df.dropna()

    df_agrupado = df.groupby(['DEPARTAMENTO', 'PERIODO']).agg({
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
        datos_agrupados = datos_agrupados[datos_agrupados['DEPARTAMENTO'] == departamento_seleccionado]

    if año_seleccionado is not None:
        # Filtrar los datos por el año seleccionado
        residuos_por_ano = datos_agrupados[datos_agrupados['PERIODO'] == año_seleccionado]
        
        # Sumar los residuos de ese año y departamento
        residuos_totales = residuos_por_ano['QRESIDUOS_DOM'].sum()
        
        return residuos_totales
    else:
        # Si no se seleccionó un año específico, calcular el promedio de residuos
        residuos_totales = datos_agrupados['QRESIDUOS_DOM'].sum()
        total_anos = len(datos_agrupados['PERIODO'].unique())
        
        # Calcular el promedio de residuos
        promedio_residuos = round((residuos_totales / total_anos),2)
        
        return promedio_residuos
