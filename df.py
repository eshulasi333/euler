import math
def fibonica():
    f1=1
    f=1
    i=2
    while len(str(f))<1000:
        i+=1
        f2=f
        f+=f1
        f1=f2
    print(i)

def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    s=math.sqrt(n)
    for x in range(3,int(s)+1):
        if n%x==0:
            return False
    else:
        return True
lis=[]
for de in range(1000000):
    if prime(de):
        g=str(de)
        for fr in range(1,len(g)):
            ui=int(g[fr:]+g[:fr])
            if not prime(ui):
                break
        else:
            lis.append(de)
print(len(lis))