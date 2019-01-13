m=int(input())
h=input().split()
d=len(h)
for i in range(0,d):
    z=h.count(h[i])
    if(z<2):
          print(h[i])
