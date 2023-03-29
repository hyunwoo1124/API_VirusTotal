import requests

url = "https://www.virustotal.com/api/v3/urls/u-ace452550c1adce3f4dd4f779fceae17e38b930098b1567c785a89de706b89a0-1675750410"

headers = {
    "accept": "application/json",
    "x-apikey": "YOUR KEY"
}

response = requests.get(url, headers=headers)

print(response.text)