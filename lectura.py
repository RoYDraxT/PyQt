import pandas as pd

def cargar_datos():
    archivo = 'Residuos2024.xlsx'
    try:
        datos = pd.read_excel(archivo)
        return datos.values.tolist()
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
