import math
# This function adds two numbers
# Essa função soma dois números
def add(x, y):
    return x + y

# This function subtracts two numbers
# Essa função subtrai dois números
def subtract(x, y):
    return x - y

# This function multiplies two numbers
# Essa função multiplica dois números
def multiply(x, y):
    return x * y

# This function divides two numbers
# Essa função divide dois números
def divide(x, y):
    return x / y

# This function does math power
# Essa função eleva um número ao outro (potenciação)
def power(x, y):
    return x ** y

# This function divides a number, but leaves the result integer and approximate
# Essa função faz a divisão com resto, mas não o exibe
def divideaprox(x, y):
    return x // y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Aproximated division")

while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4/5/6) -> ")

    # Check if choice is one of the six options
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number -> "))
            num2 = float(input("Enter second number -> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", power(num1, num2))

        elif choice == '6':
            print(num1, "//", num2, "=", divideaprox(num1, num2))
        
        # Check if user wants another calculation
        # Confirma se o usuário quer fazer outro cálculo

        # Break the while loop if answer is 'No' or 'no'
        # Quebra o loop 'while' se a resposta for 'No' ou 'no'
        next_calculation = input("Press ENTER to do next calculation or digit 'close' to exit -> ")
        if next_calculation == "close":
          break
        elif next_calculation == "Close":
          break
    else:
        print("Invalid Input")