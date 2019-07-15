while True:
        text = str(input('\nEnter any text:'))
        text=text.lower()
        vowel=0
        conson=0
        for i in text:
            if i in ('a','e','i','o','u'):
                vowel=vowel+1
            else:
                conson=conson+1
        print('''\nIn the given text the count of vowels is "{0}" and the count of consonants is "{1}".'''.format(vowel,conson))
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