import pandas as pd

# 读取CSV文件
file_path = 'E:\\岗位和技能数据.csv'
df = pd.read_csv(file_path)

# 确保Required_Skills列是字符串类型
df['Required_Skills'] = df['Required_Skills'].astype(str)

# 分割技能列（如果技能是用逗号分隔的）
df['Required_Skills'] = df['Required_Skills'].str.split(',')

# 将数据展开以便计算频数
df_exploded = df.explode('Required_Skills')

# 计算每个岗位下各个技能的频数
skill_frequency = df_exploded.groupby(['Job_Title', 'Required_Skills']).size().unstack(fill_value=0)

# 确保结果是一个10x10的矩阵
# 如果某些岗位或技能缺失，它们的频数将被填充为0
skill_frequency_matrix = skill_frequency.reindex(index=df['Job_Title'].unique(), columns=df_exploded['Required_Skills'].unique(), fill_value=0)

# 将结果保存到新的CSV文件
output_file_path = 'E:\\岗位技能频数矩阵.csv'
skill_frequency_matrix.to_csv(output_file_path)

print(f"技能频数矩阵计算完成，结果已保存到 {output_file_path}")