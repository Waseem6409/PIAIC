while True:
                while True:
                                try:
                                    num1 = int(input('\nEnter a number: '))
                                except ValueError:
                                    print("Please enter only number")
                                else:
                                    break
                n1 = int( "%d" % num1)
                n2 = int( "%d%d" % (num1,num1) )
                n3 = int( "%d%d%d" % (num1,num1,num1))
                print(n1)
                print(n2)
                print(n3)
                print(n1,'+',n2,'+',n3,'=',(n1+n2+n3))
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


