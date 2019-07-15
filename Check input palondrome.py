while True:
            while True:
                        word = str(input('\nEnter First number:'))
                        word=word.lower()
                        if word.isalpha:
                            break
                        else:
                            print("\nPlease enter word only")
            r_word=word[::-1]
            if word == r_word:
                print("\nThe word",'"'+word.title()+'"',"is palindrome.")
            else:
                print("\nThe word",'"'+word.title()+'"',"is not palindrome.")
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