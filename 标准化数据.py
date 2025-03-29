import pandas as pd
from sklearn.preprocessing import StandardScaler

# 加载数据
data = pd.read_csv('E:/赋值_encoded1.csv')

# 选择数量数据的列
columns_to_normalize = data.columns

# 创建StandardScaler对象
scaler = StandardScaler()

# 应用Z标准化
data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

# 保存标准化后的数据
data.to_csv('E:/normalized_data.csv', index=False)