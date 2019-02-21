i,j=map(int,input().split())
s=input().split()
h=input().split()
s.sort()
h.sort()
S1=''.join(s)
S2=''.join(h)
if(S2 in S1):
     print("YES")
else:
     print("NO")   
        
        
        
