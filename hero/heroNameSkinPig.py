import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def read_file():
    # 读取数据
    hero_list = json.load(open("./file/heroskin.json", 'r', encoding='utf-8'))
    hero_skin_data = hero_list["hero_skin_data"]
    return hero_skin_data


def get_hero_name_skin_count():
    hero_skin_data = read_file()

    # 所有英雄、皮肤个数
    hero_name_list = []
    hero_skin_name = []

    for hero_skin_item in hero_skin_data:
        # 英雄名称
        temp_name = hero_skin_item["hero_name"]
        # 英雄皮肤
        temp_skin_list = hero_skin_item["skin_list"]
        # 英雄名称列表
        hero_name_list.append(temp_name)
        # 英雄皮肤
        for temp_skin_name_item in temp_skin_list:
            hero_skin_name.append(temp_skin_name_item["skin_name"])

    """计算出各个英雄名称的长度"""
    name_label_list = []
    name_count = []
    n = 0
    for hero_name in hero_name_list:
        if n < len(hero_name):
            n = len(hero_name)

    # 有多少个字的英雄名称，向列表初始化多少个0
    for i in range(n):
        name_label_list.append(str(i + 1) + "个字")
        name_count.append(0)

    # 统计各个长度的英雄名称
    for hero_name in hero_name_list:
        l = len(hero_name)
        name_count[l - 1] += 1

    """计算出所有皮肤名称的长度"""
    skin_label_list = []
    skin_count = []
    s = 0
    for skin_name in hero_skin_name:
        if s < len(skin_name):
            s = len(skin_name)

    # 有多少个字的英雄名称，向列表初始化多少个0
    for i in range(s):
        skin_label_list.append(str(i + 1) + "个字")
        skin_count.append(0)

    # 统计各个长度的皮肤名称
    for hero_name in hero_skin_name:
        l = len(hero_name)
        skin_count[l - 1] += 1

    # print(name_label_list)
    # print(name_count)
    # print(skin_label_list)
    # print(skin_count)

    return name_label_list, name_count, skin_label_list, skin_count
    pass


def drawPie():
    # 显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 显示负号
    plt.rcParams['axes.unicode_minus'] = False

    # 设置突出值
    name_explode = []
    skin_explode = []

    # 英雄数据
    name_label_list, name_count, skin_label_list, skin_count = get_hero_name_skin_count()
    m = 0
    for i in range(len(name_count)-1):
        if name_count[i] > name_count[i-1]:
            m = i
    for item in name_count:
        if item == name_count[m]:
            name_explode.append(0.1)
        else:
            name_explode.append(0)
    s = 0
    for i in range(len(skin_count)-1):
        if skin_count[i] > skin_count[i-1]:
            s = i
    for item in skin_count:
        if item == skin_count[s]:
            skin_explode.append(0.1)
        else:
            skin_explode.append(0)


    # 设置窗口展示大小
    plt.figure(figsize=(10, 8), dpi=80)

    # 饼图各部分颜色
    color1 = ["#EB7AD4", "#76BFF0", "#EFAA98", "#AA8ADC"]
    color2 = ["#EB7AD4", "#76BFF0", "#EFAA98", "#AA8ADC", "#90EE90"]

    # 多个图
    # 一行二列的第一个图
    plt.subplot(1, 2, 1)
    plt.title('王者荣耀英雄名称字数分析图', fontsize=16)
    plt.pie(name_count,
            explode=name_explode,
            colors=color1,
            labels=name_label_list,
            labeldistance=1.1,
            autopct="%1.1f%%",
            shadow=False,
            startangle=90,
            pctdistance=0.8,
            counterclock=False)
    # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.axis("equal")
    # 设置图例样式
    plt.legend(loc="upper right")

    # 一行二列的第二个图
    plt.subplot(1, 2, 2)   # 多个图
    plt.title('王者荣耀英雄皮肤字数分析图', fontsize=16)
    plt.pie(skin_count,
            explode=skin_explode,
            colors=color2,
            labels=skin_label_list,
            labeldistance=1.1,
            autopct="%1.1f%%",
            shadow=False,
            startangle=90,
            pctdistance=0.8,
            counterclock=False)
    # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.axis("equal")
    # 设置图例样式
    plt.legend(loc="upper right")
    # 显示
    plt.show()


def main():
    drawPie()

if __name__ == '__main__':
    main()