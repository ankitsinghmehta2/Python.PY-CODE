# x=int(input("enter the number :"))
# y=x
# num=0
# while(y!=0):
#     r=y%10
#     y=y//10
#     num=num*10+r
# print(num)

# x=6
# for i in range(0,x):
#     for j in range(0,x-i-1):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# for i in range(5):
#     for j in range(5):
#         if (i+j==2) or (j-i==2) or (i-j==2) or (i+j==6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print() 

fact=1
c=5
for i in range(c,0,-1):
    fact=fact*i
print(fact)
