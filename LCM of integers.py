while True:
            while True:
                        try:
                            num1 = int(input('\nEnter First number:'))
                            num2 = int(input('\nEnter Second number:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            if num1 > num2:
                greater = num1
            else:
                greater = num2
            while(True):
                if((greater % num1 == 0) and (greater % num2 == 0)):               
                    break
                greater += 1
            print("\nThe LCM of given integers {0} and {1} is {2}.".format(num1,num2,greater))
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