while True:
    try:
        U_input = input("Simpleshell> ")
        if U_input == "exit":
            break
        else:
            print("You have entered", U_input)
    except Exception as _:
        print("Unexpected input please try again")
