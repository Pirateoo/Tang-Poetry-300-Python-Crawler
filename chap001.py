import re
import requests
url = requests.get("https://so.gushiwen.cn/gushi/tangshi.aspx")
data = url.text
# print(data)
data2 = re.findall(r'<span><a href="(.*?)" target="_blank">(.*?)</a>(.*?)</span>',data)
# print(data2)
with open('gushi.txt', 'w', encoding='utf-8') as f:
    for i in data2:

        url2 = 'https://so.gushiwen.cn/'+i[0]
        data2 = requests.get(url2).text
        # print(data2)
        gushi = re.findall('name="description" content="(.*?)" /',data2)
        # print(gushi)

        # print(f'诗名：{i[1]}，作者：{i[2]}，诗句链接：https://so.gushiwen.cn/{i[0]}')
        output = f' 诗名：{i[1]}，作者：{i[2]}，古诗内容：{gushi}\n'
        f.write(output)
        print(output)

