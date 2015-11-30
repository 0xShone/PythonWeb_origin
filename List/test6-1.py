#coding: UTF-8

list = ["A", "B"]

list.append("C")
print list

list.extend(["D", "E"])
print list

newlist = list + ["F"]
print newlist

newlist.append(["G", "H"])
print newlist
