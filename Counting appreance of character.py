while True:
            sentence = str(input('\nEnter any word or sentence:'))
            while True:
                        character=str(input("Of which single charcter count you want?:"))
                        character=character.lower()
                        if len(character) !=1:
                                print("\nPlease enter one letter only.")
                        else:
                                break
            c_character=(sentence.count(character))
            print("\nThe character",'"' + character + '"',"appeared",c_character,"times in given word or sentence.")
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