while True:
    from math import pi
    while True:
                                try:
                                    r=float(input("Please insert the radius of circle:"))
                                except ValueError:
                                    print("Please enter only number")
                                else:
                                    break
    a=(pi)*(r)**2
    print("The area of triangel=",a)
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


