t = "mam123"
m = []
for x in t:
    if x.isdecimal() and x != "0":
        
        k = t.index(x)
        m.append(k)
        
u = m[0]     
g = t[u:]
print(g.isdecimal())


s = []

s.append(2)
s.append(3)

print(s)


