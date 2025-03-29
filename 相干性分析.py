import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv(r'E:/normalized_data.csv')  # 确保这是你标准化后的数据文件

# 计算相关系数矩阵
correlation_matrix = data.corr()

# 保存相关系数矩阵到CSV文件
#correlation_matrix.to_csv('E:/correlation_matrix.csv')  # 保存到当前目录

# 使用Seaborn生成热力图
plt.figure(figsize=(12, 10))  # 设置热力图的大小
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='Reds', linewidths=0.5)

# 保存热力图为图片
plt.savefig(r'E:/correlation_heatmap.png')  # 保存到当前目录
plt.close()  # 关闭图像窗口