while True:
        while True:
            letter = input('\nEnter one letter:')
            letter1=letter.lower()
            if letter.isalpha():
                if len(letter) !=1:
                    print("\nPlease enter one letter only.")
                else:
                    break
            else:
                print("\nPlease enter letter A-Z only.")
        if letter1 in ['a','e','i','o','u']:
            print("\nThe",'''"'''+letter+'''"''',"is a vowel.")
        else:
            print("\nThe",'''"''',letter,'''"''',"is not a vowel.")
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