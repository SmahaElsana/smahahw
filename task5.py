import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobType, PremiumPageBlobTier

connectionA_string = "DefaultEndpointsProtocol=https;AccountName=smahastorage11;AccountKey=UebeyWiIDXh2KARjsjYxgsM1UBsOOls19NvNDjmfvpJsnsOPJaJ7cP9Hba6ryeFFdj3hMSDvEoML+ASt6PeGbg==;EndpointSuffix=core.windows.net"
blob_service_clientA = BlobServiceClient.from_connection_string(connectionA_string)
containerA_name = "container1"
containerA_client = blob_service_clientA.get_container_client(containerA_name)

connectionB_string = "DefaultEndpointsProtocol=https;AccountName=smahastorage22;AccountKey=6VIaTToWgAccNHuOetzjg0v9JAUkMwrQk/YSyrkRnW1al8Y9TDhIgTVuteITdjlFAGW2GUNAwGtl+AStLmdPbg==;EndpointSuffix=core.windows.net"
blob_service_clientB = BlobServiceClient.from_connection_string(connectionB_string)
containerB_name = "container1"
containerB_client = blob_service_clientB.get_container_client(containerB_name)

for i in range(1, 101):

    blob_name = f"myfirstblob{i}.txt"
    data = "Hello, Azure Blob {i} Storage!"
    data_bytes = data.encode("utf-8")
    containerA_client.upload_blob(name=blob_name, data=data_bytes)


for blob in containerA_client.list_blobs():
    A_blob_client = containerA_client.get_blob_client(blob.name)
    B_blob_client = containerB_client.get_blob_client(blob.name)
    B_blob_client.start_copy_from_url(A_blob_client.url)