while True:
        from math import pi
        while True:
                try:
                    radius = float(input('\nEnter the radius of sphere: '))
                except ValueError:
                    print("\nPlease enter only number")
                else:
                    break
        vol_of_sphere=((4.0/3.)*pi*(radius**3))
        print("\nThe Volume of the sphere is",vol_of_sphere)
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

