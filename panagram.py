n=int(input())
a=str(input())
b=a.lower()
flag=0
for i in range(26):
    if chr(97+i) in b:
        flag=1
    else:
        flag=0
        break
if flag==0:
    print("NO")
else:
    print("YES")
    
