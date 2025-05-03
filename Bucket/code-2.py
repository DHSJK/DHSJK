import base64
import requests
import json
from google.cloud import storage
from google.api_core.exceptions import GoogleAPIError

def fetch_and_store_data(event, context):
    # Lista de recorridos
    recorridos = ["101", "102", "103", "104", "105"]
    
    bucket_name = 'proyecto-duoc-e3-transporte-real-time'
    
    # Inicializar el cliente de Cloud Storage
    storage_client = storage.Client()
    print("Cliente de Cloud Storage inicializado.")
    
    for recorrido in recorridos:
        api_url = f"https://www.red.cl/restservice_v2/rest/conocerecorrido?codsint={recorrido}"
        file_name = f'datos_conocerecorrido_{recorrido}.json'
        
        try:
            # Realizar la solicitud GET a la API
            response = requests.get(api_url)
            response.raise_for_status()  # Lanza un error para códigos de estado HTTP 4xx/5xx
            print(f"Datos obtenidos de la API para el recorrido {recorrido}.")
            
            # Obtener los datos de la respuesta en formato JSON
            data = response.json()
            data_str = json.dumps(data, indent=2)
            print(f"Datos JSON formateados para el recorrido {recorrido}.")
            
            # Obtener el bucket de Cloud Storage
            bucket = storage_client.bucket(bucket_name)
            print(f"Bucket {bucket_name} obtenido.")
            
            # Crear un objeto blob en el bucket y cargar los datos
            blob = bucket.blob(file_name)
            blob.upload_from_string(data_str, content_type='application/json')
            print(f"Archivo {file_name} cargado exitosamente en el bucket.")
        
        except requests.RequestException as e:
            print(f"Error al realizar la solicitud a la API para el recorrido {recorrido}: {e}")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar la respuesta JSON para el recorrido {recorrido}: {e}")
        except GoogleAPIError as e:
            print(f"Error con Google Cloud Storage para el recorrido {recorrido}: {e}")
        except Exception as e:
            print(f"Error inesperado para el recorrido {recorrido}: {e}")
    
    return "Proceso completado para todos los recorridos."

# Este es el manejador de eventos que Google Cloud Functions invocará
def pubsub_trigger(event, context):
    # El mensaje Pub/Sub está en base64, así que se debe decodificar
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(f"Mensaje recibido: {pubsub_message}")
    
    # Llamar a la función principal con el evento
    fetch_and_store_data(event, context)
