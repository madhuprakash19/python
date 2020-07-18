m=[int(i) for i in input().split()]
a=m[0]
n=m[1]
for i in range(0,n):
    if(a%10!=0):
        a=a-1
    else:
        a=a/10
print(int(a))
