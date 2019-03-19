# coding: utf-8


# tuple 생성
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[1])

# 생성자를 이용해서 생성
thistuple2 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple2)

#
for x in thistuple1:
    print(x)

if "apple" in thistuple1:
    print("Yes, Apple is in thistuple1")

