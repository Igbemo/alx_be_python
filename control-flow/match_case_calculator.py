#This prpgramme allows me to use match case for multiple operations

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
operator = input("Choose the operation (+, -, *, /): ")

if operator == '/'and num1 and num2 ==0:
        print("Cannot divide by zero.") 

#The match case treating each operator as a case      
else: 
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
            result = num1 / num2
            print(f"The result is {result}")    


        
        
    
