

x={}
y={"apple"}

print(type(x))
print(type(y))

# add set item in x
# x.add("orange")
x["color"]="red"
x["type"]="apple"
x["price"]=1000.0
print(type(x), x)

for i,j in x.items():
    print(i,j);

