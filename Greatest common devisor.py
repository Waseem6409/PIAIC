while True:
            while True:
                        try:
                            a = float(input("\nPlease Enter the First Value:"))
                            b = float(input("\nPlease Enter the Second Value:"))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            i = 1
            while(i <= a and i <= b):
                if(a % i == 0 and b % i == 0):
                    gcd = i
                i = i + 1
                
            print("\nGCD of given integers {0} and {1} is {2}.".format(a, b, gcd))
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