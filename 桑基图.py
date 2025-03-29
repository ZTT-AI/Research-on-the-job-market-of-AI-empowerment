import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Sankey

# 加载数据（请替换为实际文件路径）
data_path = 'E:/职位、规模、城市.csv'
df = pd.read_csv(data_path)

# 定义节点列表
nodes = []
for job in df['Job_Title'].unique():
    nodes.append({"name": job})
for size in df['Company_Size'].unique():
    nodes.append({"name": size})
for loc in df['Location'].unique():
    nodes.append({"name": loc})

# 统计流量数据
links = []
for _, row in df.iterrows():
    job = row['Job_Title']
    size = row['Company_Size']
    loc = row['Location']
    link1 = {"source": nodes.index({"name": job}), "target": nodes.index({"name": size}), "value": 1}
    if link1 not in links:
        links.append(link1)
    else:
        links[links.index(link1)]["value"] += 1

    link2 = {"source": nodes.index({"name": size}), "target": nodes.index({"name": loc}), "value": 1}
    if link2 not in links:
        links.append(link2)
    else:
        links[links.index(link2)]["value"] += 1

# 创建桑基图，调整布局
sankey = (
    Sankey(init_opts=opts.InitOpts(width="1600px", height="800px"))  # 设置图表的宽度和高度
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.8, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="职位、规模和城市关系桑基图"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
)

# 渲染图表到 HTML 文件
sankey.render("E:/sankey_diagram_adjusted.html")