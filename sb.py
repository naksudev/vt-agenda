from seleniumbase import Driver
from time import sleep
import datetime

def openAgenda():
    # Configuration of SB Driver
    sb = Driver(headless=True)
    sb.set_window_size(1760, 845)

    # Login process
    sb.open("https://edt.univ-evry.fr/index.php")
    sleep(1.5)
    sb.type("input[name='loginstudent']", "lpisvd_11")
    sb.click("input[name='cookieetudiant']")
    sb.click("input[type='submit']")
    
    # User input 
    currentdate = datetime.date.today()
    year,week,weekday = currentdate.isocalendar()

    while True:
        print(f"[i] Semaine actuelle: {week}")
        week = int(input(">> Entrez la semaine voulu: "))
        
        if not week:
            print("[X] La semaine ne peut pas être vide.")
            continue

        try:
            week = int(week)

            if 1 <= week <= 52:
                break
            else:
                print(f"[X] L'année {year} contient 52 semaines uniquement")
        except ValueError:
            print("[X] Veuillez entrer un nombre valide en 1 et 52")

    url = f"https://edt.univ-evry.fr/index.php?current_year={year}&current_student=68425503&horiz=1&jour=0&current_week={week}"
    imgPath = f"output/{year}-{week}.png"

    # Screenshot and quit
    sb.open(url)
    sb.save_screenshot(imgPath)
    sb.quit()

    return imgPath 
