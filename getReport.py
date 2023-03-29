import requests

url = "https://www.virustotal.com/api/v3/urls/u-ace452550c1adce3f4dd4f779fceae17e38b930098b1567c785a89de706b89a0-1675750410"

headers = {
    "accept": "application/json",
    "x-apikey": "0d5a952c81c23aa27f7ffbddef5895d989a80f3bb7053d371554652c0d92d979"
}

response = requests.get(url, headers=headers)

print(response.text)