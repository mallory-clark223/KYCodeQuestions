menu = ['Knickered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']

menu_prices = {}
price = .50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)

