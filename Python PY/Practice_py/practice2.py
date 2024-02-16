num=123
y=num
x=0
while(y!=0):
    r=y%10
    y=y//10
    x=x*10+r
print(x)
