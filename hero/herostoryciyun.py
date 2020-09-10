import jieba
import json
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from os import path

def read_hero_skin_file():
    # 读取数据
    hero_list = json.load(open("./file/heroskin.json", 'r', encoding='utf-8'))
    hero_skin_data = hero_list["hero_skin_data"]

    # 英雄名称列表
    hero_name_list = []
    for hero_story in hero_skin_data:
        hero_name_list.append(hero_story["hero_name"])

    # 英雄故事
    hero_story_list = []
    for hero_story in hero_skin_data:
        hero_story_list.append(hero_story["hero_str_story"])
    hero_story = ""
    for hero_story_item in hero_story_list:
        hero_story += hero_story_item
    # 将所有英雄故事保存到txt文件中
    with open("./file/herostory.txt", 'w', encoding="utf-8") as f:
        f.write(hero_story)
    return hero_name_list, hero_story_list


def heroWordcloud():

    hero_name_list, hero_story_list = read_hero_skin_file()
    index = 0
    while index < len(hero_name_list):
        # 分词
        texts = hero_story_list[index]
        word_list = jieba.cut(texts)
        wordcloud_text = ' '.join(word_list)
        # 图片名称
        file_name = hero_name_list[index]

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
            # mask=alice_mask,
            repeat=False,
            # 设置有多少种随机生成状态，即有多少种配色方案
            random_state=30,
            mode='RGBA'    # 设置颜色
        ).generate(wordcloud_text)

        # 保存图片
        image_path = './heroimages/' + file_name + '/' + file_name + '.png'
        wordcloud.to_file(image_path)
        print("正在绘制 英雄 %s 的词云"%file_name)

        index += 1

        # plt.imshow(wordcloud)
        # plt.axis('off')
        # plt.show()
    pass

def main():
    # 保存所有的英雄故事
    read_hero_skin_file()
    # 绘图
    heroWordcloud()
    print("所有英雄故事词云保存完成")

if __name__ == '__main__':
    main()