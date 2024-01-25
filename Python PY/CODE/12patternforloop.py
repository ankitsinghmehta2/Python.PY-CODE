# output
# *
# **
# ***
# ****
# *****
num=5
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end="")
    print()

    
# output opposite
num = 5
for i in range(0, num + 1):
    for j in range(0, num-i):
        print("*", end="")
    print()



# row =5
# output
#     *
#    * *
#   * * *
#  * * * *

num=int(input("enter the Row : "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()


# row =5
# output
#     *
#    ***
#   *****
#  *******
num=int(input("enter the Row : "))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print()


