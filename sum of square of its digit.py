a=int(input())
d=0
while(a>0):
    a1=int(a%10)
    d=(a1*a1)+d
    a=int(a/10)
print(d)
