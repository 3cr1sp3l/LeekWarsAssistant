import requests
import time

language = "fr"

# API URL
url = "https://leekwars.com/api/"

# Endpoints
getAllFunction = "function/get-all"
getEncyclopedia = "encyclopedia/get/" + language + "/"


# Get all functions
allFunctions = requests.get(url + getAllFunction)

if allFunctions.status_code == 200:
    allFunctionsData = allFunctions.json()
else:
    print(f"Erreur: {allFunctions.status_code}")

missingFunctions = 0
# Get functions encyclopedia page
for function in allFunctionsData["functions"]:
    functionEncyclopediaPage = requests.get(url + getEncyclopedia + function['name'])

    if functionEncyclopediaPage.status_code == 200:
        functionEncyclopediaPageData = functionEncyclopediaPage.json()
        with open(f"encyclopedia/{functionEncyclopediaPageData['title']}.md", 'w', encoding='utf-8') as file:
            file.write(functionEncyclopediaPageData['content'])
    else:
        missingFunctions += 1
        print(f"Erreur: {functionEncyclopediaPage.status_code} " + function['name'])
    
    # To avoid "too many requests"
    time.sleep(0.1)

print(f"Missing functions: {missingFunctions}")