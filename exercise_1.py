#!/usr/bin/python3

num = 13  #int
flo = 13.13  #float
str_ = "asdf"  #str
str_mul = ''' asdf
asdf
asdf'''  #str
boolean = True  #bool

var_type = lambda x: str(type(x))[8:-2]

print("Zmienna {} typu {}".format("num",var_type(num)))
print("Zmienna {} typu {}".format("flo",var_type(flo)))
print("Zmienna {} typu {}".format("str_",var_type(str_)))
print("Zmienna {} typu {}".format("str_mul",var_type(str_mul)))
print("Zmienna {} typu {}".format("boolean",var_type(boolean)))