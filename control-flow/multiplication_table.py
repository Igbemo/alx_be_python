#this programme prints a multiplication table of any number you entered

number = int(input("Enter a number to see its multiplication table: ")) #Enter a number to see its table
X = number
for Y in range(1,11):
    Z = Y * X
    print(f"{X} x {Y} = {Z}" )
