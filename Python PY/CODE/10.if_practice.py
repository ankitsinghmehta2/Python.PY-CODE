age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")


num1=float(input("Enter the First Number: "))
num2=float(input("Enter the Second number: "))
num3=float(input("enter the third number: "))
if num1>=num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2>=num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

word = input("Enter a word: ").lower()
reversed_word = word[::-1]

if word == reversed_word:
    print(reversed_word,"Palindrome")
else:
    print(reversed_word,"Not a palindrome")