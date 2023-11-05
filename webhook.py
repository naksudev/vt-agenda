import requests
import json
import base64

def sendWebhook(url):
    webhook_url = url

    payload = {
        "wait": True,
        "username": "VT Agenda",
        "avatar_url": "https://edt.univ-evry.fr/vt_agenda.png",
    }

    with open("screenshot.png", 'rb') as img:
        image_data = img.read()

    files = {
        'file': ('screenshot.png', image_data)
    }

    response = requests.post(webhook_url, data={'payload_json': json.dumps(payload)}, files=files)

    if response.status_code == 200:
        print("[!] Screenshot envoyé dans le channel #edt-screenshot")
    else:
        print(response.status_code)
        print(response.content)

