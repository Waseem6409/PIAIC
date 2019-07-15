from datetime import date
while True:
        while True:
                    try:
                        print("\nInsert appropriate values for first date.")
                        year1 = int(input("\nEnter a year:"))
                        month1 = int(input("Enter a month:"))
                        day1 = int(input("Enter a day:"))
                    except ValueError:
                        print("\nPlease enter only number")
                    else:
                        break
        while True:
                    try:
                        print("\nInsert appropriate values for second date.")
                        year2 = int(input("\nEnter  year:"))
                        month2 = int(input("Enter  month:"))
                        day2 = int(input("Enter  day:"))
                    except ValueError:
                        print("\nPlease enter only number:")
                    else:
                        break
        date1 =date(year1,month1,day1)
        date2 =date(year2,month2,day2)
        num_of_days=(date2 - date1)
        print("\nThe days between the given dates is/are",abs(num_of_days.days),'.')
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
