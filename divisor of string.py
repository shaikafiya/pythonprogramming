s1=input()
s2=input()
c=1
for y in range(4,min(len(s1),len(s2))+1):
    if (len(s1)%y==0 and len(s2)%y==0):
          c=c+1
print(c)         
