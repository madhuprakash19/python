n=int(input())
count=0
a=[]
for i in range(0,n):
    new=str(input())
    a.append(new)
for i in range(0,n):
    if a[i] in "+":
        count=count+1
    else:
        count=count-1
print(count)

