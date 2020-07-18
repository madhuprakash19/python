a=str(input())
b=str(input())
c=[]
for i in range(len(a)):
    if a[i]==b[i]:
        temp=str(0)
        c.append(temp)
    else:
        temp=str(1)
        c.append(temp)

print(*c,sep="")
