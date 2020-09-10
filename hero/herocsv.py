import urllib.request
import json

import useragenttool

def parse_index_http_url(url, decode="utf-8"):
    """解析首页，获取源码数据内容"""
    # 隐藏身份
    request_obj = urllib.request.Request(url, headers=useragenttool.get_headers())
    # 发送请求
    response = urllib.request.urlopen(request_obj)
    # 源码
    # 编码模式查看网页源码head中的meta中的charset
    hero_html_content = response.read().decode(decode)
    return hero_html_content


def catch_hero_data(hero_json_data):
    """抓取所有英雄数据"""
    # 获取英雄json文件url
    hero_http_url = "https://pvp.qq.com/web201605/js/herolist.json"

    # 爬取url数据
    data = hero_json_data

    # 所有英雄的数据列表
    all_hero_data = []

    # 获取英雄列表
    all_hero_json = json.loads(data)
    for hero_item_data in all_hero_json:
        temp = []
        hero_ename = str(hero_item_data['ename'])
        hero_name = hero_item_data['cname']
        hero_title = hero_item_data['title']
        hero_new_type = str(hero_item_data['new_type'])
        hero_type = str(hero_item_data['hero_type'])
        hero_skin_name = hero_item_data.get('skin_name') or ""
        hero_image = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/' + hero_ename + '/' + hero_ename + '.jpg'
        hero_detail_url = 'https://pvp.qq.com/web201605/herodetail/' + hero_ename + '.shtml'
        # 处理英雄类型
        if hero_type == '1':
            hero_type = "战士"
        elif hero_type == '2':
            hero_type = "法师"
        elif hero_type == '3':
            hero_type = "坦克"
        elif hero_type == '4':
            hero_type = "刺客"
        elif hero_type == '5':
            hero_type = "射手"
        elif hero_type == '6':
            hero_type = "辅助"
        else:
            hero_type = "战士"
        temp.append(hero_ename)
        temp.append(hero_name)
        temp.append(hero_title)
        temp.append(hero_new_type)
        temp.append(hero_type)
        temp.append(hero_skin_name)
        temp.append(hero_image)
        temp.append(hero_detail_url)
        all_hero_data.insert(0, temp)
    # print(all_hero_data)
    return all_hero_data

def save_hero_data(all_hero_data):
    # 所有英雄数据
    data = all_hero_data

    # 表头
    hero_list_title = ['英雄ID', '英雄名称', '英雄称号', '新类型', '英雄类型', '英雄皮肤', '英雄头像页面', '英雄详情页面']
    # 备份
    csv_file_data = data[:]
    # 添加表头
    csv_file_data.insert(0, hero_list_title)
    # 保存到csv文件
    csv_file = open('./file/hero.csv', 'w', encoding='GBK')
    for item in csv_file_data:
        text = ','.join(item)
        csv_file.write(text + '\n')
    csv_file.close()
    print("英雄数据保存成功")


def main():
    # 获取英雄json文件url
    hero_http_url = "https://pvp.qq.com/web201605/js/herolist.json"
    # 爬取url数据
    hero_json_data = parse_index_http_url(hero_http_url)
    # 所有英雄数据
    all_hero_data = catch_hero_data(hero_json_data)
    # 保存数据到csv文件
    save_hero_data(all_hero_data)


if __name__ == '__main__':
    save_hero_data()