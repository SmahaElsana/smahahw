$rg = 'smaha-hw'
$TemplateFile = 'C:\Users\smaha\azure\azuredeploy.json' 
$parameterFile = 'C:\Users\smaha\azure\azuredeploy.parameters.json'

New-AzResourceGroup -Name $rg -Location eastus -Force

New-AzResourceGroupDeployment 
-ResourceGroupName $rg 
-TemplateFile $templateFile 
-TemplateParameterFile $parameterFile


New-AzResourceGroupDeployment -ResourceGroupName smaha-hw -TemplateFile C:\Users\smaha\azure\azuredeploy.json