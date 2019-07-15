while True:
        while True:
                    try:
                        num1 = int(input('\nEnter First number:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        while True:
                    try:
                        num2 = int(input('\nEnter Second number:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        sol=(num1+num2)*(num1+num2)
        print("\nThe Solution is {}.".format(sol))
        #print("\nThe Solution is",str(sol) + '.')
        #print(f"\nThe Solution is {sol}.")
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