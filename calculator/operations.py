def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def main():
    print("1- Add\n 2- Subtract\n 3- Multiply\n 4- Divivde")
    op=int(input("Enter your choice:"))
    num1=int(input("Enter the first num:"))
    num2=int(input("Enter the second num:"))
    
    if op==1:
        print(f"{num1}+{num2}={add(num1,num2)}")
    elif op==2:
        print(f"{num1}-{num2}={subtract(num1,num2)}")
    elif op==3:
        print(f"{num1}*{num2}={multiply(num1,num2)}")
    elif op==4:
        print(f"{num1}/{num2}={divide(num1,num2)}")
    else:
        print("Enter 1-4!")
    
if __name__=="__main__":
    main()

# Webhook test
# Webhook test 2
