from flask import Flask
import json
import base64

app = Flask(__name__)
available_versions = ["1.2.0", "1.1.0"]

@app.route('/')
def index():
    return "Welcome !<br/> 1. [/last_version/] Get last version<br /> 2. [/get/<version>] Get version."


@app.route('/last_version/')
def last_version():
    return json.dumps({"version":"1.2.0"})


@app.route('/get/<version>/')
def get_version(version):
    if version in available_versions:
        with open('data/bender.png', 'rb') as f:
            b64_data = base64.b64encode(f.read())
            return json.dumps({"file_name": "bender.png", "b64_data": b64_data})
    else:
        return json.dumps({"error": "Version %s does not exist !" % version})

if __name__ == '__main__':
    app.run()
