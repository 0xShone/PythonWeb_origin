#coding: UTF-8

dict = {"yamada": 75, "endou": 82}
print dict

print 'del dict["endou"]'
del dict["endou"]
print dict

dict = {"yamada": 75, "endou": 82}
print dict

print 'dict.pop("yamada")'
val = dict.pop("yamada")
print u"削除された要素の値は" + str(val) + u"です"

print 'dict.pop("yamda", "none")'
val = dict.pop("yamda", "none")
print u"削除された要素の値は" + str(val) + u"です"

dict = {"yamada": 75, "endou": 82, "itou": 76}
print dict

while dict:
    tuple = dict.popitem()
    print tuple
