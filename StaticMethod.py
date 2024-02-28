class StaicMethod:
    # These are static variable
    a = 10
    b = 20
    c = 30
    d = 40 
    e = 50

    #Static Method Declaration 
    @staticmethod
    def Display():
        print("This is Static Method")
        print("These are staic varibale")
        print(StaicMethod.a)
        print(StaicMethod.b)
        print(StaicMethod.c)
        print(StaicMethod.d)
        print(StaicMethod.e)

StaicMethod.Display()

# if we want to create a object of the class then we have to do it like this 
obj = StaicMethod
obj.Display()
# this will perform same operation like StaticMethod obj = new StaticMethiod(); syntax 