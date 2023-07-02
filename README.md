HI :)
The code for the following assginment resides in the master branch,

2. Create an ARM (Azure Resource Manager) template for storage account and create 2 storage accounts
3. Create an ARM template for a Windows or Linux server
4. Create a tool to deploy the Storage accounts and the server in a continuous manner. Any type of CD (Continues deployment) pipe can be used here, preferred is an Azure DevOps pipe (In order to bypass permissions, set your personal computer as Azure DevOps agent)
5. Write a script that will create, upload, and copy 100 blobs from Storage account A to B, execute it on the server you created earlier using CD pipeline.
6. Choose metrics to monitor that small system of 1 server and 2 storage accounts   and create dashboard via "Monitor" to show that

the templates for storage account: **azuredeploy.json** and its parameters **azuredeploy.parameters.json**
template for sever: **servertemp.json**
**deployment** of storage accounts and server: **cideps.yaml**
the container whas created manually through the azure portal (could have done it while creating the data to be upoladed to it)
code that create, upload, and copy 100 blobs from Storage account A to B: **task5.py**
the code that connects to the server and runs the code on it: **fullt5.py**, connecting to the vm using the winrm library in python.
    I configured the server and my machine to listen on the ports 5985 and 5986
    added an NSG for each of the ports and **created ssl certificates** to fix the **ssl:wrong_version_number** error,But i keep getting the **ssl:certificate_verify_failed due to it being self signed**

Thank you.
