import jieba
import json
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from os import path

def hero_story_cipin():
    txt = open("./file/herostory.txt", "r", encoding="utf-8").read()
    # jieba 分词
    ls = jieba.lcut(txt)
    # 保存 词 次数
    counts = {}
    for word in ls:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 词
    word_list = []
    # 次数
    count_text = []
    # 获取数据
    word_counts = hero_story_cipin()
    items = list(word_counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(100):
        word, count = items[i]
        word_list.append(word)
        count_text.append(count)
        print("{0:<10}{1:>4}".format(word, count))
    return word_list, count_text
    pass

def wordcloud():
    # 导入一个文本文件
    text = open('./file/herostory.txt', 'r', encoding='utf-8')
    story_text = list(text)

    # 对 story_text 进行遍历,并将其做分词切割后做成列表
    word_list = [''.join(jieba.cut(sentence)) for sentence in story_text]
    # 将word_list内的元素用空格连接起来，以便于计算词频
    wordcloud_text = ''.join(word_list)

    # 当前文件路径
    d = path.dirname(__file__)
    # PIL导入图片
    image = Image.open(path.join(d, 'file/tuxing.jpg'))
    # 背景图
    alice_mask = np.array(image)
    # 设置词云的属性
    wordcloud = WordCloud(
        # 设置背景色
        background_color='white',
        # 设置背景宽
        width=500,
        # 设置背景高
        height=350,
        # 最大字体
        max_font_size=50,
        # 最小字体
        min_font_size=10,
        # 字体
        font_path='simhei.ttf',
        # 背景图
        mask=alice_mask,
        repeat=False,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    ).generate(wordcloud_text)

    # 保存图片
    image_path = './file/allherostoryciyun.png'
    wordcloud.to_file(image_path)
    print("绘制词云完成")

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    pass

def main():
    # 分词
    # hero_story_cipin()
    # 绘图
    wordcloud()

if __name__ == '__main__':
    main()