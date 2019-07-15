while True:       
        user_string=input('''Please Type anything:''')
        while True:
            try:
                num1 = int(input("\nEnter number(s) for copies:"))
            except ValueError:
                print('''"\nPlease enter only number"''')
                # can also use "num1=abs(num1)"
            else:
                if num1 < 0 :
                    print('''\n"Please enter positive number(s) only"''')
                else:
                    break
        new_string=user_string * num1
        print(new_string)
        while True:
            Repeat=input("\nDo you want to repeat?\n\nYes or No:")
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