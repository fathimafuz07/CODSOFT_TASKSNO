def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "error:Cannot divide by zero"
def calculator():
    print("Simple Calculator")
    keep_going="y"
    while keep_going=="y":
        a=float(input("enter first number:"))
        b=float(input("enter second number:"))
        op=input("enter operation(+,-,*,/):")
        if op=="+":
            result=add(a,b)
        elif op=="-":
            result=substract(a,b)
        elif op=="*":
            result=multiply(a,b)
        elif op=="/":
            result=divide(a,b)
        else:
            result="invalid operation"
        print("Result:",result)
        keep_going=input("do you want to calculate again?(y/n):").lower()
    print("Goodbye")
calculator()
    
