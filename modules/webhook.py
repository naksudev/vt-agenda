import requests
import json

def send(url, contentPayload):
    payload = {
        "username": "VT Agenda",
        "avatar_url": "https://edt.univ-evry.fr/vt_agenda.png",
        "content": f"{contentPayload}"
    }

    response = requests.post(url, data={'payload_json': json.dumps(payload)})

    if response.status_code == 200 or response.status_code == 204:
        print("\n[!] Webhook envoyé (sans attachements)")
    else:
        print(f"\n[X] Erreur webhook ({response.status_code})")
        print(response.content)

