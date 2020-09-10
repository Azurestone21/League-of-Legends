import json
import random

def read_ip_data_file():
    """所有IP数据"""
    file = open("./file/proxypool.json", 'r')
    ip_datas = json.load(file)
    return ip_datas

def get_proxies():
    # 获取批量的IP代理数据
    proxy_datas = read_ip_data_file()
    # 动态获取
    index = random.randint(0, len(proxy_datas)-1)
    return proxy_datas[index]

if __name__ == '__main__':
    proxy = get_proxies()
    print("IP代理：", proxy)