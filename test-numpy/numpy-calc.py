import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 각 요소 더하기
c = a + b
# c = np.add(a, b)
print(c)  # [5 7 9]

# 각 요소 빼기
c = a - b
# c = np.subtract(a, b)
print(c)  # [-3 -3 -3]

# 각 요소 곱하기
# c = a * b
c = np.multiply(a, b)
print(c)  # [4 10 18]

# 각 요소 나누기
# c = a / b
c = np.divide(a, b)
print(c)  # [0.25 0.4 0.5]


# Matrix 연산은 dot 메서드를 사
lst1 = [
    [1, 2],
    [3, 4]
]

lst2 = [
    [5, 6],
    [7, 8]
]
a = np.array(lst1)
b = np.array(lst2)

c = np.dot(a, b)
print(c)
# 출력:
# [[19 22]
#  [43 50]]


a = np.array([[1, 2], [3, 4]])

s = np.sum(a)
print(s)  # 10

# axis=0 이면, ax 0의 출력을 만듬. 즉 컬럼끼리 더함
# axis=1 이면, ax 1의 출력을 만듬. 득 행끼리 더함
s = np.sum(a, axis=0)
print(s)  # [4 6]

s = np.sum(a, axis=1)
print(s)  # [3 7]

s = np.prod(a)
print(s)  # 24

