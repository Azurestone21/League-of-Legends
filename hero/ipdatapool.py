import requests
import json
import time

import useragenttool

def get_proxy():
    """获取代理IP"""
    with open('./file/ip.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # {"HTTP": "http://125.108.90.88:9000"}
    #     print(json_data[i])
    return json_data

def get_current_ip(pro):
    """验证 IP 是否可用"""
    proxy_list = []
    try:
        # 发送请求
        url = 'http://www.sohu.com'
        for ip_item in pro:
            req = requests.get(url,
                               headers=useragenttool.get_headers(),
                               proxies=ip_item)
            # 成功访问
            if req.status_code == 200:
                proxy_list.append(ip_item)
                print("%s--可用"%ip_item)
            else:
                print("%s--不可用" % ip_item)
    except Exception:
        pass
    return proxy_list

def save_to_file(proxy_list):
    """保存可用的IP到代理池"""
    # print(proxy_list)
    with open('./file/proxypool.json', 'w', encoding='utf-8') as f:
        json.dump(proxy_list, f, ensure_ascii=False, indent=4)
    # for item in proxy_list:
    #     with open('./file/proxypool.json', 'w', encoding='utf-8') as f:
    #         f.write(item['HTTP'] + '\n')
    print("所有可用的IP已保存成功")

def main():
    # 获取代理IP
    pro = get_proxy()
    # 验证 IP 是否可用
    proxy_list = get_current_ip(pro)
    # 保存可用的IP到代理池
    save_to_file(proxy_list)

if __name__ == '__main__':
    main()