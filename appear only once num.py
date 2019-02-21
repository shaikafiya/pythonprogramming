n=int(input())
m=input().split()
h=len(m)
for i in range(0,h):
    z=m.count(m[i])
    if(z<2):
       print(m[i])
       
