# coding: utf-8

import mymodule as mm

mm.greeting("Kang")

# Built-in Modules

from mymodule import person1

print(person1["age"])

import platform

x = platform.system()
print(x)

# Built-in function dir() shows all names in module

y = dir(x)
print(type(y),len(y))
# for z in y:
#     print(z)