import requests
import json 

def select_env():
    environments = {
        "main": "CHANGE_ME"
    }

    while True:
        print("[?] Sélectionnez l'environnement webhook")
        env_input = input("(main) >> ").lower()

        if env_input in environments:
            return environments[env_input]
        else:
            continue

def hook(url, contentPayload):    
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

def main():
    try:
        webhook_url = select_env()

        print("[?] Entrez l'ID étudiant (obtenable via l'URL)")
        studentID = int(input(">> "))

        print("[?] Entrez l'année voulue")
        yearInput = int(input(">> "))

        print("[?] Entrez la semaine voulue")
        weekInput = int(input(">> "))

        finalURL = f"https://edt.univ-evry.fr/vue_etudiant_horizontale.php?current_year={yearInput}&current_student={studentID}&current_week={weekInput}&lar=1920&hau=1080"
        hook(webhook_url, finalURL)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as e:
        print(f"Unexcepted error: {e}")
        raise

if __name__ == '__main__':
    main()
