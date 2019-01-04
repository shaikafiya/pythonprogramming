M= int(input())
N=[int(x) for x in input().split()]
H=N[::-1]
D=len(H)
for i in range(0,D-1):
    print(G[i],end="->")
print(H[D-1])    
