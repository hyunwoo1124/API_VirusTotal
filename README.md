# VirusTotal API Project
Hello my name is Hyun Woo, a Cybersecurity professional. I wanted to create script where we can utilize API to check for malicious URLs and IPs based on available database from VirusTotal.

## Instructions
1. Clone the github repo
2. Go to VirusTotal and create a free account
3. Go to settings and request for your free API Key
4. Copy & paste your API key to virustotalapikey.py variable "APIKEY" and save.

Example
```bash
hyunwookim@Hyuns-MBP-2 apiStudy % python3 ./virustotalurlcheck.py 
Type in the url you want to check in VT: http://2domeinold.ru/
69c9e6afa0ad42f53df62d517c7afc4d14ef4640d8265b108a2aa7230aa9ded2
Category Counts: 
undetected: 15
harmless: 73
malicious: 2
[
  {
    "category": "malicious",
    "result": "malicious",
    "method": "blacklist",
    "engine_name": "Seclookup"
  },
  {
    "category": "malicious",
    "result": "malicious",
    "method": "blacklist",
    "engine_name": "Sucuri SiteCheck"
  }
]
```
## Future Updates
In the next iteration, I plan on adding a feature where you can import local files and check hashes. With enough features, I plan on implementing argparse to introduce menu.