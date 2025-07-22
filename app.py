from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    try:
        url = "http://169.254.169.254/metadata/identity/oauth2/token"
        params = {
            "api-version": "2019-08-01",
            "resource": "https://vault.azure.net"
        }
        headers = {"Metadata": "true"}
        r = requests.get(url, headers=headers, params=params, timeout=2)
        return r.text
    except Exception as e:
        return f"Error: {e}"
