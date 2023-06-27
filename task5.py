# from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

connection_string = "DefaultEndpointsProtocol=https;AccountName=smahastorage1111;AccountKey=amgY8vqarqsLxK8o27Jbu7CIptQpuKW3y0GEu/vQk8ptJn+fI3acxoEqmIiSZ0ljmbnnPmBrVACd+AStRpArxQ==;EndpointSuffix=core.windows.net"


blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "container1"
container_client = blob_service_client.create_container(container_name)

blob_name = "myfirstblob"
data = "Hello, Azure Blob Storage!"

container_client.upload_blob(blob_name, data)

