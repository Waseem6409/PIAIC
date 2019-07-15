while True:
        import math
        while True:
                    try:
                        x1 = int(input("\nEnter value for x1:"))
                        y1 = int(input("\nEnter value for y1:"))
                        x2 = int(input("\nEnter value for x2:"))
                        y2 = int(input("\nEnter value for y2:"))
                    except ValueError:
                        print("\nPlease enter only number distance points")
                    else:
                        break
        d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
        print("\ndistance between the giver points is",d)
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
