a=str(input())
n=len(a)
b=[]
i=0
while (i<n):
    if a[i]=='W' and a[i+1]=='U' and a[i+2]=='B':
        i=i+2
        #print(i)
        b.append("")
        i=i+1
    else:
        #print(i)
        b.append(a[i])
        i=i+1
#print(b)
print(" " . join(b))

    
