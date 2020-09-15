import pandas as pd

key = ["ss", "qq"]
value = [[1, 2, 3], [2, 3, 4]]
staa = dict(zip(key, value))


df = pd.DataFrame.from_dict(staa)
print(type(df))
print(df)
for i in range(df.shape[1]):
    print(df.iloc[i])  # 返回某一行
    print(df.iloc[:, i])  # 返回某一列

