import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# 读取数据
data = pd.read_csv(r'E:\独热变量标准化（岗位和技能）.csv')

# 提取前 10 列岗位数据和后 10 列技能数据
job_columns = data.columns[:10]
skill_columns = data.columns[10:20]

# 去掉岗位和技能列名的前缀
job_columns = [col.replace('Job_Title_', '') for col in job_columns]
skill_columns = [col.replace('Required_Skills_', '') for col in skill_columns]

# 创建一个空的 DataFrame 用于存储 p 值
p_value_matrix = pd.DataFrame(index=job_columns, columns=skill_columns)

# 对岗位和技能进行两两卡方检验
for i, job in enumerate(job_columns):
    for j, skill in enumerate(skill_columns):
        # 创建列联表
        contingency_table = pd.crosstab(data[data.columns[i]], data[data.columns[j + 10]])
        # 进行卡方检验
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        p_value_matrix.loc[job, skill] = p

# 保留 3 位小数
p_value_matrix = p_value_matrix.round(3)

# 将结果保存到 E 盘根目录下的 CSV 文件
#result_path = r'E:\岗位技能卡方检验结果.csv'
result_path = r'E:\岗位和技能独热编码（0-1变量）.csv'
p_value_matrix.to_csv(result_path)

# 绘制 p 值的热力图
plt.figure(figsize=(10, 8))
sns.heatmap(p_value_matrix.astype(float), annot=True, cmap='coolwarm', fmt='.3f')
#plt.title('岗位和技能卡方检验 p 值热力图')
plt.xlabel('Required_Skills')
plt.ylabel('Job_Title')

# 设置 x 轴和 y 轴标签为斜体并旋转一定角度
plt.xticks(rotation=45, ha='right', style='italic')
plt.yticks(rotation=0, style='italic')

# 增加边栏留白
plt.tight_layout()

# 保存热力图到 E 盘根目录
heatmap_path = r'E:\岗位技能卡方检验_p值热力图.png'
plt.savefig(heatmap_path)
plt.show()