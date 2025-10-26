user = input("Expression: ")
num1,operator,num2 = user.split()
num1, num2 = float(num1), float(num2)

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)

    case "/":
        print(num1 / num2)
   
    case "*":
        print(num1 * num2)

    case _:
        print("Operator not reconized")