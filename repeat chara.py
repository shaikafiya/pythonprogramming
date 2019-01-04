a=input()
b=[]
for i in a:
   if(i not in b):
       b.append(i)
s1="".join(map(str,b))
print(s1)
    

