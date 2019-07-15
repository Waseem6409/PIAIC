while True:
            while True:
                        try:
                            n = int(input('\nEnter First number:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            sum_num = (n * (n + 1)) / 2
            print("The sum of numbers is",str(sum_num,+"."))
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