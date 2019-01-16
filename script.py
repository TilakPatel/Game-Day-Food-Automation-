from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pizzapi.pizzapi import *
import datetime
import time
# now = datetime.datetime.now()
# WINDOW_SIZE = "1920,1080"

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.add_argument('log-level=3')
# # driver = webdriver.Chrome()
# driver = webdriver.Chrome(chrome_options=chrome_options)
# dayLastOrdered = ''
# while True:

#     driver.get("https://www.nba.com/celtics/schedule")
#     while True:
#         day = now.strftime("%d")
#         if (int(day) < 10):
#             day = day.replace("0", "")
#         currentDate = now.strftime("%b ") + day
#         if (currentDate != dayLastOrdered):
#             try:
#                 tvProvs = driver.find_element_by_css_selector(
#                     "div[data-shortdate='" + currentDate + "'").get_attribute('data-tv')
#                 pizzaShouldBeOrdered = (("ESPN" in tvProvs) or (
#                     "ABC" in tvProvs) or ("TNT" in tvProvs))
#                 if (pizzaShouldBeOrdered):
#                     customer = Customer('Donald', 'Trump',
#                                         'donald@whitehouse.gov', '2024561111')
#                     address = Address('700 Pennsylvania Avenue NW', 'Washington', 'DC', '20408')
#                     store = address.closest_store()
#                     menu = store.get_menu()
#                     menu.search(Name='Coke')
#                 else:
#                     print('neet')
#             except:
#                 print('No game today.')
#         time.sleep(120)  # repeats every two minutes
#     # refresh calendar data every 1 hour just in case games switch up
#     time.sleep(3600)


# # driver.close()
customer = Customer('Donald', 'Trump',
                    'donald@whitehouse.gov', '2024561111')
address = Address('700 Pennsylvania Avenue NW', 'Washington', 'DC', '20408')
store = address.closest_store()
menu = store.get_menu()
menu.search(Name='Coke')
print(customer)