import json

# some JSON:

x =  '{ "name":"John", "age":30, "city":"New York"}'
# x =  '{ name:"John", age:30, city:"New York"}' # JSON key 값은 ""를 사용

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Convert python object & types to JSON

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# Convert python types to JSON

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))