import requests
import json

from requests.models import HTTPBasicAuth

# url = "https://lsapi.seomoz.com/v2/url_metrics"

url = "https://lsapi.seomoz.com/v2/top_pages"



domains = [ 

    "ownthecart.com"

]

sent_json = {
    "target": "https://www.ownthecart.com/best-laptop-for-aerospace-engineering-students/",
    
    
}

r = requests.post(url, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}, json=sent_json, auth=HTTPBasicAuth('mozscape-1d42ca08d7','5535382ad1b3b149309098964a5ceee8'))


json_result = r.json()

print(json_result)

# print(json_result['results'][0]['page'])

# print(json_result['results'][0]['domain_authority'])


# print(r.text)








