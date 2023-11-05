from webhook import *
from sb import *

if __name__ == '__main__':
    # Select environement
    while True:
        print("[?] Sélectionnez l'environnement webhook")
        envInput = str(input("(dev) (prod) >> "))

        if envInput == "dev":
            url = "https://discord.com/api/webhooks/1170076204028678274/_gIwgnTt45boaik2q0hHn15EkyLyl-l0jIrtJw8y-oKUvihM5KSH65d9pUzXh3ifVDDY"
            break
        elif envInput == "prod":
            url = "https://discord.com/api/webhooks/1170093412343627796/gKBXnkcJkxYWq_JaTVLgsu5lsC579ZiN7nfqZtz3iLMYx7mEvJpG1F_4TLmtkC-pnEv4"
            break
        else:
            continue

    # Main script
    screenName = openAgenda()
    cropImg(screenName)
    sendWebhook(url, screenName)

