N=int(input())
M=str(input())
F=str(input())
a=[]
for i in range(0,len(M)):
    if(M[i]==F[i]):
        a.append(M[i])
c=''.join(a)
print(c)
