while True:
        while True:
            try:
                num1 = int(input('\nEnter a number: '))
            except ValueError:
                print("\nPlease enter only number")
            else:
                break
        diff=num1-17
        print("\nThe difference between the number",num1,"and 17 is",abs(diff))
        while True:
            Repeat=input("\nDo you want to calculate again?\n\nYes or No:")
            Repeat=Repeat.lower()
            if Repeat not in ["yes","y","no","n"]:
                print("\nPlease select correct option")
            else:
                break
            
                
        if Repeat in ["yes","y"]:
            continue
        else:
            if Repeat in ["no","n"]:
                print("\n-----Thank you for using-----")
                input()
                break

