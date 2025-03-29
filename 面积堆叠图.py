import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 数据
data = {
    'Job Title': ['AI Researcher', 'Cybersecurity Analyst', 'Data Scientist', 'HR Manager', 'Marketing Specialist', 'Operations Manager', 'Product Manager', 'Sales Manager', 'Software Engineer', 'UX Designer'],
    'Berlin': [2.00, 2.43, 2.71, 2.40, 1.67, 1.86, 2.50, 1.80, 2.50, 1.33],
    'Dubai': [2.00, 1.56, 2.33, 1.75, 2.00, 2.00, 1.00, 1.67, 1.60, 2.00],
    'London': [2.33, 1.88, 2.20, 2.25, 1.50, 2.00, 2.33, 1.50, 1.67, 1.00],
    'New York': [2.00, 2.00, 1.62, 2.00, 2.50, 1.75, 2.50, 2.00, 2.40, 1.71],
    'Paris': [2.20, 2.25, 1.75, 1.75, 1.83, 2.50, 2.25, 2.60, 1.75, 1.57],
    'San Francisco': [2.00, 2.00, 1.17, 2.00, 2.00, 1.86, 2.33, 1.60, 1.67, 1.60],
    'Sydney': [2.00, 2.33, 2.20, 2.00, 2.33, 2.25, 1.67, 1.57, 2.00, 1.83],
    'Tokyo': [1.60, 2.00, 2.12, 2.00, 2.00, 1.00, 1.80, 2.20, 2.00, 2.00],
    'Toronto': [1.86, 2.33, 2.00, 2.40, 3.00, 3.00, 1.80, 2.33, 1.20, 2.75]
}

df = pd.DataFrame(data)

# 折线图
plt.figure(figsize=(12, 8))
for city in df.columns[1:]:
    plt.plot(df['Job Title'], df[city], marker='o', label=city)

plt.title('Average Company Size by Job Title and Location (Line Plot)')
plt.xlabel('Job Title')
plt.ylabel('Average Company Size')
plt.xticks(rotation=45)  # 设置横轴标签的倾斜角度为45度
plt.legend()
plt.grid(True)
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.savefig('E:/line_plot.png')  # 保存折线图
plt.show()

# 面积堆叠图
cities = ['London', 'Berlin', 'Toronto']
plt.figure(figsize=(12, 8))

# 计算累计公司规模
bottom = np.zeros(len(df['Job Title']))
for city in cities:
    plt.fill_between(df['Job Title'], df[city], bottom, label=city, alpha=0.5)
    bottom += df[city]

plt.title('Average Company Size by Job Title and Location (Stacked Area Plot)')
plt.xlabel('Job Title')
plt.ylabel('Average Company Size')
plt.xticks(rotation=45)  # 设置横轴标签的倾斜角度为45度
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.savefig('E:/stacked_area_plot.png')  # 保存面积堆叠图
plt.show()