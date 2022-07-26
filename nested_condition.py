age = int(input("Type Your Age"))

if age >= 18 :
    nid_card = input("Do yo Have Nid'Card : (y/n)")
    if nid_card == 'y':
        Mark_sheet = input("Do You Have Mark-Sheet : (y/n)")
        if Mark_sheet == "y" :
            print("Congratulation You've Selected")
        else:
            print("Mark-Sheet Must Be REquired")
    else:
        print("Nid'Card Must Be Required")
else:
    print("You Are Little Boy")