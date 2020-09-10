import json
import numpy as np
import matplotlib.pyplot as plt

def read_file():
    # 读取数据
    hero_list = json.load(open("./file/heroskin.json", 'r', encoding='utf-8'))
    hero_skin_data = hero_list["hero_skin_data"]
    return hero_skin_data

def get_hero_skin_count():
    hero_skin_data = read_file()

    # 所有英雄、皮肤个数
    hero_name_list = []
    hero_skin_count = []

    for hero_skin_item in hero_skin_data:
        temp_name = hero_skin_item["hero_name"]
        temp_skin_count = hero_skin_item["hero_skin_count"]
        hero_name_list.append(temp_name)
        hero_skin_count.append(temp_skin_count)
    return hero_name_list, hero_skin_count
    pass

def drawLine():
    # 显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 显示负号
    plt.rcParams['axes.unicode_minus'] = False

    # 英雄数据
    hero_name_list, hero_skin_count = get_hero_skin_count()
    # 设置坐标数据 数组
    x_text = hero_name_list
    y_text = hero_skin_count

    # 设置窗口展示大小
    plt.figure(figsize=(20, 8), dpi=80)

    # 显示网格
    plt.grid(True, linestyle="--", color='gray', linewidth='0.5', axis='both')

    # 标题
    plt.title('英雄皮肤数据折线图')
    # 设置坐标轴名称
    plt.xlabel('英雄名称')
    plt.ylabel('皮肤数量')

    # 设置x轴文字角度
    plt.xticks(rotation=60, fontsize=9)

    # 设置间隔
    plt.xlim(-0.5, 100)

    # 柱形图
    bar = plt.bar(x=x_text, height=y_text, color='steelblue', alpha=0.8)

    # 折线图
    line = plt.plot(x_text,  y_text, color='red', linewidth=1, marker='o', markerfacecolor='salmon', markersize=3)
    # 设置数字标签
    for x, y in zip(x_text, y_text):
        plt.text(x, y, y, ha='center', va='bottom', fontsize=10)

    # 设置图例样式
    plt.legend(line, ("英雄皮肤数量",), loc='upper left')

    # 设置平均线
    avg = np.mean(y_text)
    plt.axhline(y=avg, color="green")

    # 显示
    plt.show()

def main():
    drawLine()

if __name__ == '__main__':
    main()