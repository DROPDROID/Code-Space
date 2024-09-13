def fuel():

    while True:
        try:
            x,y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            result = round(x / y * 100)

            if result <= 1 and result >= 0:
                print("E")
            elif result >= 99 and result <= 100:
                print("F")
            elif result < 99 and result > 1:
                print(str(result) + "%")
            else:
                continue

            break
        
        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")

fuel()
