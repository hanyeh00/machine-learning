import copy
class father:
    a = {1:2, 2:9,3:80,4:50}
    b=a

    print(b)
class child(father):
    c=copy.copy(father.a)
a=father
a[1]=40
print(b)
print(c)
print(d)