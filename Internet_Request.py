import requests
from winotify import Notification


def get_price():
    site_html = requests.get("https://www.emag.bg/smartfon-apple-iphone-13-256gb-5g-red-mlq93rm-a/pd/DSFCMXMBM/?").text

    split_html = site_html.split(';')

    for part in split_html:
        if 'EM.productFullPrice' in part:
            price = part.split()[2]
            return float(price)


price = get_price()
print(price)

if price < 1750:
    notifier = Notification(
        app_id="Price checker",
        title='iPhone price checker',
        msg='Buy the iPhone!',
        duration='short'
    )
    notifier.show()
