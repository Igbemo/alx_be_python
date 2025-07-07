#This prpgramme allows me to use match case for multiple operations

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ") 

#The match case treating each operator as a case      
match operator:
        case '+':
            result = num1 + num2
            print(f"The result is {result} ")
        case '-':
            result = num1 - num2
            print(f"The result is {result} ")
        case '*':
            result = num1 * num2
            print(f"The result is {result} ")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero")
                exit()
                result = num1/num2
                print(f"The result is {result} ")

        
        
    
