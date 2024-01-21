x=int(input("enter the number :"))
y=x
num=0
while(y!=0):
    r=y%10
    y=y//10
    num=num*10+r
print(num)