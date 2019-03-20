# coding: utf-8

# iterable object
# iterable object는 __iter__(), __next__()를 구현한 객체이다.
# list,tuple,set,dictionary,
# string

mytuple = ("bannea", "apple", "orange")

myiter = iter(mytuple)

print(next(myiter));
print(next(myiter));
print(next(myiter));

# String도 iterator object이다.
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# for x in y:를 써도 된다.
# 사실 for..은 iterator를 이용해서 구현된다.


# 나만의 iterator를 만들 수 있다.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Iteration을 정지하기
# 정지 조건에서 StopIteration

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)




