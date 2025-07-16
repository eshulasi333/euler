def palin(n):
    x=int(str(n)[-1::-1])
    if x==n:
        return True
    else:
        return False
def rev(m):
    y=int(str(m)[-1::-1])
    z=y+m
    return z
sr=[]
for x in range(10000):
    
    de=x
    for i in range(49):
        de=rev(de)
        if palin(de):
            break
    else:
        sr.append(x)
print(len(sr))