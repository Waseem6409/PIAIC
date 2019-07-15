while True:
            while True:
                            f_name = input('\nEnter first name:')
                            l_name = input('\nEnter last name:')
                            if f_name.isalpha() and l_name.isalpha():
                                break
                            else:
                                print("\nPlease enter correct name")
            full_name=f_name +' '+l_name
            r_full_name=full_name[::-1]
            print("\nYour name is",full_name+'.')
            print("\nYour name in reverse is",r_full_name+'.')
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