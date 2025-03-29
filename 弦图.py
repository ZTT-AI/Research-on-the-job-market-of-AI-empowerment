#弦图
import pandas as pd
import holoviews as hv
from holoviews import opts

# 启用 Bokeh 后端
hv.extension('bokeh')

# 读取数据（替换为你的实际文件路径）
df = pd.read_csv(r"E:\ai_job_market_insights.csv")

# 1. 生成 Job_Title 和 Automation_Risk 的交叉表
cross_tab = pd.crosstab(df['Job_Title'], df['Automation_Risk'])

# 2. 将交叉表转换为长格式（Holoviews 需要此格式）
edges = cross_tab.stack().reset_index()
edges.columns = ['Job_Title', 'Automation_Risk', 'Count']

# 3. 生成弦图（确保数据格式正确）
chord = hv.Chord(edges, ['Job_Title', 'Automation_Risk'], ['Count'])

# 4. 设置样式，调整弦的颜色
chord.opts(
    opts.Chord(
        cmap='Category20',          # Node color map
        edge_cmap='Viridis',        # Change the edge (chord) color map
        edge_color=hv.dim('Count'), # Map the color of the edges to the 'Count' column
        labels='index',
        node_color='index',
        width=800,
        height=800,
        directed=False
    )
)


# 5. 保存为 HTML 文件（到 C 盘根目录）
hv.save(chord, r"E:\job_automation_chord.html")