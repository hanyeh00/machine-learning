x=int(input("x: "))
n=1
l=[]
while x>=n:
    if x % n==0:
        l.append(n)
    n+=1
print(l)