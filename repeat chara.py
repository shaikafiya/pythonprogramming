a=input()
b=[]
for i in a:
   if(i not in b):
      b.append(i)
s2="".join(map(str,b))
print(s2)

