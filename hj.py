import math
def th():
    s=1
    i=2
    d=0
    while d<500:
        d=2
        s+=i
        i+=1
        for r in range(2,int(math.sqrt(s))+1):
            if r==math.sqrt(s):
                d+1
            if s%r==0:
                d+=2
    print(s)

def leap(n):
    if n%400==0:
        return True
    if n%100==0:
        return False
    if n%4==0:
        return True
def gh():
    sub=0
    for x in range(1900,2001):
        year_day=30*4+31*7
        if leap(x):
            year_day+=29
        else:
            year_day+=28
        if x==1900:
            dew=year_day
        sub+=year_day
    sub=sub-dew
    er=sub//7
    if sub%7==0:
        er=er-1
    print(er)
day=7
for y in range(1900,2001):
    