year = int(input("Enter a year :- "))
isleapyear = False
if(year % 4 == 0):
    if(year % 100 ==0):
        if( year % 400 ==0):
            isleapyear=True
        else:
            isleapyear = False
    else:
        isleapyear=True
else:
    isleapyear= False

if(isleapyear):
    print("This is leap year  ",year)
else:
    print("This is not a leap Year", year)

