# coding: utf-8

# 파일을 open해서 작업한 후
# 파일을 close해줘야 한다.

f1 = open("./with.txt", "w")
f1.write("f1에서 기록합니다.")
# f1.close()


# with는 close를 자동으로 해주는 역할을 한다.
# with문에 포함된 f2는 블록을 벗어나는 순간 자동으로 close된다.
with open("./with.txt", "w") as f2:
    f2.write("f2에서 기록합니다.")
