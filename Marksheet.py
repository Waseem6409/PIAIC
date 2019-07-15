from datetime import datetime
year=datetime.now().year
date=datetime.now().strftime("%d-%m-%Y")
while True:
            while True:
                        Name=input("\nType your name:")
                        if len(Name)==0:
                            print('''"You made mistake while filling name section"''')
                        else:
                            break
            while True:
                        F_Name=input("\nType father name:")
                        if len(F_Name)==0:
                            print('''"You made mistake while filling f.name section"''')
                        else:
                            break
            while True:
                        School=input("\nType your school name:")
                        if len(School)==0:
                            print('''"You made mistake while filling school section"''')
                        else:
                            break
            while True:
                        Group=input("\nType your group eg.Science,Arts:")
                        if len(Group)==0:
                            print('''"You made mistake while filling group section"''')
                        else:
                            break
            while True:
                        Board=input("\nType name of your board:")
                        if len(Board)==0:
                            print('''"You made mistake while filling board section"''')
                        else:
                            break
            while True:
                        try:
                            num1 = int(input('\nEnter number of total subjects:'))
                        except ValueError:
                            print('''\n"Please enter only number"''')
                        else:
                            break
            l_Subjects=[]
            l_T_Marks=[]
            l_Marks=[]
            S_numbers=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelth","thirteenth","fourteenth","fifteenth","sixteenth","eighteenth","nineteenth","twentieth"]
            for i in range(num1):
                    print(f'''\n"For the {S_numbers.pop(0)} subject"\n''')
                    Subjects=input("Type subject name:")
                    l_Subjects.append(Subjects)
                    while True:
                        try:
                            T_Marks= int(input(f'Enter total marks for {Subjects}:'))
                            l_T_Marks.append(T_Marks)
                            while True:
                                try:
                                    Marks = int(input('Enter obtained marks:'))
                                
                                except ValueError:
                                    print('''\n"Please enter only number"''')
                                if Marks>T_Marks:
                                    print('''\n"Please insert correct marks"''')
                                else:
                                        l_Marks.append(Marks)
                                        break
                        except ValueError:
                            print('''\n"Please enter only number"''')
                        else:
                            break
            print('''\n\n                              "Here is your Marksheet"\n\n''')
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(f"{'§': <80}§")
            print(f"{'§': <80}§")
            print(f"§                       {Board.title(): <56}§")
            print(f"{'§': <80}§") 
            print(f"{'§': <80}§")           
            print(f"§    Examination      Annual {year: <51}§")
            print(f"{'§': <80}§")
            print(f"§    Name             {Name.title(): <58}§")
            print(f"{'§': <80}§")
            print(f"§    F.Name           {F_Name.title(): <58}§")
            print(f"{'§': <80}§")
            print(f"§    School/Private   {School.title(): <58}§")
            print(f"{'§': <80}§")
            print(f"§    Group            {Group.title(): <58}§")
            print(f"{'§': <80}§")
            print("§   _________________________________________________________________________   §")
            print("§  |                                                                         |  §")
            print("§  |                               Subjects                                  |  §")
            print("§  |_________________________________________________________________________|  §")
            print("§  |            Component                |              Marks                |  §")
            print("§  |_____________________________________|___________________________________|  §")
            
            l_T_Marks1=list(l_T_Marks)
            l_Marks1=l_Marks.copy()
            l_Subjects1=l_Subjects.copy()

            for i in list(l_Marks):
                print(f"§  |            {(l_Subjects.pop(0)).title(): <22}   |            {l_Marks.pop(0):>4}/{l_T_Marks.pop(0): <18}|  §")
                print(f"§  |_____________________________________|___________________________________|  §")
            Sum_Marks=(sum(l_Marks1))
            Sum_T_Marks=(sum(l_T_Marks1))
            Percentage=(Sum_Marks/Sum_T_Marks)*100
            if(Percentage>=80):
                Grade='A+'
            elif(Percentage>=70 and Percentage<80):
                Grade='A'
            elif(Percentage>=60 and Percentage<70):
                Grade='B'
            elif(Percentage>=50 and Percentage<60):
                Grade='C'
            elif(Percentage>=40 and Percentage<50):
                Grade='D'
            else:
                Failed=('''"Sorry! You have failed the exam."                  §''')
                Grade='F'
            print(f"{'§': <80}§")
            print(f"{'§': <80}§")
            print(f"§                                Grand Total {Sum_Marks:>4} out of {Sum_T_Marks:<23}§")
            print(f"{'§': <80}§")
            print("§                                         _______                               §")
            print("§                                        |       |                              §")
            print(f"§                                Grade   |   {Grade.title(): <4}|                              §")
            print("§                                        |_______|                              §")
            if Grade=='F':
                print(f"{'§': <80}§")
                print(f"§                           {Failed: <5}")
            print(f"{'§': <80}§")
            print("§                                       Waseem Munir                            §")
            print("§                                _________________________                      §")
            print("§                                Controller of Examination                      §")
            print(f"{'§': <80}§")
            print(f"§ Dated:{date: <72}§")
            print(f"{'§': <80}§")
            print(f"{'§': <80}§")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            while True:
                        Repeat=input("\nDo you want to repeat?\n\nYes or No:")
                        Repeat=Repeat.lower()
                        if Repeat not in ["yes","y","no","n"]:
                            print('''"\nPlease select correct option"''')
                        else:
                            break
            if Repeat in ["yes","y"]:
                continue
            else:
                if Repeat in ["no","n"]:
                    print("\n-----Thank you for using-----")
                    input()
                    break