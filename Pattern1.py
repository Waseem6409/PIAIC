while True:
            while True:
                        try:
                            n = int(input('\nEnter number for pattern:'))
                        except ValueError:
                            print('''\n"Please enter only number"''')
                        else:
                            break
            for i in range(n):
                for j in range(i):
                    print('*',end="")
                print(' ')
            for i in range(n,0,-1):
                for j in range(i):
                    print('*',end="")
                print(' ')
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