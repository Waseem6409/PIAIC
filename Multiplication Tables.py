while True:
            while True:
                        try:
                            table_num = int(input('\nEnter table number:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            for y in range(1,11):
                z=table_num*y
                print (table_num,'x',y,'=',z)
            while True:
                        Repeat=input("\nDo you want to repeat?\n\nYes or No:")
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