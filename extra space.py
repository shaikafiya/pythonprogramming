m=input()
a=list(m)
c=len(a)-1
for i in range(c):
    if a[i]==" ":
       a.remove(a[i])
       if i!=c-1:
          i=i+1
          c=c-1
       else:
           break
n="".join(a)
print(n)
          
    

   
    


 
   
