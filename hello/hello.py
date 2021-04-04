import cs50

name = cs50.get_string("What is your name? ")

if name:
    print("hello, " + name)
else:
    print("hello, world")