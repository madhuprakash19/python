n=int(input())
count=0
for i in range(n):
    temp=str(input())
    if temp=="Tetrahedron":
        count+=4
    if temp=="Cube":
        count+=6
    if temp=="Dodecahedron":
        count+=12
    if temp=="Octahedron":
        count+=8
    if temp=="Icosahedron":
        count+=20
print(count)
    
