n,b=map(int,input().split())
c=0
y=b-1
while(c==0 and y>1):
    if(b%y==0 and n%y==0):
         c+=1
    y-=1
print(y+1)    
