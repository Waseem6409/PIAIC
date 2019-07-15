while True:
            while True:
                        try:
                            n = int(input('\nEnter number for pattern:'))
                        except ValueError:
                            print('''\n"Please enter only number"''')
                        else:
                            break
            n=n+1
            for i in range(1,n):
                for j in range(1,i):
                    print(j,end="")
                print(' ')
            for i in range(n,0,-1):
                for j in range(1,i):
                    print(j,end="")
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