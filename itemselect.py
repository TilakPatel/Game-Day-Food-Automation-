from pizzapi import address, store, menu, Address
import config as credentials


print('Make sure that you have set up your config file correctly!')
while True:
    address = Address(credentials.credentials['addressLine'], credentials.credentials['city'],
                      credentials.credentials['state'], credentials.credentials['zip'])
    store = address.closest_store()
    menu = store.get_menu()
    query = input("Enter a search term to find item codes(capitalize first letter): ")
    menu.search(Name=query)
