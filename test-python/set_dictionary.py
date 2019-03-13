# coding : utf-8

ds= {}

print(type(ds))


print("====================")
thisset = { "v1", "v2", "v3"}
print(type(thisset))
print(thisset)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("====================")
print(thisdict)

key=thisdict.keys()
print(type(key), key)

values=thisdict.values()
print(type(values), values)

print(thisdict.items())


# Accessing Items
print(thisdict["model"])
print(thisdict.get("brand"))


# Change & add key,value
thisdict["color"]="yellow"
print(thisdict.get("color"))

# Loop
print("=============================")
for x in thisdict:
    print(x, thisdict[x])
    # print(thisdict[x])


for k,v in thisdict.items():
    print(k, v)

# Clear dictionary
print("=============================")

thisdict.clear()
print(thisdict)

del thisdict
# print(thisdict) # Error