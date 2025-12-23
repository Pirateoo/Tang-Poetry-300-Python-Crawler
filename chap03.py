import pandas as pd
from collections import Counter
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取data.txt文件
input_file = "data.txt"
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 解析数据
poems = []
for line in lines:
    parts = line.strip().split()
    if len(parts) == 4:
        poem_type = parts[0]
        poem_title = parts[1]
        poem_author = parts[-1]
        poem_content = " ".join(parts[2:-1])
        poems.append({
            "诗类型": poem_type,
            "诗题目": poem_title,
            "诗内容": poem_content,
            "诗作者": poem_author
        })

# 创建DataFrame
df = pd.DataFrame(poems)

# 统计每种诗类型的诗数量
poem_type_counts = df["诗类型"].value_counts()
poem_type_counts_df = pd.DataFrame(poem_type_counts).reset_index()
poem_type_counts_df.columns = ["诗类型", "数量"]

# 保存诗类型统计结果到Excel文件
poem_type_counts_df.to_excel("poem_type_counts.xlsx", index=False)

# 统计每个作者的诗数量
author_counts = df["诗作者"].value_counts()
author_counts_df = pd.DataFrame(author_counts).reset_index()
author_counts_df.columns = ["诗作者", "数量"]

# 保存作者统计结果到Excel文件
author_counts_df.to_excel("author_counts.xlsx", index=False)

# 对诗内容进行中文分词
all_poem_content = " ".join(df["诗内容"])
words = jieba.lcut(all_poem_content)
words_joined = " ".join(words)

# 生成词云图
wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate(words_joined)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存词云图到文件
wordcloud.to_file("poem_wordcloud.png")
