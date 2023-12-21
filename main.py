from modules import webhook

def select_env():
    environments = {
        "dev": "https://discord.com/api/webhooks/1170076204028678274/_gIwgnTt45boaik2q0hHn15EkyLyl-l0jIrtJw8y-oKUvihM5KSH65d9pUzXh3ifVDDY",
        "prod": "https://discord.com/api/webhooks/1170093412343627796/gKBXnkcJkxYWq_JaTVLgsu5lsC579ZiN7nfqZtz3iLMYx7mEvJpG1F_4TLmtkC-pnEv4"
    }

    while True:
        print("[?] Sélectionnez l'environnement webhook")
        env_input = input("(dev) (prod) >> ").lower()

        if env_input in environments:
            return environments[env_input]
        else:
            continue

def main():
    try:
        webhook_url = select_env()

        print("[?] Entrez l'année voulue")
        yearInput = int(input(">> "))

        print("[?] Entrez la semaine voulue")
        weekInput = int(input(">> "))

        finalURL = f"https://edt.univ-evry.fr/vue_etudiant_horizontale.php?current_year={yearInput}&current_student=68425503&current_week={weekInput}&lar=1920&hau=1080"
        webhook.send(webhook_url, finalURL)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as e:
        print(f"Unexcepted error: {e}")
        raise

if __name__ == '__main__':
    main()
