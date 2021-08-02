import requests
import json

# MAKE AN API CALL AND STORE THE RESPONSE
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r= requests.get(url)
print(f"Status code: {r.status_code}")

# EXPLORE THE STRUCTURE OF THE DATA
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)