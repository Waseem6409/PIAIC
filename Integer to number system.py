while True:
            while True:
                        try:
                            value = int(input('\nEnter any integer value:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            print("\nThe integer value in binary is",bin(value) + '.'"\nThe integer value in octal is",oct(value) + '.'"\nThe integer value in hexadecimal is",hex(value)+'.')
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