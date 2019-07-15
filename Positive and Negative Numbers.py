while True:
        while True:
            try:
                num1=int(input("\nInput the number:"))
            except ValueError:
                print("Input can only be numbers,Please input a number")
            else:
                break
        if num1 > 0:
            print("\n")
            print(num1,"is a positive number")
        elif num1 < 0:
            print("\n")
            print(num1,"is a negative number")
        elif num1==0:
            print("\n")
            print(num1,"is zero")
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
                print("\nThank you for using")
                input()
                break


