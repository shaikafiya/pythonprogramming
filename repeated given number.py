h=int(input())
j=input().split()
c=" ".join(map(str,j))
c=[]
for x in c:
    if(x not in c):
        if(c.count(x)>1):
            k.append(x)
i=" ".join(k) 
print(i)
