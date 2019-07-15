while True:
            a_string=input("\nType anything:")
            letters=0
            digits=0
            for b in a_string:
                if b.isdigit():
                    digits+=1
                elif b.isalpha:
                    letters+=1
            print('''\nIn the given input the number of letters is "{0}" and digits is "{1}".'''.format(letters,digits))
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