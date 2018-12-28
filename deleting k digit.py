a,b=input().split()
b=int(b)
f=len(a)
g=[]
for i in range(0,f):
	s=a[i]
	g.append(s)
w=f-b
z=[]
for i in range(b,f):
	s=g[i]
	z.append(s)
print("".join(z))

