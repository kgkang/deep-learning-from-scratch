import pandas as pd
import numpy as np

# 10 Minutes to pandas
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min

# Series
# 1 차원 구조
data = [1, 3, 5, 7, 9]
s = pd.Series(data)

print(type(s))
print(s)

# Dataframe
# 2차원 구

data = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}

df = pd.DataFrame(data)
print(df)

# Panel => Deprecated. Dataframe을 이용
# 3차원 데이터 구조

# data = np.random.rand(2,3,4)
# p = pd.Panel(data)
# print(p)




