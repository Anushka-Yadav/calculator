# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function exponents two numbers
def exponentiation(x, y):
    return x ** y


# This function finds the floor division two numbers
def root(x, y):
    return x // y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponential")
print("6.Floor Division")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", exponentiation(num1, num2))

        elif choice == '6':
            print(num1, "//", num2, "=", root(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation != "yes":
            break

    else:
        print("Invalid Input")
        

from whiteCalculator import Calculator
c = Calculator()
print(c.run("1+8(5^2)"))
# Output: 201
print(c.run("9Ans"))
# Output: 1809

while True:
 print("1 Adition")
 print("2 Subtraction")
 print("3 multiplication")
 print("4 Division")

 choice = input("Enter your choice : ")

 num1 = float(input("Enter number 1 : "))
 num2 = float(input("Enter number 2 : "))

 if choice == "1":
     print(num1, "+", num2, "=", (num1+num2))
 elif choice == "2":
     print(num1, "-", num2, "=", (num1-num2))
 if choice == "3":
     print(num1, "*", num2, "=", (num1*num2))
 elif choice == "4":
     if num2 == 0.0:
       print("error 303")
     else:
         print(num1, "/", num2, "=", (num1/num2))

 else:
     print("invalid choice")

   

print("Enter Your Choice 1(Add)/2(Sub)/3(Divide)/4(Multiply)")
num = int(input())
if num == 1:
    print("Enter Number 1 : ")
    add1  = int(input())
    print("Enter Number 2 : ")
    add2 = int(input())
    sum = add1 + add2
    print("The Sum Is ", sum)
elif num == 2:
    print("Enter Number 1 : ")
    sub1  = int(input())
    print("Enter Number 2 : ")
    sub2 = int(input())
    difference = sub1 - sub2
    print("The Difference Is ", difference)
elif num == 3:
    print("Enter Number 1 : ")
    div1  = float(input())
    print("Enter Number 2 : ")
    div2 = float(input())
    division = div1 / div2
    print("The Division Is ", division)
elif num == 4:
    print("Enter Number 1 : ")
    mul1 = int(input())
    print("Enter Number 2 : ")
    mul2 = int(input())
    multiply = mul1 * mul2
    print("The Difference Is ", multiply)
else:
    print("enter a valid Number")

print("Choose operator (+,-,*,/):")
mode = input()
print("Choose first int:")
x = int(input())
print("Choose second int:")
y = int(input())

print("Your result:")
if mode == "+":
    print(x+y)
elif mode == "-":
    print(x-y)
elif mode == "*":
    print(x*y)
elif mode == "/":
    print(x/y)

root.title("calculator")

print("Python Calculator")
problem = input("Enter a math problem, or 'q' to quit") # Takes User's input
while (problem != "q", "Q"): # If problem = "q", or "Q", quit
    print("The answer to ", problem, "is:", eval(problem)) # Solve problem
    problem = input("Enter another math problom, or 'q' to quit: ") # Repeat question

print('Calculator')
input_1 = input('First Number? ')
input_2 = input('Second Number? ')

try:
    print(f'{input_1} + {input_2} is {float(input_1) + float(input_2)}')
    print(f'{input_1} - {input_2} is {float(input_1) - float(input_2)}') 
    print(f'{input_1} X {input_2} is {float(input_1) * float(input_2)}')
    print(f'{input_1} / {input_2} is {float(input_1) // float(input_2)}')
except Exception as e:
    print(f'ERROR: {e}')