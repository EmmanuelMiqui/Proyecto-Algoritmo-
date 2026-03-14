import requests
import json
# Aquí importarías tus clases: from Profesores import Profesor

def descargar_datos_github():
    """
    Descarga los datos de profesores y materias desde el repositorio de GitHub en formato JSON.
    """
    # OJO: Para leer un archivo de GitHub desde Python, necesitas la URL "Raw" (cruda) del archivo JSON.
    # Ve al repositorio de FernandoSapient, abre el archivo JSON y dale clic al botón "Raw". Copia ese link.
    url_profesores = "LA_URL_RAW_DEL_JSON_AQUI" 
    
    try:
        print("Conectando con la API de GitHub...")
        respuesta = requests.get(url_profesores)
        
        # Esto verifica que la descarga fue exitosa (código 200)
        respuesta.raise_for_status() 
        
        # Convertimos el texto descargado a un diccionario de Python
        datos_json = respuesta.json()
        
        # Aquí harías un ciclo 'for' para recorrer datos_json 
        # y crear tus objetos Profesor y Materia, igual que con el CSV.
        # for item in datos_json:
        #      nuevo_profesor = Profesor(item['nombre'], item['cedula']...)
        #      profesores.append(nuevo_profesor)
        
        print("¡Datos descargados y cargados con éxito!")
        
    except requests.exceptions.RequestException as e:
        # ¡Puntos de validación! Si no hay internet o la URL está mal, el programa no explota.
        print(f"Error de conexión: No se pudieron descargar los datos. Revise su internet o la URL.\nDetalle: {e}")
    except json.JSONDecodeError:
        print("Error: El archivo descargado no tiene un formato JSON válido.")