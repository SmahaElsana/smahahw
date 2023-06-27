import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobType, PremiumPageBlobTier

connection_string = "DefaultEndpointsProtocol=https;AccountName=smahastorage1111;AccountKey=amgY8vqarqsLxK8o27Jbu7CIptQpuKW3y0GEu/vQk8ptJn+fI3acxoEqmIiSZ0ljmbnnPmBrVACd+AStRpArxQ==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "container1"
container_client = blob_service_client.get_container_client(container_name)

blob_name = "myfirstblob1.txt"
data = "Hello, Azure Blob Storage!"
data_bytes = data.encode("utf-8")

container_client.upload_blob(name=blob_name, data=data_bytes)
