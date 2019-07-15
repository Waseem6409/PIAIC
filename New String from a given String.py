while True:
        user_string=input("\nPlease Type anything:")      
        new_string="Is" + user_string
        if user_string[:2] in ["Is","is"]:
            print('\n"' + user_string.title()+'"')
        else:
            print ('\n"' + new_string +'"')
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