import art

print(f"{art.logo}\n Welcome to our Python calculator")

def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
a=float(input('type in the first number'))
continue_game="y"
while continue_game=="y":
    operations={
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
        
    
    for operation in operations:
        print(operation)
    c=input('input one of the operations from above')
    b=float(input('type in the second number'))
    d=operations[c]
    result=d(a,b)
    print(f"{str(a)} {str(c)} {b} = {str(result)} ")
    a=d(a,b)
    continue_game = input('Operate this number again? input "y" to continue or "n" to end')


print('goodbye')