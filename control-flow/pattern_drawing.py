# This programme draws a simple text-based pattern.
i=0
x = int(input("Enter the size of the pattern: ")) #This value creates the number of rows amd for the outer loop
while i < x:
    j = 0
    while j < 4:
        print ( "*" ,end = "") #this prints tbe value of j in four columns, horizontal *
        j = j +1
    print()
    i = i+1