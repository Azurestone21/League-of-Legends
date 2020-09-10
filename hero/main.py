"""
    项目程序入口
"""
import herocsv
import downloadHeroHeadImage
import heroskinjson
import ipdaili
import ipdatapool
import downloadHeroSkinImages
import heroSkinLine
import heroNameSkinPig
import herostoryciyun
import heroallstoryciyun

def main():
    # 获取所有英雄数据、保存到csv文件中
    # herocsv.main()
    # 下载英雄头像
    # downloadHeroHeadImage.main()
    # 爬取所有皮肤数据
    # heroskinjson.main()
    # 制作代理池
    # ipdaili.main()
    # ipdatapool.main()
    # 下载皮肤图片
    downloadHeroSkinImages.main()
    # 绘制分析图
    # 英雄皮肤折线图
    heroSkinLine.main()
    # 英雄名称皮肤饼图
    heroNameSkinPig.main()
    # 绘制并保存各个英雄故事词云
    herostoryciyun.main()
    # 绘制所有英雄故事词云
    heroallstoryciyun.main()

if __name__ == '__main__':
    main()