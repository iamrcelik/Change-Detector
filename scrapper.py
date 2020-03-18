import requests
import time
from bs4 import BeautifulSoup
import schedule


def timeScrapper():
    while True:
        page = requests.get("https://www.hepsiburada.com/samsung-250gb-t3-tasinabilir-ssd-disk-mu-pt250b-ww-p-BD805290?magaza=Gsmavm&wt_gl=cpc.elk.bilgisayar-diger.pla&gclid=Cj0KEQjwk-jGBRCbxoPLld_bp-IBEiQAgJaftZN5_sodk8_F_1iCg52BObnRKxiju21x3HygiZESSmkaAts78P8HAQ")
        # Fetch webpage
        soup = BeautifulSoup(page.content, "html.parser")

        # Scraping Data
        name = soup.find("h1", {"class": "product-name best-price-trick"}).text.replace("\n", "").strip()
        return name


def telegram_bot_sendtext(bot_message):
    bot_token = '639130642:AAHe0FdnfvIucWl8xmj6XDiKjPG9swlqQiE'
    bot_chatID = '988926794'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

def getFirstName(first_name):
    name = first_name
    return name

def report(name):

    if x == name:
        print("no change")
    else:
        my_message = "Price change detected {}".format(name)
        telegram_bot_sendtext(my_message)


b = timeScrapper()
x = getFirstName(b)

while True:
    a = timeScrapper()
    report(a)
    time.sleep(5)