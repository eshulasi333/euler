def leap_year(n):
    if n%400==0:
        return True
    if n%100==0:
        return False
    if n%4==0:
        return True
    else:
        return False
count=0
dy=7
for x in range(1900,2001):
    for y in range(1,13):
        if y==2:
            lim=28
        if y==2 and leap_year(x):
            lim=29
        if y==4 or y==6 or y==9 or y==11:
            lim=30
        else:
            lim=31
        while dy<=lim:
            if dy==1 and x>1900:
                count+=1
            dy+=7
        dy-=lim
print(count)