m,k=map(int,(input()).split())
a=[]
c=[]
for i in range(m):
    a.append(list(map(int,(input()).split())))
for i in range(k):
    if all(a[0][i] in a[j]for j in range(1,m)):
        c=c+[a[0][i]]
c=sorted(c)
print(" ".join(str(i) for i in c))
