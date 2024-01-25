# palindrome

x=int(input("enter the number :"))
y=x
num=0
while(y!=0):
    r=y%10
    y=y//10
    num=num*10+r
print(num)

 
# input = 123
# output = 321




x = int(input("Enter the number:"))  # Takes an integer input from the user
y = x  # Assigns the input number to another variable 'y'
num = 0  # Initializes a variable 'num' to store the reversed number

while y != 0:  # While 'y' is not equal to 0
    r = y % 10  # Gets the last digit of 'y'
    y = y // 10  # Removes the last digit from 'y'
    num = num * 10 + r  # Builds the reversed number digit by digit
print(num)  # Prints the reversed number
