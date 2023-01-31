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

                    ##  .2 = 2 decimal places & f = float

## Result:                                                  

##          Knackered Spam: $0.50
##          Pip pip Spam: $1.50
##          Squidgy Spam: $2.50
##          Smashing Spam: $3.50

## While Loops:

## for loops - allow you to loop a CERTAIN amount of times
## while loops - allow you to loop while a condition is TRUE

x = 1

while x != 3:
    print('x is', x)
    x = x + 1

## Result: 

##          x is 1
##          x is 2

## We want to let customers order and add as many menu items as they want.
orders = []
order = input("What would you like to order? (Q to Quit)")

while (order.upper() != 'Q'):
    # Find the order and add it to the list if it exists
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")
    

    # See if the customer wants to order anything else
    order = input("Anything else? (Q to Quit)")

print(orders)

###### Could not get the above code to work

###### Here's another method to break out of the loop:

## We want to let customers order and add as many menu items as they want.
orders = []
order = input("What would you like to order? (Q to Quit)")

while (True):
    if order == 'Smashing Spam':
        print("Sorry, we're all out!")
        continue
    if order.upper() == 'Q':
        break
    # Find the order and add it to the list if it exists
    found = menu.get(order)
    if found:
        orders.append(order)
    else:
        print("Menu item doesn't exist")
    

    # See if the customer wants to order anything else
    order = input("Anything else? (Q to Quit)")

print(orders)