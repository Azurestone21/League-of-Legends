import requests
import json
import lxml.html
import time
import os

import useragenttool

class Kuaidaili(object):
    # 初始化函数
    def __init__(self):
        self.common_url = "https://www.kuaidaili.com/free/inha/{}/"
        # json 格式
        self.ip_data = {}
        # 每页的数据
        self.page_data = []
        pass

    def get_html_data(self, page):
        """获取页面html内容"""
        url = self.common_url.format(str(page))
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url,
                                headers=useragenttool.get_headers(),
                                verify=False)
        # print(response)
        return response

    def get_ip_data(self, html_content, page):
        metree = lxml.html.etree
        parser = metree.HTML(html_content.text)

        # 获取表格数据
        # ['IP', 'PORT', '匿名度', '类型', '位置', '响应速度', '最后验证时间']
        # ['175.43.153.114', '9999', '高匿名', 'HTTP', '福建省泉州市  联通', '3秒', '2020-08-29 01:31:01']

        tbody_trs = parser.xpath('//div[@id="content"]//table/tbody/tr')
        for tr in tbody_trs:
            temp = {}
            td_texts = tr.xpath('./td/text()')
            # 拼接url   协议类型 id 端口号
            id = td_texts[0]
            port = td_texts[1]
            type = td_texts[3]
            # HTTP, HTTPS
            if ',' in type:
                type = type.split(',')[1]
            http_url = type.lower() + '://' + id + ":" + port
            # 字典类型
            temp['HTTP'] = http_url
            # 一页的ip数据
            self.page_data.append(temp)
        return self.page_data
        pass

    def save_ip_data(self, data, page):
        """保存数据到json文件"""
        ip_path = './file'
        # 创建文件夹
        if not os.path.exists(ip_path):
            os.mkdir(ip_path)
        # 提示
        print("正在保存第%s页的数据..."%page)
        # 保存
        with open('./file/ip.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        # 提示
        print("保存成功")
        pass

    def start(self):
        """开始函数"""
        # 获取到html内容
        # daili_data = self.get_html_data()
        for i in range(16, 21):
            # 获取html内容
            html_content = self.get_html_data(i)
            # 获取每页的数据
            daili_data = self.get_ip_data(html_content, i)
            # 一页的数据添加到总数据中
            self.ip_data["ip_data"] = self.page_data
            # 保存数据
            self.save_ip_data(daili_data, i)
            # 操作过快，部分数据获取不到
            time.sleep(3)
        pass

def main():
    kdl = Kuaidaili()
    kdl.start()

if __name__ == '__main__':
    main()
