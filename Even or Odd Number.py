while True:
        while True:
            try:
                num1 = int(input('\nEnter First number: '))
            except ValueError:
                print("\nPlease enter only number")
            else:
                break
        if num1 % 2 ==0:
            print('''\n"The number''',num1,'''is an even number"''')
        elif num1 % 2 != 0:
            print('''\n"The number''',num1,'''is an odd number"''')
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