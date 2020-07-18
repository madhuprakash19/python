n=int(input())
a=[]
b=[]
count=0
for i in range(n):
    m=[int(x) for x in input().split()]
    a.append(m[0])
    b.append(m[1])
for i in range(0,n):
    for j in range(0,n):
        if a[i]==b[j]:
            count+=1
print(count)
