b,d=map(int,input().split())
c=0
for i in range(b,d):
    if(int(i**0.5)==i**0.5):
          c=c+1
    else:
        c=c
print(c)        
