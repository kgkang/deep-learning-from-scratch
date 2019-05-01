import pandas as pd
import numpy as np

# 1차원 데이터는 pd.Series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# 2차원 데이터는 pd.Dataframe
# ==================


dates = pd.date_range('20130101', periods=6)
print(dates)

# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)


# df2 = pd.DataFrame({'A': 1.},
#                    {'B': pd.Timestamp('20130102')},
#                    {'C': pd.Series(1,index=list(range(4)), dtype='float32')},
#                    {'D': })


# =========
