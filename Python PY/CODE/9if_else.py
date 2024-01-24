# The if-else statement in Python facilitates conditional execution, running the code inside the if block if a specified condition is true, and the code inside the else block otherwise, enabling effective branching logic.

# example and use of if else
# if (condition):
#     do some work

x =  int(input("enter the number : " ))
if x > 5:
    print(x," is greater than 5")
else:
    print(x,"is not greater than 5")


# example 2: if-elif-else statement
    
y = int(input("enter the number : " ))
if y > 10:
    print(y," is greater than 10")
elif y == 10:
    print(y," is equal to 10")
else:
    print(y," is less than 10")

z=10
if z> 0:
    print(z," is a positive")
else:
    print(z," is a negative ")



# in print line to check odd even number
# even divisible by 2 
num = 3
print("Even" if num % 2 == 0 else "Odd")