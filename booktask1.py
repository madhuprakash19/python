a=[i for i in input().split()]
b=[]
for i in range(0,len(a)):
    b.append(' ')
for i in range(0,len(a)):
    b[i]='a'+a[i][1:]+a[i][0]
print(b)
c=' '.join(b)
print(c)
    
