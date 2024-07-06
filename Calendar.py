# print("THIS PROGRAM IS BUILT BY DHAIRYA TAAK AS ASSIGNMENT 3 FOR THE COURSE PROG12853. IT ASKS THE USER FOR A YEAR AND DISPLAYS THE CALENDAR. I FINISHED THIS ASSIGNMENT ON 21 MARCH 2024")
# user_year_input=int(input("PLEASE ENTER A YEAR BETWEEN 1970 AND 2030\t:\t"))
# if user_year_input%4==0 and user_year_input%100!=0:
#     type_year=True
# else:
#     type_year=False

# if user_year_input<1970 or user_year_input>2030:
#     while True:
#         user_year_input=int(input("PLEASE ENTER A VALID VALUE \n YEAR SHOULD BE BETWEEN 1970 AND 2030\t:\t"))
#         if user_year_input>1970 or user_year_input<2030:
#             break
# if user_year_input%4==0 and user_year_input%100!=0:
#     type_year=True
# else:
#     type_year=False
# NAME= DHAIRYA TAAK
# COURSE = COMPUTER PROGRAMMING
# PLEASE IGNORE ABOVE CODE IT WAS USED FOR TESTING

type_year=False
# print("THIS PROGRAM IS BUILT BY DHAIRYA TAAK AS ASSIGNMENT 3 FOR THE COURSE PROG12853. IT ASKS THE USER FOR A YEAR AND DISPLAYS THE CALENDAR. I FINISHED THIS ASSIGNMENT ON 21 MARCH 2024")
def firstfunction(year):
    # this function determines the offset
    years_difference=year-1970
    no_leap_years=years_difference//4
    years_difference_in_days=(years_difference*365)+no_leap_years
    offset=(years_difference_in_days-3)%7
    return offset
    # this function returns offset as 
# 0 sunday
# 1 monday
# 2 tuesday
# 3 wednesday
# 4 thursday
# 5 friday
# 6 saturday
# print(firstfunction(user_year_input))
def secondfunction(month_n,offset,type_year):
    # print(type_year)
    if month_n==1:
        month_offset=offset
    if month_n==2:
        month_offset=(31+offset)%7
    if month_n==3  and type_year:
        month_offset=(31+29+offset)%7
    if month_n==3  and  not type_year:
        month_offset=(31+28+offset)%7
    if month_n==4 and type_year:
        month_offset=(31+29+31+offset)%7
    if month_n==5 and type_year:
        month_offset=(31+29+31+30+offset)%7
    if month_n==6 and type_year:
        month_offset=(31+29+31+30+31+offset)%7
    if month_n==7 and type_year:
        month_offset=(31+29+31+30+31+30+offset)%7
    if month_n==8 and type_year:
        month_offset=(31+29+31+30+31+30+31+offset)%7
    if month_n==9 and type_year:
        month_offset=(31+29+31+30+31+30+31+31+offset)%7
    if month_n==10 and type_year:
        month_offset=(31+29+31+30+31+30+31+31+30+offset)%7
    if month_n==11 and type_year:
        month_offset=(31+29+31+30+31+30+31+31+30+31+offset)%7
    if month_n==12 and type_year:
        month_offset=(31+29+31+30+31+30+31+31+30+31+30+offset)%7
    if month_n==4 and  not type_year:
        month_offset=(31+28+31+offset)%7
    if month_n==5 and  not type_year:
        month_offset=(31+28+31+30+offset)%7
    if month_n==6 and  not type_year:
        month_offset=(31+28+31+30+31+offset)%7
    if month_n==7 and  not type_year:
        month_offset=(31+28+31+30+31+30+offset)%7
    if month_n==8 and  not type_year:
        month_offset=(31+28+31+30+31+30+31+offset)%7
    if month_n==9 and  not type_year:
        month_offset=(31+28+31+30+31+30+31+31+offset)%7
    if month_n==10 and  not type_year:
        month_offset=(31+28+31+30+31+30+31+31+30+offset)%7
    if month_n==11 and  not type_year:
        month_offset=(31+28+31+30+31+30+31+31+30+31+offset)%7
    if month_n==12 and  not type_year:
        month_offset=(31+28+31+30+31+30+31+31+30+31+30+offset)%7
    return month_offset
def thirdFunction(month_number, offset_ofthe_month,type_year):
    # Days in each month
    if type_year==True:
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Month names
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    print(month_names[month_number-1],"\n")
    print("{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}".format("Sun","Mon","Tue","Wed","Thu","Fri","Sat"))
    spaces=6*offset_ofthe_month
    print(" " * spaces, end="")
    for i in range(1, days_in_month[month_number - 1] + 1):
        print("{:5}".format(i), end=" ")
        offset_ofthe_month += 1
        if offset_ofthe_month % 7 == 0:
            print("\n")  # Move to the next line after Saturday
    print()  
def fourthfunction():
    while True:
        user_year_input = (input("PLEASE ENTER A YEAR BETWEEN 1970 AND 2030\t(OR ENTER 0 TO EXIT)\t:\t"))
        try:
            user_year_input=int(user_year_input)
        except Exception:
            print("Please enter valid value as year can be only an integer not nay other type")
        if user_year_input%4==0 and user_year_input%100!=0:
            yeart_type= True  
        else:
            yeart_type= False  
        if user_year_input == 0:
            print("THANKS FOR USING THIS PROGRAM")
            return None
        if user_year_input >= 1970 and user_year_input <= 2030:
            return user_year_input,yeart_type
        print("PLEASE ENTER A VALID YEAR BETWEEN 1970 AND 2030.\n\n")

   
def main():
    
        while True:
            try:
                data=fourthfunction()
                if data is None:
                    break
                year=data[0]
                type_year=data[1]
                listmonth=[]
                # print(type_year)
                # print(year)
                year_offset=firstfunction(year)
                for i in range(1,13):
                    listmonth.append(secondfunction(i,year_offset,type_year))
                for i in range(1,13):
                    thirdFunction(i,listmonth[(i-1)],type_year)
            except Exception as e :
                print(e)
if __name__=="__main__":    
    main()
