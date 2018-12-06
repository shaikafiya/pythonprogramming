f=str(raw_input())
h=''.join(c[1] + c[0] for c in zip(f[::2], f[1::2])])
print(h)
