M= int(input())
N=[int(x) for x in input().split()]
G=N[::-1]
D=len(G)
for i in range(0,D-1):
    print(G[i],end=">")
print(G[D-1])    
