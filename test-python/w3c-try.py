# coding: utf-8

# x="Hello"

try:
    print(x)
# NameError가 발생했을 때
except NameError:
    print("Variable x is not defined")
# 다른 에러가 발생했을 때
except:
    print("Something else went wrong")
# 아무 문제가 없을 경우 실행되는 코드
else:
    print("Nothing went wrong")
# 에러 유무와 관계없이 항상 실행
finally:
    print("Finished try block!!")
