while True:
            while True:
                        try:
                            amount = int(input('\nEnter amount:'))
                        except ValueError:
                            print("\nPlease enter only number")
                        else:
                            break
            n_1000=amount//1000
            amount=amount-(n_1000*1000)
            n_500=amount//500
            amount=amount-(n_500*500)
            n_100=amount//100
            amount=amount-(n_100*100)
            n_50=amount//50
            amount=amount-(n_50*50)
            n_20=amount//20
            amount=amount-(n_20*20)
            n_10=amount//10
            amount=amount-(n_10*10)
            l_amount=amount
            print('''\nThere are "{0}" 1000 notes,"{1}" 500 notes,"{2}" 100 notes,"{3}" 50 notes,"{4}" 20 notes,"{5}" 10 notes and "{6}" is left in given amount.'''.format(n_1000,n_500,n_100,n_50,n_20,n_10,l_amount))
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