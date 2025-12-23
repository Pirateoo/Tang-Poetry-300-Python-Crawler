import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 读取data.txt文件
input_file = "data.txt"
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 解析数据
poems = []
for line in lines:
    parts = line.strip().split(' ')
    if len(parts)== 4:
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

# 提取诗内容
poem_texts = [poem["诗内容"] for poem in poems]

# 计算TF-IDF值
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(poem_texts)
tfidf_array = tfidf_matrix.toarray()

# 获取词汇表
vocab = vectorizer.get_feature_names_out()

# 将结果保存为txt文件
output_file = "poems_tfidf.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for i, poem in enumerate(poems):
        tfidf_values = " ".join(map(str, tfidf_array[i]))
        line = f'{poem["诗类型"]}\t{poem["诗题目"]}\t{poem["诗内容"]}\t{poem["诗作者"]}\t{tfidf_values}\n'
        f.write(line)

print(f"TF-IDF值已保存到 {output_file}")
