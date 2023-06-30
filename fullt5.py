import winrm

# Azure VM details
vm_name = 'myWinVm'  # Replace with the name of your Azure VM
username = 'smahaAdmin'  # Replace with the username for the WinRM connection
password = 'smahaAdmin123'  # Replace with the password for the WinRM connection

# Python code to execute on the VM
python_code = '''
print("Hello, Azure VM!")
'''

# WinRM connection settings
winrm_url = f'https://{vm_name}.eastus.cloudapp.azure.com:5986'  # Replace <azure_region> with your VM's region

# Create a WinRM session
session = winrm.Session(winrm_url, auth=(username, password), transport='ntlm')

# Execute Python code on the VM
result = session.run_cmd('python', ['-c', python_code])

# Print the output of the Python code
print(result.std_out.decode())

# Disconnect from the VM
session.close()
