## PROJECT IDEA
We will create a web application that runs once a day, 
gets news form YLE, and makes a funny short extract of those articles.

## TODO:
0. Check if YLE already have API or RSS feed, which could be used.
1. Consider where the project will bw hosted (Azure, AWS, Google Cloud, etc.).
2. Conside how code should be executed.
3. Chose storage (SQL or NoSQL or both)
4. Check ot existing AI services. Preferably free or dirt cheap.
5. Select a hosting method/provider to display the results.
6. Conider YLE.LOL domain


## Installation procedure:

1. PowerShell 7 : https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4#msi


2. Azure CLI (in case deployment is done to Azure): 
Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi