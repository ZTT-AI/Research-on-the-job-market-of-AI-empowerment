import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal


def create_ellipsoid(mean, cov, n_std=2):
    # 创建椭球体
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = mean[0] + n_std * np.outer(np.cos(u), np.sin(v)) * np.sqrt(cov[0, 0])
    y = mean[1] + n_std * np.outer(np.sin(u), np.sin(v)) * np.sqrt(cov[1, 1])
    z = mean[2] + n_std * np.outer(np.ones_like(u), np.cos(v)) * np.sqrt(cov[2, 2])
    return x, y, z

# 读取岗位技能频数矩阵
file_path = 'E:\\岗位技能频数矩阵.csv'
df = pd.read_csv(file_path, index_col=0)  # 第一列作为行索引

# 数据标准化
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# 使用PCA降维到3维
pca = PCA(n_components=3)
pca_data = pca.fit_transform(scaled_data)

# KMeans聚类
n_clusters = 2  # 假设分为2类，您可以根据需要调整
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# 将聚类结果添加到原始数据框
df['Cluster'] = clusters

# 可视化聚类结果（三维图）
fig = plt.figure(figsize=(14, 12))
ax = fig.add_subplot(111, projection='3d')

# 定义颜色和标记
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
markers = ['o', 's', 'D', '^', 'v', '<', '>']

# 绘制每个聚类的点
for i in range(n_clusters):
    cluster_data = pca_data[clusters == i]
    ax.scatter(
        cluster_data[:, 0], cluster_data[:, 1], cluster_data[:, 2],
        c=colors[i % len(colors)], marker=markers[i % len(markers)],
        label=f'Cluster {i}', s=100, alpha=0.8, edgecolors='w', linewidths=0.5
    )

    # 计算聚类的质心和协方差矩阵
    mean = np.mean(cluster_data, axis=0)
    cov = np.cov(cluster_data, rowvar=False)
    
    # 创建椭球体
    try:
        x, y, z = create_ellipsoid(mean, cov)
        ax.plot_surface(x, y, z, color=colors[i % len(colors)], alpha=0.2)
    except np.linalg.LinAlgError:
        print(f"Cluster {i} has a singular covariance matrix. Skipping surface plot for this cluster.")

# 设置轴标签和标题
ax.set_xlabel('Principal Component 1', fontsize=10, fontfamily='sans-serif')
ax.set_ylabel('Principal Component 2', fontsize=10, fontfamily='sans-serif')
ax.set_zlabel('Principal Component 3', fontsize=10, fontfamily='sans-serif')
ax.set_title('3D KMeans Clustering of Job Skills', fontsize=14, fontfamily='sans-serif', pad=20)

# 添加图例
ax.legend(loc='upper right', fontsize=10)

# 调整网格线
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.xaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)
ax.yaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color='gray', linestyle='--', linewidth=0.5)

# 调整视角
ax.view_init(elev=20, azim=45)

# 设置背景颜色为白色
ax.set_facecolor('white')

# 调整布局以确保标签显示完整
plt.tight_layout()

# 保存图表
chart_path = 'E:\\岗位技能聚类三维图.png'
plt.savefig(chart_path, dpi=300, bbox_inches='tight')

# 保存聚类结果到CSV文件
result_path = 'E:\\岗位技能聚类结果.csv'
df.to_csv(result_path)

print(f"聚类结果已保存到 {result_path}")
print(f"聚类三维图表已保存到 {chart_path}")