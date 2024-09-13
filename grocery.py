def grocery():

    list_of_items = {}

    while True:
        try:

            item = input("").upper()

            if item in list_of_items:
                list_of_items[item] += 1
            else:
                list_of_items[item] = 1

        except EOFError:
            print("\n")
            break


    for item, i in sorted(list_of_items.items()):
        print(f"{i} {item}")


grocery()