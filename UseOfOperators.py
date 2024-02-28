# Enter two numbers and do the following arithmetic Operations find max and min.
# i) a+b*c ii) c+a/b
# iii) a%b+c iV) a*b+c
print("Press 1 for a+b*c ")
print("Press 2 c+a/b")
print("Press 3 a%b+c")
print("Press 4 c+a/b")
choice = int(input("Enter Your Choice:- "))
first_Number = int(input("Enter a Number :- "))
Second_Number = int(input("Enter 2nd Number :- "))
Third_Number = int(input("Enter 3rd Number :- "))
if(choice ==1 ):
    c= first_Number+Second_Number+Third_Number
    print(c)
if(choice ==2):
    c= Third_Number+first_Number/Second_Number
    print(c)
if(choice == 3):
    c= first_Number%Second_Number+Third_Number
    print(c)
if(choice == 4):
    c =Third_Number+first_Number/Second_Number
    print(c)