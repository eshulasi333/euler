def tri(m,l):
    a=m[-1]
    b=m[-2]
    diff=a-b+1
    tu=a+diff
    m.append(tu)
    if tu<l:
        return tri(m,l)
    return m
se=[1,3,6,10]
so=input(">").strip().split(",")
count=0
val=0
for x in so:
    tr=x[1:-1]
    for t in tr:
        val+=ord(t.lower())-ord("a")+1
    if val>se[-1]:
        ty=tri(se,val)
    if val in se:
        count+=1
    val=0
print(count)