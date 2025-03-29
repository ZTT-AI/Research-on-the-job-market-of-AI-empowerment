import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
file_path = r"E:\城市岗位规模马赛克数.csv"
data = pd.read_csv(file_path)

# 计算每个岗位和地点组合的公司规模平均数
pivot_table = data.pivot_table(index='Job_Title', columns='Location', values='Company_Size', aggfunc='mean')

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 绘制热力图（调整图形尺寸）
plt.figure(figsize=(14, 12))  # 增大画布尺寸
sns.heatmap(
    pivot_table, 
    annot=True, 
    fmt=".2f", 
    cmap="YlGnBu",
    annot_kws={"fontsize": 10}  # 注释字体大小
)

# 添加标题和标签（设置字体大小）
plt.title('Average Company Size by Job Title and Location', fontsize=16)
plt.xlabel('Location', fontsize=14)
plt.ylabel('Job Title', fontsize=14)

# 优化坐标标签显示
plt.xticks(
    rotation=45, 
    ha='right',  # 右对齐防止重叠
    fontsize=12
)
plt.yticks(fontsize=12)

plt.tight_layout()  # 自动调整布局，避免元素重叠

# 保存图片到 E 盘根目录（优化保存参数）
save_path = r"E:\city_job_size_heatmap.png"
plt.savefig(save_path, bbox_inches='tight')  # 裁剪空白边缘

# 显示图形
plt.show()