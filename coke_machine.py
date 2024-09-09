def coke_machine():

    coke = 50

    while coke > 0:
        print(f'Amount Due: {coke}')
        coins = int(input('Insert Coin: '))

        if coins in [25, 10, 5]:
           coke -= coins

        if coke == 0:
            print(f'Change Owed: {coke}')
        elif coke < 0:
            print(f'Change Owed: {abs(coke)}')



coke_machine()
