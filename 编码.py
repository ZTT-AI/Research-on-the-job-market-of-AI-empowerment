import pandas as pd

# 读取 CSV 文件
file_path = 'E:/赋值.csv'  # 替换为你的文件路径
data = pd.read_csv(file_path)

# 对指定的名义变量进行独热编码
categorical_columns = ['Job_Title', 'Industry', 'Location', 'Required_Skills']
data_encoded = pd.get_dummies(data, columns=categorical_columns)

# 查看处理后的数据
print(data_encoded.head())

# 如果需要保存处理后的数据到新的 CSV 文件
data_encoded.to_csv('E:/赋值_encoded.csv', index=False)