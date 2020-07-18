a=str(input())
b=[]
if len(a)>2:
    for i in range(1,len(a),3):
        b.append(a[i])
#print(b)    
c=list(set(b))
print(len(c))
