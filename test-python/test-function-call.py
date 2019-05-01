


a1 = [1,2,3]

def func1(a):
    for i in range(len(a)):
        a[i] += 1

    print(a)


a2 = "Hello"

def func2(a):
    print(a)
    a = "Hi"
    print(a)



# 함수 호출은 call by reference ...
if __name__ == "__main__":
    print(a1)
    func1(a1)
    print(a1)

    print(a2)
    func2(a2)
    print(a2)
