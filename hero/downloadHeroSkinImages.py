import time
import json
import os
import requests

import useragenttool
import proxytool

def download_hero_skin():
    """下载皮肤"""
    with open('./file/heroskin.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

        # 皮肤公共存储路径
        skin_dir_path = "./heroimages/"

        for hero_skin_data in json_data['hero_skin_data']:
            # 获取英雄名称 用于创建文件夹
            hero_name = hero_skin_data['hero_name']
            hero_skin_path = skin_dir_path + hero_name + "/"

            for hero_skin_list in hero_skin_data['skin_list']:
                # 获取英雄皮肤名称和地址
                skin_name = hero_skin_list['skin_name']
                skin_image_url = hero_skin_list['skin_image_url']

                # 下载的皮肤名称
                filename = skin_name

                # 创建文件夹
                if not os.path.exists(hero_skin_path):
                    # 如果不存在就创建
                    os.mkdir(hero_skin_path)
                # 下载英雄皮肤
                if not os.path.exists(filename):
                    # 隐藏身份
                    req = requests.get(skin_image_url,
                                       headers=useragenttool.get_headers(),
                                       proxies=proxytool.get_proxies())
                    # 获取图片内容
                    image = req.content

                    # 把图片写入文件中
                    file = open(hero_skin_path + '/' + filename + '.jpg', 'wb')
                    file.write(image)
                    file.close()
                    print("%s--%s皮肤保存成功"%(hero_name,skin_name))
            print("%s的皮肤保存完成"%hero_name)
            time.sleep(3)
        print("所有皮肤保存完成")
    pass

def main():
    download_hero_skin()

if __name__ == '__main__':
    main()