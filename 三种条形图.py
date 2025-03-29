import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 设置文件路径
file_path = r'E:\薪资和公司规模数据.csv'
save_path = r'E:\salary_distribution_combined.png'

# 读取CSV文件
data = pd.read_csv(file_path)

# 检查数据结构
print(data.head())

# 按公司规模分组
small_company = data[data['Company_Size'] == 'Small']['Salary_USD']
medium_company = data[data['Company_Size'] == 'Medium']['Salary_USD']
large_company = data[data['Company_Size'] == 'Large']['Salary_USD']

# 创建图表
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制柱状图
ax1.hist([small_company, medium_company, large_company], 
         bins=30, 
         label=['Small', 'Medium', 'Large'],
         color=['#6495ED', '#FFA500', '#40E0D0'],
         alpha=0.5)

# 设置柱状图的标签和标题
ax1.set_xlabel('Salary (USD)')
ax1.set_ylabel('Counts', color='black')
ax1.tick_params(axis='y', labelcolor='black')

# 创建第二个坐标轴用于KDE曲线
ax2 = ax1.twinx()

# 绘制核密度估计曲线
sns.kdeplot(small_company, color='#6495ED', label='Small KDE', alpha=0.7, ax=ax2)
sns.kdeplot(medium_company, color='#FFA500', label='Medium KDE', alpha=0.7, ax=ax2)
sns.kdeplot(large_company, color='#40E0D0', label='Large KDE', alpha=0.7, ax=ax2)

# 设置KDE曲线的标签
ax2.set_ylabel('Density', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# 合并图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, title='Company Size', loc='upper right')

# 添加标题
plt.title('Salary Distribution by Company Size (Combined)')

# 保存图片
plt.savefig(save_path)
plt.close()

print(f'图片已保存到: {save_path}')