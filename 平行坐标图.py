import pandas as pd
import plotly.express as px
import plotly.io as pio

# 读取数据集
df = pd.read_csv(r'E:/ai_job_market_insights.csv')

# 将分类变量转为数值编码
df['Automation_Risk_encoded'] = df['Automation_Risk'].astype('category').cat.codes
df['AI_Adoption_Level_encoded'] = df['AI_Adoption_Level'].astype('category').cat.codes

# 创建热力图
fig = px.density_heatmap(
    df,
    x='Automation_Risk',  # X 轴为自动化风险
    y='AI_Adoption_Level',  # Y 轴为 AI 采用水平
    z='Salary_USD',  # 颜色映射为薪资
    histfunc='avg',  # 使用平均值来聚合薪资
    color_continuous_scale='Viridis',  # 颜色方案
    title='热力图：薪资、自动化风险与人工智能采用水平'
)

# 显示图表
fig.show()

# 保存图片到 E 盘根目录
try:
    pio.write_image(fig, 'E:/heatmap.png')
    print("图片已成功保存到 E 盘根目录，文件名为 heatmap.png")
except Exception as e:
    print(f"保存图片时出现错误：{e}")