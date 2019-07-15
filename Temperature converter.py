while True:
            while True:
                converter = str(input('''\nIn which unit you want to convert the temperature?\nInput "Celcius or C" or "Fahrenheit or F":'''))
                converter=converter.lower()
                if converter in ["celcius","c","fahrenheit","f"]:
                    break
                else:
                    print("\nPlease input correct unit.")
            while True:
                try:
                     temp = float(input('\nEnter the temperature:'))
                except ValueError:
                    print("\nPlease input correct temperature")
                else:
                    break
            if converter in ["celcius","c"]:
                temp=((temp - 32) * 5/9)
                u_converter="Celcius"      
            elif converter in ["fahrenheit","f"]:
                temp=((temp * 9/5) + 32)
                u_converter="Fahrenheit"
            # print("\nThe temperature in",u_converter,f"is {temp} degrees.")
            # print("\nThe temperature in",u_converter,"is %.2f degrees."% temp)
            print("\nThe temperature in",u_converter,"is %s degrees."% temp)            
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