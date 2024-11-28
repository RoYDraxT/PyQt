import pandas as pd

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
    
datos = cargar_datos(archivo="Residuos2024.xlsx")

def calcular_promedio_residuos_por_habitante(datos):
    """
    Calcula el promedio de residuos anuales por habitante en cada distrito.

    Args:
        datos (list of list): Lista de datos donde cada fila contiene:
            [Departamento, Provincia, Distrito, Población, ResiduosAnuales].

    Returns:
        list: Una lista de diccionarios con el promedio de residuos por habitante para cada distrito.
    """
    resultados = []
    for fila in datos:
        departamento, provincia, distrito, poblacion, residuos_anuales = fila
        if poblacion > 0:  # Evita divisiones por cero
            promedio = round(residuos_anuales / poblacion, 2)
            resultados.append({
                "Departamento": departamento,
                "Provincia": provincia,
                "Distrito": distrito,
                "Promedio por Habitante": promedio
            })
        else:
            resultados.append({
                "Departamento": departamento,
                "Provincia": provincia,
                "Distrito": distrito,
                "Promedio por Habitante": "N/A"
            })
    
    return resultados

def calcular_promedio_total_residuos(datos):
    """
    Calcula el promedio total de residuos anuales en todas las zonas.

    Args:
        datos (list of list): Lista de datos donde cada fila contiene:
            [Departamento, Provincia, Distrito, Población, ResiduosAnuales].

    Returns:
        float: El promedio total de residuos anuales en todas las zonas.
    """
    total_residuos = 0
    for fila in datos:
        _, _, _, _, residuos_anuales = fila
        total_residuos += residuos_anuales
    
    promedio_total_residuos = round(total_residuos / len(datos), 2) if len(datos) > 0 else 0
    return promedio_total_residuos

def calcular_promedio_residuos_por_zona(datos):
    """
    Calcula el promedio de residuos anuales por zona.

    Args:
        datos (list of list): Lista de datos donde cada fila contiene:
            [Departamento, Provincia, Distrito, Población, ResiduosAnuales].

    Returns:
        float: El promedio de residuos anuales por zona.
    """
    total_residuos = 0
    num_zonas = len(datos)
    
    for fila in datos:
        _, _, _, _, residuos_anuales = fila
        total_residuos += residuos_anuales
    
    promedio_residuos_zona = round(total_residuos / num_zonas, 2) if num_zonas > 0 else 0
    return promedio_residuos_zona