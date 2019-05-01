import numpy as np


lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)

# 슬라이스
a = arr[0:2, 0:2]
print(a)
# 출력:
# [[1 2]
#  [4 5]]

a = arr[1:, 1:]
print(a)
# 출력:
# [[5 6]
#  [8 9]]


# 정수 슬라이싱

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)

# 정수 인덱싱
s = a[[0, 2], [1, 3]]
# s = a[[0, 2], [1, 3], [1, 2]]

print(s)
# 출력
# [2 12]

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)

bool_indexing_array = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])

n = a[bool_indexing_array];
print(n)
# 출력
# [2 4 6 8]

# Boolean indexing 두번째 방법
# 표현식으로 boolean index를 만들어서 사용
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)

# 배열 a 에 대해 짝수면 True, 홀수면 False
bool_indexing = (a % 2 == 0)

print(bool_indexing)
# 출력: 부울린 인덱싱 배열
# [[False  True False]
#  [ True False  True]
#  [False  True False]]

# 부울린 인덱스를 사용하여 True인 요소만 뽑아냄
print(a[bool_indexing])
# 출력:
# [2 4 6 8]

# 더 간단한 표현
n = a[a % 2 == 0]
print(n)
