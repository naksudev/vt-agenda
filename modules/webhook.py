import requests
import json

def send(url, imgPath):
    payload = {
        "username": "VT Agenda",
        "avatar_url": "https://edt.univ-evry.fr/vt_agenda.png",
        "content": "> [Accéder à VT](https://edt.univ-evry.fr/index.php) // `lpisvd_11`"
    }

    files = { 'file': (imgPath, _getImageData(imgPath)) }

    response = requests.post(url, data={'payload_json': json.dumps(payload)}, files=files)

    if response.status_code == 200:
        print("\n[!] Screenshot envoyé.")
    else:
        print(f"\n[X] Erreur webhook ({response.status_code})")
        print(response.content)

def _getImageData(imgPath):
    with open(imgPath, 'rb') as img:
        image_data = img.read()

    return image_data