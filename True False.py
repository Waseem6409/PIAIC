while True:
            while True:
                        try:
                            num1 = int(input('\nEnter First number: '))
                            num2 = int(input('\nEnter Second number: '))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            if num2==num1 or abs(num2-num1)==5 or num2+num1==5:
                        print('\n"', True ,'"',sep="")
            else:
                        print('\n"', False ,'"',sep="")
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