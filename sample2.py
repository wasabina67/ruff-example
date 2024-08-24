def greet(name):
    if name != "":
        return "Hello, " + name + "!"
    else:
        return "Hello, Stranger!"

def redundant_code():
    a = 10
    if a == 10:
        b = a
        print(b)
    else:
        print("This should never happen.")

greet("Alice")
redundant_code()
