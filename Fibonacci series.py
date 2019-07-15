while True:
            while True:
                        try:
                            last_number = int(input('\nEnter last number :'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            x,y=0,1
            z=[]
            while y<last_number:
                z.append(y)
                x,y=y,x+y
            a=str(z)[1:-1]
            print(f'''\nThe Fibonacci series of number "{last_number}" is {a}.''')
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