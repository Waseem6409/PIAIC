while True:
            while True:
                        try:
                            feet = float(input('\nEnter First number:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            inch=(feet*12)
            yard=(feet/3)
            mile=(feet/5280)
            print(f"\nYour height {feet} foot is {inch:.2f} inch.")
            print(f"\nYour height {feet} foot is {yard:.2f} yard.")
            print(f"\nYour height {feet} foot is {mile:.2f} mile.")
            
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