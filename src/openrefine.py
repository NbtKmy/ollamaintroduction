#  This code is originally created by MichaelMarkert
# https://github.com/MichaelMarkert/SODa/blob/main/OR-LLM-Script.py


import json
import urllib2


Basisprompt = u"Generate a basic JSON containing only the following information on the person mentioned: dateofbirth, placeofbirth, dateofdeath, placeofdeath. Do not provide further information."

url = "http://localhost:11434/api/chat"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "messages": [
        {
            "content": Basisprompt,
            "role": "system"
        },
        {
            "content": value,
            "role": "user"
        }
    ],
    "model": "mistral:latest",
    "stream": False,
    "max_tokens": 2048,
    "temperature": 0.3,
    "top_p": 0.95
}

data_string = json.dumps(data, ensure_ascii=False)
data_bytes = data_string.encode('utf-8')

req = urllib2.Request(url, data=data_bytes, headers=headers)

response = urllib2.urlopen(req)
response_bytes = response.read()
response_json = json.loads(response_bytes.decode('utf-8'))
content = response_json["message"]["content"]

return content