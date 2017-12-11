password="hello"

def id(value):
    if(value==password):
        print("password match")

    else:
        print("wrong password")


value=input("Enter your password:")
id(value)