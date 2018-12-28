b,c=input().split()
c=list(c)
d=list(d)
e=len(c)
f=len(d)
i=0
j=0
h=[]
while e>0:
   if b[i]==c[j]:
       h.append(b[i])
   j=j+1
   i=i+1
   e=e-1
print(f-len(h))        
