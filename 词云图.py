import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np
from collections import Counter
from matplotlib.font_manager import FontProperties

# 读取文本文件
file_path = r'E:\Required_Skills.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print("原始文本：", text)  # 调试：打印文本内容
except Exception as e:
    print(f"读取文件失败：{e}")
    exit()

# 中文分词
text_cut = " ".join(jieba.cut(text))
print("分词结果：", text_cut)  # 调试：打印分词结果

# 统计词频
word_freq = Counter(text_cut.split())
print("词频统计：", word_freq)  # 调试：打印词频

if not word_freq:
    print("错误：没有统计到任何词语")
    exit()

# 按词频排序
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# 初始化词云对象
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    font_path=r"C:\Windows\Fonts\msyh.ttc",  # 尝试其他字体
    collocations=False,
    colormap='viridis'
)

# 生成完整的词云（固定词语位置）
full_wordcloud = wordcloud.generate_from_frequencies(word_freq)

# 获取词语布局
layout = wordcloud.layout_
print("Layout 结构：", layout)  # 调试：打印布局

if not layout:
    print("错误：词云布局为空")
    exit()

# 创建画布
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')  # 隐藏坐标轴

# 指定固定颜色，这里使用蓝色
fixed_color = 'blue'

# 创建字体属性对象
font_prop = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")

# 逐词显示并保存帧
images = []
for i in range(1, len(sorted_word_freq) + 1):
    # 取前 i 个词语
    partial_word_freq = dict(sorted_word_freq[:i])
    print(f"当前处理第 {i} 个词语：{sorted_word_freq[i - 1][0]}")  # 调试：打印当前词语

    # 清空画布
    ax.clear()
    ax.axis('off')

    # 绘制当前词语
    for item in layout:
        # 解析 layout 结构
        word_info = item[0]  # ('词语', 词频权重)
        word = word_info[0]  # 提取词语文本
        size = item[1]  # 字体大小
        position = item[2]  # (x, y)

        if word in partial_word_freq:
            x, y = position
            ax.text(x, y, word, fontsize=size, color=fixed_color, fontproperties=font_prop)

    # 将当前帧保存为图像数据
    fig.canvas.draw()  # 更新画布
    image = np.array(fig.canvas.renderer.buffer_rgba())  # 获取图像数据
    images.append(image)
    # 让每个词语停留一段时间，这里设置为停留 5 帧
    for _ in range(5):
        images.append(image)

# 添加最终完整词云图并显示 5 秒（假设帧率为 10 帧/秒）
final_image = images[-1]
for _ in range(50):  # 50 帧，每帧 0.1 秒，共 5 秒
    images.append(final_image)

# 保存为 GIF
output_path = r'C:/temp/wordcloud_animation.gif'  # 修改保存路径
imageio.mimsave(output_path, images, duration=0.1)  # 每帧 0.1 秒
print(f"动态词云图已保存到：{output_path}")