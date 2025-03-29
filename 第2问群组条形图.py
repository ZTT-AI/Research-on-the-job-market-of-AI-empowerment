import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置文件路径
data_path = r'E:\按城市分岗位和规模.xlsx'
output_path = r'E:\群组条形图.png'

# 加载数据
data = pd.read_excel(data_path)

# 创建一个交叉表，统计每个岗位在不同公司规模中的数量
crosstab_data = pd.crosstab(data['Job_Title'], data['Company_Size'])

# 绘制群组条形图
plt.figure(figsize=(12, 8))
crosstab_data.plot(kind='bar', ax=plt.gca())

# 添加标题和标签
plt.title('岗位与公司规模分布 - 群组条形图')
plt.xlabel('岗位')
plt.ylabel('数量')
plt.legend(title='公司规模')

# 调整X轴标签旋转角度，避免重叠
plt.xticks(rotation=45)

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig(output_path)

# 显示图片
plt.show()

print(f'群组条形图已保存到: {output_path}')