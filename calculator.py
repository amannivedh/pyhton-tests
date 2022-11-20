def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculator():
    operations={"+":add,"-":subtract,"*":multiply,"/":divide}
    num1=int(input("Enter the first number: "))
    for symbols in operations:
        print(symbols) 
    should_continue=True
    while should_continue:    
        operation_symbol=input("Pick and operation ")    
        num2=int(input("Enter the second number: "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)


        print(f"{num1} {operation_symbol} {num2}= {answer}")
        if(input(f"Type 'y' to continue calculating with {answer} else type 'n' to exit: ").lower())=="y":
            num1=answer
        else:    
            should_continue=False
            calculator()
calculator()