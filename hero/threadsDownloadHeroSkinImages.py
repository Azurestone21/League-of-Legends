import requests
import json
from queue import Queue
from threading import Thread
import os
import multiprocessing as mp
import time

from day6.test import useragenttool
from day6.test import proxytool

class SkinImageSpider(object):
    def __init__(self):
        # 队列：存放单个英雄数据
        manager = mp.Manager()
        self.read_queue = manager.Queue()
        self.download_queue = manager.Queue()
        pass

    def read_file(self):
        # 读取数据
        hero_list = json.load(open("./file/heroskin.json", 'r', encoding='utf-8'))
        hero_skin_data = hero_list["hero_skin_data"]
        self.skin_data = hero_skin_data
        # 遍历处理
        for hero_element in hero_skin_data:
            # 发送数据
            self.read_queue.put(hero_element)

    def download_image(self):
        while True:
            # 获取到数据集  --单个英雄
            hero_item = self.read_queue.get()
            # 英雄名称、皮肤列表（皮肤名称、皮肤地址）
            hero_name = hero_item["hero_name"]
            # 获取列表
            skin_list = hero_item.get("skin_list")
            skin_name = ""
            # 下载图片
            for skin in skin_list:
                # 下一步
                item = []
                # 皮肤名称
                skin_name = skin["skin_name"]
                # 皮肤地址
                skin_url = skin["skin_image_url"]
                print("正在下载英雄 %s 的皮肤：%s"%(hero_name, skin_name))
                # 发送请求，获取结果
                response = requests.get(skin_url,
                                        headers=useragenttool.get_headers(),
                                        proxies=proxytool.get_proxies())
                # 图片
                image_content = response.content
                # 英雄名称、皮肤名称、图片
                item.append(hero_name)
                item.append(skin_name)
                item.append(image_content)
                # 设定到队列
                self.download_queue.put(item)
            # 关闭队列
            self.read_queue.task_done()
        pass

    def save_image_file(self):
        while True:
            # 获取数据   英雄名称、皮肤名称、图片
            skin_item = self.download_queue.get()
            # ./heroimages/英雄名称/皮肤名称.jpg
            hero_name = skin_item[0]
            skin_name = skin_item[1]
            image = skin_item[2]

            # 文件夹名
            hero_skin_path = "./heroimages/" + hero_name + "/"

            # 文件名
            filename = skin_name

            # 创建文件夹
            if not os.path.exists(hero_skin_path):
                # 如果不存在就创建
                os.mkdir(hero_skin_path)
            # 下载英雄皮肤
            if not os.path.exists(filename):
                # 把图片写入文件中
                file = open(hero_skin_path + '/' + filename + '.jpg', 'wb')
                file.write(image)
                file.close()
            # 提示
            print("正在保存英雄 %s 的皮肤：%s" % (hero_name, skin_name))

            # 关闭
            self.download_queue.task_done()
        pass

    def run(self):
        # 存放线程的列表
        thread_list = []

        # 读取线程，专门用于读取文件
        read_thread = Thread(target=self.read_file)
        # thread_list.append(read_thread)
        read_thread.start()
        read_thread.join()

        # 获取并下载图片的线程，获取数据、下载图片并获取图片内容
        download_thread = Thread(target=self.download_image)
        thread_list.append(download_thread)

        # 保存图片文件的线程，保存文件
        save_thread = Thread(target=self.save_image_file)
        thread_list.append(save_thread)

        # 启动线程
        for temp_thread in thread_list:
            # 线程设定为守护线程
            temp_thread.setDaemon(True)
            temp_thread.start()

        # 启动队列
        for temp_queue in [self.read_queue, self.download_queue]:
            temp_queue.join()
        pass

def main():
    spider = SkinImageSpider()
    # start_time = time.time()
    spider.run()
    # end_time = time.time()
    # print(end_time - start_time)

if __name__ == '__main__':
    main()
