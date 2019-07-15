while True:
            while True:
                        try:
                            hexa = input('\nEnter hexadecimal number:')
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            decimal = str(int(hexa,16))
            print("\nThe decimal value of the given hexadecimal number is",decimal +'.')
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