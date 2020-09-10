# 项目：英雄联盟

通过 urllib+requests+XPath+json+selenium 等模块来完成一个python爬虫数据分析程序项目，要完成的基本需求如下：

1. 获得王者荣耀官网的所有英雄信息，字段内容有英雄名称、英雄图片地址、详情链接地址等；
2. 使用 json 格式数据来保存，并将文件命名为 `hero.json`；
3. 把所有英雄头像图片都下载并保存到本地，并命名为`英雄名称.jpg`。注意：王者荣耀官网的英雄信息数据来自王者荣耀官网 https://pvp.qq.com/web201605/herolist.shtml；
4. 把各个英雄的英雄故事、英雄历史、英雄皮肤等数据保存到`heroskin.json`文件中；
5. 根据`heroskin.json`文件，把所有英雄的皮肤图片都下载并保存到本地，并命名为`皮肤名称.jpg`。注意：王者荣耀英雄的皮肤信息数据来自单个英雄点击进入的详情链接地址页面，参考上述英雄“云中君”https://pvp.qq.com/web201605/herodetail/506.shtml；
6. 分析英雄名称字数和英雄皮肤字数，制作折线图；
7. 对英雄故事进行分词，制作每个英雄故事的词云。



## 开发环境

python3.7-32

官网：https://www.python.org/



## 库

+ urllib：HTTP请求
+ os：操作文件/夹
+ lxm：操作XPath
+ json：编码和解码 JSON 对象
+ selenium：获取动态数据
+ requests：HTTP请求
+ time：处理日期和时间
+ matplotlib：绘图
+ numpy：科学计算、数据统计
+ jieba：中文分词
+ wordworld：词云



