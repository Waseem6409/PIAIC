while True:
        while True:
                    try:
                        amount = float(input('\nEnter amount as of today:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        while True:
                    try:
                        interest = float(input('\nEnter interest amount of every year:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        while True:
                    try:
                        years = float(input('\nEnter years:'))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        interest_rate=(amount/100)*interest
        #amount_after_years=(interest_rate*years)+amount
        amount_after_years= amount*((1+(0.01*interest))** years)
        print("\nThe amount",amount,"after",years," years will be",str(amount_after_years))
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