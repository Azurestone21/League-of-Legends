from selenium import webdriver
import time
import urllib.request
import json
import os

import useragenttool

def save_hero_head():
    """下载英雄头像"""
    with open('./file/hero.csv', 'r', encoding='gbk') as file:
        file_data = file.readlines()

        # 保存英雄头像的公共路径
        head_dir_path = "./heroimages/"

        # 删除表头
        del file_data[0]

        for hero_item_data in file_data:
            hero_item_data_list = hero_item_data.split(',')
            # print(hero_item_data_list)
            hero_name = hero_item_data_list[1]
            hero_image = hero_item_data_list[6]
            # print(hero_name)
            # print(hero_image)
            # 保存头像图片
            try:
                # 获取图片名字
                filename = hero_image.split("/")[-1]
                hero_dir_path = head_dir_path + hero_name + "/"

                # 判断是否存在目录
                if not os.path.exists(hero_dir_path):
                    # 如果不存在就创建
                    os.makedirs(hero_dir_path)
                if not os.path.exists(filename):
                    # 发送请求
                    response = urllib.request.urlopen(hero_image)
                    # 获取图片内容
                    content = response.read()
                    # 把图片写入文件中
                    file = open(hero_dir_path + '/' + hero_name + '.jpg', 'wb')
                    file.write(content)
                    file.close()
                    print("英雄 %s 头像图片保存成功"%hero_name)
            except IOError as e:
                print(e)
    print("所有英雄头像图片保存成功")
    pass

def main():
    save_hero_head()

if __name__ == '__main__':
    save_hero_head()