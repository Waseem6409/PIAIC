while True:
            while True:
                        try:
                            num = int(input('\nEnter number:'))
                        except ValueError: 
                            print("\nPlease enter only number")
                        o_num=num
                        num_rev = 0    
                        while num > 0:    
                            dig = num %10    
                            num_rev = (num_rev *10) + dig   
                            num = num //10
                        print("\nThe reverse of given number is {}.".format(num_rev))
                        f_num=o_num+num_rev                   
                        print("\nAfter adding the reverse number in given number,the sum is {}.".format(f_num))
                        f_num2=f_num
                        a_num_rev=0
                        while f_num > 0:    
                            dig = f_num % 10    
                            a_num_rev = (a_num_rev *10) + dig   
                            f_num = f_num //10
                        if f_num2==a_num_rev:
                            print('''\nThe number "{}"" is palindrome.'''.format(f_num2))
                            break
                        else:
                            print('''\nThe number "{}" is not palindrome.\n\n"Please try again"'''.format(f_num2))
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