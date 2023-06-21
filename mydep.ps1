$resourceGroupName = "mysmaha"
$templateFile = "C:\Users\smaha\azure\azuredeploy.json"
$templateParameterFile = "C:\Users\smaha\azure\azuredeploy.parameters.json"

New-AzResourceGroup -Name $resourceGroupName -Location eastus -Force
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroupName -TemplateFile $templateFile -TemplateParameterFile $templateParameterFile
