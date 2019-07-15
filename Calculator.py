while True:
                
                while True:
        
                            operation=input('\nSelect any operation:\n\n1.Add\n\n2.Subtract\n\n3.Multiply\n\n4.Divide\n\nSelect:')
                            operation=operation.lower()
                            if operation not in ["1","add","2","subtract","3","multiply","4","divide"]:
                                print("\nPlease enter the correct operator")
                            else:
                                break         
                while True:
                                try:
                                    num1 = int(input('\nEnter First number:'))
                                except ValueError:
                                    print("Please enter only number")
                                else:
                                    break
                while True:
                                try:
                                    num2 = int(input('\nEnter Second number: '))
                                except ValueError:
                                    print("Please enter only number")
                                else:
                                    break
                if operation == "add" or operation == '1' :
                    print('\n',num1,"+",num2,"=", (num1+num2))
                elif operation =="subtract" or operation == '2':
                    print("\n",num1,"-",num2,"=", (num1-num2))
                elif operation =="multiply" or operation == '3':
                    print('\n',num1,"*",num2,"=", (num1*num2))
                elif operation =="divide" or operation == '4':
                    print('\n',num1,"/",num2,"=", (num1/num2))
                        
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


