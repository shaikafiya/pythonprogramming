a=int(input())
s=str(input())
e=[]
for x in s:
    if(x!=('a'or'e'or'i'or'o'or'u')):
        e.append(x)
print(e)
e.reverse()
print(e)
c=''.join(e)
print(c)
