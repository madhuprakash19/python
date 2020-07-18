a=input()
b='hello'
m=0
count=0
for i in range(0,len(a)):
    if a[i]==b[m]:
        m+=1
        count+=1
    if count==5:
        break
if(count==5):
    print('YES')
else:
    print("NO")
