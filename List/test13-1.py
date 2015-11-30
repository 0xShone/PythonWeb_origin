#coding: UTF-8

print list("ABC")
print list((20, 18))

l = ["PHP", "PERL"]
print list(l)

t = (74, 82, 59)
print t
tmplist = list(t)
tmplist.reverse()
t = tuple(tmplist)
print t
