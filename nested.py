
def one():
    def two():
        print("good ")
    print("morning")
    two()
one()
#callfunction inside another function is called nested function.
def washhands():
    print("washing hands")
def servefood():
    print("serving food")
def eatfood():
    washhands()
    print("eating food")
    servefood()
eatfood()
