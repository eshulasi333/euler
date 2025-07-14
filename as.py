def palindoramic(n):
    n=int(n)
    m=int(str(n)[-1::-1])
    if m==n:
        return True
def binary(k):
    re=bin(k)
    er=re[2:]
    return er
sum=0
for x in range(1000000):
    if palindoramic(x):
        res=binary(x)
        if palindoramic(res):
            sum+=x
print(sum)