import requests
import json
import base64


if __name__ == '__main__':
    r = requests.get('http://127.0.0.1:5000/get/1.2.0')
    json_data = r.json()
    with open('output.png', 'wb') as f:
        f.write(base64.b64decode(json_data['b64_data']))
