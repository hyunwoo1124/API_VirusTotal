import requests
import json
from collections import Counter

from virustotalapikey import APIKEY

url = 'https://www.virustotal.com/api/v3/urls'

## Let's make the payload dynamic
domain = input("Type in the IP/url you want to check in VT: ")
payload = "url=" + domain

# header represent what the the server expects when we do a post request
headers = {
    "accept": "application/json",
    "x-apikey": APIKEY,
    "content-type": "application/x-www-form-urlencoded"
}
## after we post a request we get something back
response = requests.post(url, data=payload, headers=headers)

# jsonify the response
json_response = response.json()
# VT gives you the requestID after submission
analysis_id = json_response['data']['id']
# filter the encoding so only the requestID is saved
analysis_id_split = analysis_id.split('-')[1]
print(analysis_id_split)

#now that we have a URL requestID, let's GET a response back of the result
url_report = "https://www.virustotal.com/api/v3/urls/" + analysis_id_split

response_report = requests.get(url_report, headers=headers)

#print(response_report.text)

# jsonify the report
response_report = response_report.json()
# Since its jsonified go down the "Keys" and find the values we get from "last_analysis_results"
response_report_last_analysis_results = response_report['data']['attributes']['last_analysis_results']
# add indent of 2 so that the format is nice and pretty. At this point you get all the results from the vendors
response_pretty = json.dumps(response_report_last_analysis_results, indent=2)

differentCategory = []
for v in response_report['data']['attributes']['last_analysis_results'].values():
    differentCategory.append(v['category'])
# This dumps all categories found on the results above Ex. "harmless", "harmless", "harmless", "undetected"
#print(differentCategory)
#print(type(differentCategory))

# This prints how many undetected, harmless, and malicious we have using Counter
category_counts = dict(Counter(differentCategory))
print("Category Counts: ")
for category, count in category_counts.items():
    print(f"{category}: {count}")

attributes_list = []
# Values from "last_analysis_results" will ran to find if the value of the 'category' is 'malicious'
for attributes in response_report_last_analysis_results.values():
    if attributes['category'] == 'malicious':
        attributes_list.append(attributes)

attributes_pretty = json.dumps(attributes_list, indent=2)
print(attributes_pretty)
##print(response_pretty)

