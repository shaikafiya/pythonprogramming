val = {'G': 1, 'H': 5, 'Y': 10, 'P': 50, 'E': 300, 'L': 500, 'Q': 1000 }
s = str(input())
s = s.upper()
t = 0
while s:
    if len(s) == 1 or val[s[0]] >= val[s[1]]:
        t += val[s[0]]
        s = s[1:]
    else:
        t += val[s[1]] - val[s[0]]
        s = s[2:]
print (t)


