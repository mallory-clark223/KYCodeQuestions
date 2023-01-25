slang = ['Knackered', 'Pip pip', 'Squidgy', 'Smashing']

menu = []

for word in slang:
    menu.append(word + ' Spam')

print(menu)

## menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']

menu_prices = {}
price = .50

for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)

## Result: {'Knackered Spam': 0.5, 'Pip pip Spam': 1.5, 'Squidgy Spam': 2.5, 'Smashing Spam': 3.5}

for name, price in menu_prices.items():
    print(name, ': $', price)

## Result:
##          Knackered Spam : $ 0.5
##          Pip pip Spam : $ 1.5
##          Squidgy Spam : $ 2.5
##          Smashing Spam : $ 3.5

for name, price in menu_prices.items():
    print(name, ': $', price, sep='')

## Result:
##          Knackered Spam: $0.5
##          Pip pip Spam: $1.5
##          Squidgy Spam: $2.5
##          Smashing Spam: $3.5

for name, price in menu_prices.items():
    print(name, ': $', format(price, '.2f'), sep='')

                    ##  .2 = 2 decimal places % f = float

## Result:                                                  

##          Knackered Spam: $0.50
##          Pip pip Spam: $1.50
##          Squidgy Spam: $2.50
##          Smashing Spam: $3.50

