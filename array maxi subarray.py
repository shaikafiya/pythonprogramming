m=int(input())
l=list(map(int,input().split()))
n=l[0]
k=[]
k.append(n)
for x in range(1,len(l)):
    n=n+l[x] 
    k.append(n)
k.append(l[len(l)-1])
a=l[len(l)-1]
for y in range(len(l)-2,-1,-1):
    a=a+l[y] 
    k.append(a)
    
    
print(max(k))
    

