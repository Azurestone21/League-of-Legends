from selenium import webdriver
import time
import lxml.html
import json
import os
import urllib.request

import useragenttool


def read_hero_file_csv():
    """读取英雄数据文件内容"""
    hero_list = []
    path = './file/hero.csv'
    hero_file = open(path, 'r', encoding="gbk")
    hero_lines = hero_file.readlines()[1:]
    for hero_element in hero_lines:
        hero = hero_element[:-1]
        # print(hero)
        temp = hero.split(',')
        hero_item = {}
        # 获取英雄名称、英雄详情地址
        hero_item["hero_name"] = temp[1]
        hero_item["detail_url"] = temp[7]
        # print(hero_item)
        hero_list.append(hero_item)
    # print(hero_list)
    return hero_list

def catch_hero_skin_list(hero_csv_data):
    """发送请求，获取数据"""
    chrome_path = r"D:\PythonTools\GeckoDriver\chromedriver.exe"

    # 获取英雄数据 英雄名称、英雄详情地址
    data = hero_csv_data

    # 存放英雄皮肤信息列表
    hero_skin_list = []
    # 遍历
    for hero_element in data:
        # {'hero_name': '阿古朵', 'detail_url': 'https://pvp.qq.com/web201605/herodetail/533.shtml'}
        hero_name = hero_element['hero_name']
        detail_url = hero_element['detail_url']
        # 提示
        print("正在爬取英雄---%s---的皮肤数据"%hero_name)
        # 浏览器获取数据
        browser = webdriver.Chrome(chrome_path)
        browser.maximize_window()
        browser.get(detail_url)
        # 延时
        time.sleep(3)

        # XPath 加载数据内容
        # 批量获取英雄皮肤标签
        li_list = browser.find_elements_by_xpath("//div[@class='pic-pf']/ul[@class='pic-pf-list pic-pf-list3']/li")

        # 单个英雄 json
        hero_item = {}
        # 单个英雄 json 添加名称、皮肤个数
        hero_item["hero_name"] = hero_name
        hero_item["hero_skin_count"] = len(li_list)

        # 源码
        hero_html_content = browser.page_source
        parser = lxml.html.etree.HTML(hero_html_content)

        # 获取 英雄故事
        # hero_story = parser.xpath("//div[@class='pop-story']/div[@class='pop-bd']/p//text()")
        hero_story = parser.xpath("//div[@class='pop-story']/div[@class='pop-bd']//text()")
        # print(hero_story)
        # 遍历
        hero_str_story = ""
        for temp in hero_story:
            # 去除空格
            temp = temp.strip()
            hero_str_story += temp
        # print(hero_str_story)
        hero_item["hero_str_story"] = hero_str_story

        # 获取 历史中的ta
        hero_history = parser.xpath("//div[@id='history']/div[@class='pop-bd']//text()")
        # print(hero_history)
        # 遍历
        hero_str_history = ""
        for temp in hero_history:
            # 去除空格
            temp = temp.strip()
            hero_str_history += temp
        # print(hero_str_history)
        hero_str_history = hero_str_history if hero_str_history != "" else "暂无数据"
        hero_item["hero_str_history"] = hero_str_history

        # 皮肤数据列表
        skin_list = []
        # 遍历
        for li_element in li_list:
            skin_item = {}
            # 皮肤名称
            skin_item["skin_name"] = li_element.find_element_by_xpath('./p').text
            # 皮肤地址
            skin_item["skin_image_url"] = 'http:' + li_element.find_element_by_xpath(".//img").get_attribute("data-imgname")

            # {'skin_name': '山林之子', 'skin_image_url': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/533/533-bigskin-1.jpg'}
            #print(skin_item)

            skin_list.append(skin_item)

        # 将 英雄皮肤 添加到 单个英雄 json 中
        hero_item["skin_list"] = skin_list
        # print(hero_item)
        # 将 英雄皮肤 添加到 单个英雄 json 中
        hero_skin_list.append(hero_item)
        browser.quit()
    # print(hero_skin_list)
    return hero_skin_list

def save_hero_skin_data(hero_skin_list):
    """保存数据到json"""
    ''' 
    {
        'hero_name': '阿古朵', 
        'hero_skin_count': 2, 
        'hero_str_story': '...(省略)', 
        'hero_str_history': '暂无数据', 
        'skin_list': [
            {
                'skin_name': '山林之子', 
                'skin_image_url': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/533/533-bigskin-1.jpg'
            }, {
                'skin_name': '熊喵少女', 
                'skin_image_url': 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/533/533-bigskin-2.jpg'
            }
        ]
    }
    '''
    # 英雄皮肤数据
    data = hero_skin_list

    hero_data = {}
    hero_data["hero_skin_data"] = data
    with open('./file/heroskin.json', 'w', encoding='utf-8') as f:
        json.dump(hero_data, f, ensure_ascii=False, indent=4)
    print("所有皮肤数据保存成功")

def main():
    # 读取文件数据
    hero_csv_data = read_hero_file_csv()
    # 发送请求，获取数据（英雄名称、英雄皮肤个数、英雄皮肤、英雄故事、英雄历史）
    hero_skin_list = catch_hero_skin_list(hero_csv_data)
    # 保存数据到json
    save_hero_skin_data(hero_skin_list)

if __name__ == '__main__':
    save_hero_skin_data()