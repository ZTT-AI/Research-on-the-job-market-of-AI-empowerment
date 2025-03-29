import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from community import community_louvain  # 需安装python-louvain

# 读取数据
df = pd.read_csv('E:/ai_job_market_insights.csv')

# 清洗技能字段（假设技能以逗号分隔）
df['Required_Skills'] = df['Required_Skills'].str.split(',')

# 提取唯一节点,避免节点重复
industries = df['Industry'].unique()
job_titles = df['Job_Title'].unique()
skills = list(set(skill for sublist in df['Required_Skills'] for skill in sublist))

# 创建空图
G = nx.Graph()

# 添加节点
G.add_nodes_from(industries, node_type='industry')
G.add_nodes_from(job_titles, node_type='job')
G.add_nodes_from(skills, node_type='skill')

# 定义边权重计算函数：基于指定分组的权重（频率）
def calculate_weight(df, group_col, target_col):
    return df.groupby([group_col, target_col]).size().reset_index(name='weight')

# 添加行业-职位边
industry_job_edges = calculate_weight(df, 'Industry', 'Job_Title')
for _, row in industry_job_edges.iterrows():
    G.add_edge(row['Industry'], row['Job_Title'], weight=row['weight'], edge_type='industry_job')

# 添加职位-技能边
job_skill_edges = df.explode('Required_Skills').groupby(['Job_Title', 'Required_Skills']).size().reset_index(name='weight')
for _, row in job_skill_edges.iterrows():
    G.add_edge(row['Job_Title'], row['Required_Skills'], weight=row['weight'], edge_type='job_skill')

# 添加行业-技能边（间接关联）
industry_skill_edges = df.explode('Required_Skills').groupby(['Industry', 'Required_Skills']).size().reset_index(name='weight')
for _, row in industry_skill_edges.iterrows():
    G.add_edge(row['Industry'], row['Required_Skills'], weight=row['weight'], edge_type='industry_skill')

# 转换为无向图（Louvain要求无向图）
undirected_G = G.to_undirected()

# 运行Louvain算法
partition = community_louvain.best_partition(undirected_G)

# 将社区标签添加到节点属性
nx.set_node_attributes(G, partition, 'community')

# 打印社区结果
communities = {}
for node, comm_id in partition.items():
    communities.setdefault(comm_id, []).append(node)
print(f"发现 {len(communities)} 个社区")

# 度中心性
degree_centrality = nx.degree_centrality(G)

# 介数中心性
betweenness_centrality = nx.betweenness_centrality(G, weight='weight')

# 接近中心性
closeness_centrality = nx.closeness_centrality(G)

# 聚类系数
clustering_coefficient = nx.clustering(G)

# 提取Top 10关键节点
top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
top_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print("度中心性Top 10:", top_degree)
print("介数中心性Top 10:", top_betweenness)

# 定义节点颜色（按社区）
community_colors = [plt.cm.tab20(i) for i in range(len(communities))]
colors = [community_colors[partition[node]] for node in G.nodes()]

# 定义节点大小（按度中心性）
sizes = [degree_centrality[node] * 5000 for node in G.nodes()]

# 绘制网络
plt.figure(figsize=(20, 15))
pos = nx.spring_layout(G, k=0.15, iterations=50)  # 调整k值避免重叠
nx.draw_networkx(
    G,
    pos,
    node_color=colors,
    node_size=sizes,
    cmap=plt.cm.tab20,
    with_labels=True,
    font_size=12,  # 增大字体大小
    font_color='black',  # 设置字体颜色为黑色
    font_weight='bold',  # 设置字体加粗
    edge_color='gray',
    alpha=0.6
)

# 添加图例
legend_nodes = [nx.draw_networkx_nodes(G, pos, nodelist=[communities[i][0]], node_color=[community_colors[i]], node_size=500) for i in range(len(communities))]
plt.legend(legend_nodes, [f"Community {i}" for i in range(len(communities))], loc='lower right', fontsize=12)  # 增大图例字体大小

#plt.title("行业-职位-技能复杂网络分析", fontsize=16)  # 增大标题字体大小
plt.show()
plt.savefig('E:/行业-职位-技能复杂网络分析.png') 

# 保存网络指标
centrality_data = {
    'Node': list(G.nodes()),
    'Community': [partition[node] for node in G.nodes()],
    'Degree Centrality': [degree_centrality[node] for node in G.nodes()],
    'Betweenness Centrality': [betweenness_centrality[node] for node in G.nodes()],
    'Closeness Centrality': [closeness_centrality[node] for node in G.nodes()],
    'Clustering Coefficient': [clustering_coefficient[node] for node in G.nodes()]
}

centrality_df = pd.DataFrame(centrality_data)
centrality_df.to_csv('E:/network_analysis_results.csv', index=False)

print("网络分析结果已保存到E盘根目录")

#读取数据：从CSV文件中读取数据。
#清洗技能字段：将技能字段中的字符串分割成列表。
#提取唯一节点：提取行业中的唯一节点、职位和技能。
#创建空图：创建一个空的无向图 G。
#添加节点：将行业中的唯一节点、职位和技能添加到图中。
#定义边权重计算函数：定义一个函数来计算边的权重。
#添加边：根据数据添加行业-职位边、职位-技能边和行业-技能边。
#转换为无向图：将图转换为无向图，以满足Louvain算法的要求。
#运行Louvain算法：运行Louvain算法来确定社区结构。
#将社区标签添加到节点属性：将检测到的社区标签添加到每个节点的属性中。
#计算网络指标：计算度中心性、介数中心性、接近中心性和聚类系数。
#提取Top 10关键节点：提取度中心性和介数中心性最高的前10个节点。
#定义节点颜色和大小：根据社区和度中心性定义节点颜色和大小。
#绘制网络：绘制网络图并保存为PNG文件。
#保存网络指标：将网络指标保存到CSV文件中。