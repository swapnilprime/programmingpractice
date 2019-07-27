#sieve of euler
#https://programmingpraxis.com/2011/02/25/sieve-of-euler/
s=[]
t=[]
for i in xrange(30):
    s.append(i+2)
s.pop()
print s
j=0
i=s[j]
while i*i < 30:
    for k in s:
        l=k*i
        if l in s:
            t.append(l)
    for h in t:
        if h in s:
            s.remove(h)
    j=j+1
    i=s[j]
print s 