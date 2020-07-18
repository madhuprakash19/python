a=str(input())
n=len(a)
s=''
for i in range(0,n):
    if a[i] in "a e i o u y A E I O U Y":
       continue
      
    else:
        s=s+'.'+(a[i].lower())
        
print(s)
