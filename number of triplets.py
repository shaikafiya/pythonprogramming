m=int(input())
c=0
n=list(map(int,input().split()))
for x in range(0,m-2):
    for y in range(x+1,m-1):
        for z in range(y+1,m):
            if(n[x]<n[y]<n[z]):
                c=c+1
    
print(c)
    
      
