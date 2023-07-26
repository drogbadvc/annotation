import requests

url = "https://www.machinools/api/annotation/scrape"

payload = {"text": "Cette recette inratable de tomates cerises maison est un must-have dans votre carnet de recettes. "}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
