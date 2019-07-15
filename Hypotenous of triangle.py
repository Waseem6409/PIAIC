while True:
        import math
        while True:
                    try:
                        ab = float(input('\nEnter A to B distance of triangle:'))
                        bc = float(input('\nEnter B to C distance of triangle:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        ac=sqrt(ab**2 + bc**2)
        print("\nHypotenuse of the triangle is %d"%ac)
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

