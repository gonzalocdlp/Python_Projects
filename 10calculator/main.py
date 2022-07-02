import art

print(f"{art.logo}\n Welcome to our silent auction")

def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
a=int(input('type in the first number'))
continue_game="y"
while continue_game=="y":
    operations={
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
        
    b=int(input('type in the second number'))
    for operation in operations:
        print(operation)
    c=input('input one of the operations from above')
    d=operations[c]
    result=d(a,b)
    print(f"{str(a)} {str(c)} {b} = {str(result)} ")
    a=d(a,b)
    continue_game = input('end or continue input "y" for yes or n for "no"')


print('goodbye')