# Autenticación en Azure
# version azure-storage-blob==12.17.0

from azure.storage.blob import BlobServiceClient
import os
 
connection_string = ""
container_name = ""
credential = ""

 
blob_service_client = BlobServiceClient(connection_string, credential=credential)      
 
def upload_blob_file(blob_service_client: BlobServiceClient, container_name: str, ruta_carpeta: str, nombre_archivo: str, nombre_blob: str):
 
    container_client = blob_service_client.get_container_client(container=container_name)
 
    with open(file=os.path.join(ruta_carpeta, nombre_archivo), mode="rb") as data:
        blob_client = container_client.upload_blob(name=nombre_blob, data=data, overwrite=True)
 
upload_blob_file(
    blob_service_client = blob_service_client,
    container_name = container_name,
    ruta_carpeta = r'',        # ruta ENTERA de la CARPETA del archivo que quieres subir, hasta la carpeta, sin el nombre de archivo 
    nombre_archivo = '',       # nombre y extension del archivo (ejemplo 'ejemplo.xlsx')
    nombre_blob = 'inputs/')   # nombre que quieres que el archivo tenga en la carpeta de nuebe donde va a quedar, si va en una subcarpeta se pone ahi. Por eso ya hay texto ahi.
                               # EL nombre puede ser el mismo que tenía en tu pc, escribelo despues del input
 
# upload_blob_file(
#     blob_service_client = blob_service_client,
#     container_name = container_name,
#     ruta_carpeta = r'',
#     nombre_archivo = '',
#     nombre_blob = '')