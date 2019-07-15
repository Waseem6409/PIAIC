while True:
            while True:
                        try:
                            num1 = int(input('\nEnter First number:'))
                        except ValueError:
                            print('''\n"Please enter only number"''')
                        else:
                            break
            if num1 > 1: 
                for i in range(2,num1): 
                    if (num1 % i) == 0: 
                        print(f'''\n"{num1}" is not a prime number.''') 
                        break
                else: 
                    print(f'''\n"{num1}" is a prime number.''') 
                
            else: 
                print(f'''\n"{num1}" is not a prime number.''') 
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