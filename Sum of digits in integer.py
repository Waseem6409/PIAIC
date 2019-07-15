while True:
            while True:
                        try:
                            num1 = int(input('\nInput integer:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            sum=0
            while num1>0:
                        l_dig=num1%10
                        sum +=l_dig
                        num1=num1//10
            print("\nThe sum of digits of given integer is",sum)
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