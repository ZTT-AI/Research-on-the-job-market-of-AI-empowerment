import numpy as np
import matplotlib.pyplot as plt

# 数据准备
skills = [
    "UX/UI Design", "JavaScript", "Machine Learning", "Communication"
]
values = [22.42, 32.94, 3.12, 41.52]

# 计算角度
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False)

# 创建玫瑰图
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# 使用不同的颜色映射
colors = plt.cm.PuRd(np.linspace(0, 1, len(skills)))

# 绘制每个技能的扇形
for i in range(len(skills)):
    # 计算每个扇形的起始和结束角度
    start_angle = angles[i]
    end_angle = angles[i] + (2 * np.pi / len(skills))
    
    # 计算每个扇形的半径
    radius = values[i]
    
    # 绘制扇形
    ax.bar([start_angle], [radius], width=(2 * np.pi / len(skills)), bottom=0, 
           color=colors[i], alpha=0.7, edgecolor='black', linewidth=0.5)

# 设置技能标签
ax.set_xticks(angles)
ax.set_xticklabels(skills, fontsize=10, fontfamily='sans-serif')

# 设置径向标签
ax.set_rlabel_position(30)
ax.set_yticks([10, 20, 30, 40])
ax.set_yticklabels(['10%', '20%', '30%', '40%'], fontsize=10)

# 添加注释
for i in range(len(skills)):
    ax.text(angles[i], values[i] + 2, f"{values[i]:.2f}%", ha='center', fontsize=8)

# 添加标题
plt.title('Cluster 1 Skills Distribution', fontsize=16, fontfamily='sans-serif')

# 添加图例
plt.legend(['Cluster 1'], loc='upper right', bbox_to_anchor=(1.2, 1.0))

# 显示图形
plt.show()
plt.savefig('E:/技能需求玫瑰图_cluster1.png')  # 保存面积堆叠图
