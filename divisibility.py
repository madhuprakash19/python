n=int(input())
a=[]
b=[]
count=0
for i in range(n):
    m=[int(x) for x in input().split()]
    a.append(m[0])
    b.append(m[1])
for i in range(0,n):
    if a[i]%b[i]!=0:
        temp=b[i]
        p=1
        while(a[i]>=b[i]):
            b[i]=temp*p
            p+=1
        count=b[i]-a[i]
        print(count)
    else:
        print(0)
    
