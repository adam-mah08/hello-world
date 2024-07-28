x=int(input("Give me a number:"))
n=x
y=1
while n>0:
    if x==0:
        print("The factorial of 0 is 0.")
    else:
        y= y*n
        n=n-1
print(f"The factorial of {x} is {y}")