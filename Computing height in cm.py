while True:
    while True:
                try:
                    height  = float(input('\nEnter your height in feet:'))
                except ValueError:
                    print("\nPlease enter only number")
                else:
                    break
    cm = height*30.48
    #cm = round(height*30.48,2)
    #print(f"\nYour height {height} foot is %.2f cm."  % cm)
    #print(f"\nYour height {height} foot is {cm:.2f} cm.")
    #print("\nYour height",height,"foot is {:.2f} cm.".format(cm))
    print("\nYour height",height,"foot is",round(cm,2),"cm.")
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