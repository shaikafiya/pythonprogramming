num=int(input())
m=list(map(int,input().split()))
s=0
l=[]
for x in range(0,len(m)-1):
	if int(m[x+1])>=int(m[x]):
		s=s+1
	else:
		l.append(s)
		s=0
print(max(l)+1)		
		
		
