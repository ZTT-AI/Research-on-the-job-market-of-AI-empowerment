import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency

# 读取数据
data = pd.read_csv(r'E:\独热变量标准化（岗位和技能）.csv')

# 统一处理列名，去除前缀
data.columns = data.columns.str.replace('Job_Title_', '').str.replace('Required_Skills_', '')
job_columns = data.columns[:10]  # 岗位列
skill_columns = data.columns[10:20]  # 技能列

# 打印列名，检查是否正确获取
print("岗位列名：", job_columns.tolist())
print("技能列名：", skill_columns.tolist())

# 初始化矩阵
contingency_c_matrix = pd.DataFrame(index=job_columns, columns=skill_columns)
lambda_matrix = pd.DataFrame(index=job_columns, columns=skill_columns)

# 计算列联相关系数（Contingency Coefficient, C）
for job in job_columns:
    for skill in skill_columns:
        contingency_table = pd.crosstab(data[job], data[skill])
        chi2, _, _, _ = chi2_contingency(contingency_table)
        n = data.shape[0]
        c_value = np.sqrt(chi2 / (chi2 + n))  # 列联相关系数公式
        contingency_c_matrix.loc[job, skill] = c_value

# 计算 Lambda 系数
label_encoder = LabelEncoder()
for job in job_columns:
    for skill in skill_columns:
        # 处理数据（Lambda 需类别编码）
        job_encoded = label_encoder.fit_transform(data[job])
        skill_encoded = label_encoder.fit_transform(data[skill])
        
        max_freq_job = data[job].value_counts().max()
        max_freq_skill = data[skill].value_counts().max()
        
        # 避免分母为 0
        denominator = data.shape[0] - data[job].nunique()
        lambda_value = (max_freq_job + max_freq_skill - data.shape[0]) / denominator if denominator != 0 else 0
        lambda_matrix.loc[job, skill] = lambda_value

# 绘制列联相关系数 C 热力图
plt.figure(figsize=(12, 8))
sns.heatmap(contingency_c_matrix.astype(float), annot=True, cmap='coolwarm', fmt='.3f')
plt.title('岗位-技能 列联相关系数（C）热力图')
plt.xlabel('技能')
plt.ylabel('岗位')
plt.xticks(rotation=45, ha='right', style='italic')
plt.yticks(rotation=0, style='italic')
plt.tight_layout()
plt.savefig(r'E:\岗位技能_列联相关系数C热力图.png')
plt.clf()

# 绘制 Lambda 系数热力图
plt.figure(figsize=(12, 8))
sns.heatmap(lambda_matrix.astype(float), annot=True, cmap='coolwarm', fmt='.3f')
plt.title('岗位-技能 Lambda 系数热力图')
plt.xlabel('技能')
plt.ylabel('岗位')
plt.xticks(rotation=45, ha='right', style='italic')
plt.yticks(rotation=0, style='italic')
plt.tight_layout()
plt.savefig(r'E:\岗位技能_Lambda系数热力图.png')
plt.show()