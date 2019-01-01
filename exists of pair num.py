def sumpair(l,k,c):
    for i in range(l):
        for j in range(i+1,l):
            if ((c[i]+c[j])==k):
                return('yes')
            return('no')
a=(input()).split()
a=list(map(int,a))
b=(input()).split()
b=list(map(int,b))
print(sumpair(a[0],a[1],b))                   
                   
