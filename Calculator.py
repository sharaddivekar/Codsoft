a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("Select operation to be performed: /n 1.Addition /n 2.Subtraction /n 3.Multiplication /n 4.Division")
select=int(input("Select operation from 1, 2, 3, 4 :"))
if select==1:
    print(add(a,b))
elif select==2:
    print(sub(a,b))
elif select==3:
    print(mul(a,b))
elif select==4:
    print(div(a,b))
