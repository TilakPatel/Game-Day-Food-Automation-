from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pizzapi import *
import config as credentials
import datetime
import time
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
dayLastOrdered = ''
while True:
    now = datetime.datetime.now()
    driver.get("https://www.nba.com/celtics/schedule")
    while True:
        day = now.strftime("%d")
        if (int(day) < 10):
            day = day.replace("0", "")
        currentDate = now.strftime("%b ") + day
        if (currentDate != dayLastOrdered):
            try:
                tvProvs = driver.find_element_by_css_selector(
                    "div[data-shortdate='" + currentDate + "'").get_attribute('data-tv')
                pizzaShouldBeOrdered = (("ESPN" in tvProvs) or (
                    "ABC" in tvProvs) or ("TNT" in tvProvs))
                timeOfGamehelper = driver.find_element_by_css_selector(
                    "div[data-shortdate='" + currentDate + "'").get_attribute('data-time')
                timeOfGame = (str(timeOfGamehelper)[:timeOfGamehelper.find(':')])
                print(timeOfGame)
                if (pizzaShouldBeOrdered):
                    customer = Customer(credentials.credentials['firstName'], credentials.credentials['lastName'],
                                        credentials.credentials['email'], credentials.credentials['phone'])
                    address = Address(credentials.credentials['addressLine'], credentials.credentials['city'],
                                      credentials.credentials['state'], credentials.credentials['zip'])
                    store = address.closest_store()
                    order = Order(store, customer, address)
                    for item in credentials.items:
                        order.add_item(item)
                    card = PaymentObject(
                        credentials.card['number'], credentials.card['expiration'], credentials.card['cvv'], credentials.card['zip'])
                    orderText = order.pay_with(card)
                    timeEstimate = (orderText['Order']['EstimatedWaitMinutes'])
                    minutesLeft = (str(timeEstimate)[timeEstimate.find('-') + 1:])
                    print('You paid $',
                          orderText['Order']['Amounts']['Payment'])
                    dayLastOrdered = currentDate
                    
                else:
                    print('no game today.')
            except:
                print('No game today.')
        time.sleep(10800)  # repeats every 3 hours
    # refresh calendar data every 1 hour just in case games switch up
    time.sleep(3600)

# driver.close()
# a = datetime.datetime.now().hour
# print(a) 
#only order if a is equal to gametime - 1