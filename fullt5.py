import winrm

# Azure VM details
vm_name = 'myWinVm'  
username = 'smahaAdmin'  
password = 'smahaAdmin123'  

# Read the Python code from the file
with open('task5.py', 'r') as file:
    python_code = file.read()

# WinRM connection settings
winrm_url = f'https://mywinvm.eastus.cloudapp.azure.com:5986'
# Create a WinRM session
session = winrm.Session(winrm_url, auth=(username, password), transport='ntlm')

# Execute Python code on the VM
session.run_cmd('python', ['-c', python_code])