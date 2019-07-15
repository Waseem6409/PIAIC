while True:
            while True:
                        try:
                            feet = float(input('\nEnter your height in foot unit:'))
                            weight = float(input('\nEnter your weight:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            meter=feet/3.281
            bmi=round(weight/(meter**2),2)
            print("\nYour body mass index is",str(bmi)+".")
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