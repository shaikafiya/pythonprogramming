h=int(input())
l=input().split()
a=" ".join(map(str,l))
m=[]
for x in a:
    if(x not in m):
        if(a.count(x)>1):
            m.append(x)
i=" ".join(m) 
print(i)

