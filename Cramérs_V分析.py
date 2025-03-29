import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv(r'E:\独热变量标准化（岗位和技能）.csv')

# 处理列名，去掉前缀
job_columns = data.columns[:10].str.replace('Job_Title_', '')
skill_columns = data.columns[10:20].str.replace('Required_Skills_', '')

# 初始化相关性矩阵
cramer_v_matrix = pd.DataFrame(index=job_columns, columns=skill_columns)

# 计算Cramér's V
for i, job in enumerate(job_columns):
    for j, skill in enumerate(skill_columns):
        contingency_table = pd.crosstab(data.iloc[:, i], data.iloc[:, j + 10])
        chi2, _, _, _ = chi2_contingency(contingency_table)
        n = data.shape[0]
        cramer_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
        cramer_v_matrix.loc[job, skill] = cramer_v

# 保存矩阵到E盘
cramer_v_matrix.to_csv(r'E:\岗位技能_Cramérs_V矩阵.csv')

# 绘制热力图
plt.figure(figsize=(12, 8))
sns.heatmap(cramer_v_matrix.astype(float), annot=True, cmap='coolwarm', fmt='.3f')
plt.title('岗位-技能 Cramér\'s V 关联强度热力图')
plt.xlabel('技能')
plt.ylabel('岗位')

# 设置标签斜体并旋转
plt.xticks(rotation=45, ha='right', style='italic')
plt.yticks(rotation=0, style='italic')

# 保存热力图到E盘
plt.tight_layout()
plt.savefig(r'E:\岗位技能_Cramérs_V热力图.png')
plt.show()