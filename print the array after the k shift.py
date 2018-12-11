N1,n=map(int,input().split())
N=input().split()
while(n>0):
    N.insert(0,N.pop())
    n=n-1
for i in range(0,len(N)):
    if(i!=len(N)-1):
        print(N[i],end=(" "))
    else:
         print(N[i])
  
