from seleniumbase import Driver 
from webhook import *
from time import sleep
import datetime

sb = Driver(headless=True)

# DEV ENV
webhook_url = "https://discord.com/api/webhooks/1170076204028678274/_gIwgnTt45boaik2q0hHn15EkyLyl-l0jIrtJw8y-oKUvihM5KSH65d9pUzXh3ifVDDY"

# LP DISCORD
#webhook_url = "https://discord.com/api/webhooks/1170093412343627796/gKBXnkcJkxYWq_JaTVLgsu5lsC579ZiN7nfqZtz3iLMYx7mEvJpG1F_4TLmtkC-pnEv4"

def openAgenda():
    currentdate = datetime.date.today()
    year,week,weekday = currentdate.isocalendar()

    sb.set_window_size(1760, 845)

    sb.open("https://edt.univ-evry.fr/index.php")
    sleep(1.5)
    sb.type("input[name='loginstudent']", "lpisvd_11")
    sb.click("input[name='cookieetudiant']")
    sleep(1)
    sb.click("input[type='submit']")
    
    while True:
        print(f"Semaine actuelle: {week}")
        week = int(input(">> Entrez la semaine voulu: "))
        
        if not week:
            print("La semaine ne peut pas être vide.")
            continue

        try:
            week = int(week)

            if 1 <= week <= 52:
                break
            else:
                print(f"L'année {year} contient 52 semaines uniquement")
        except ValueError:
            print("Veuillez entrer un nombre valide en 1 et 52")

    url = f"https://edt.univ-evry.fr/index.php?current_year={year}&current_student=68425503&horiz=1&jour=0&current_week={week}"

    sb.open(url)

    sb.save_screenshot("screenshot.png")
    sb.quit()

if __name__ == '__main__':
    openAgenda()
    sendWebhook(webhook_url)

