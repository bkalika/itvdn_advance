import requests

url = "https://my.volia.com/v1/mobile/login"


payload = "Request body"
headers = {
    'Content-Type': 'application/json',
    'X-MB-DEVICE-KEY': '4287f769e9a626ada334ec0e39eed45a182e4254a4eead098ce582df5bdeab23',
    'X-AGREEMENT-KEY': '5121357',
    'X-CREDENTIALS-KEY': '11111',
    'OS-NAME': 'MobIOS',
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.headers)
