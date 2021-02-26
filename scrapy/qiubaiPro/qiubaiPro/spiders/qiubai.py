# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']
#基于管道
    # def parse(self, response):
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []#存储所有解析到的数据
    #     print(div_list)
    #     for div in div_list:
    #         #xpath返回的是列表，且列表元素是Selector类型的对象
    #         #extract可以将Selector对象中data参数存储的字符串提取出来
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         #author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         #列表中调用extract表示将列表中每一个Selector对象中的data对应的字符串提取出来
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         #join（）将列表转化为字符串
    #         content = ''.join(content)

    #         dic = {
    #         'author':author,
    #         'content':content
    #         }

    #         all_data.append(dic)
    #         return all_data

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []#存储所有解析到的数据
        for div in div_list:
            #xpath返回的是列表，且列表元素是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            #列表中调用extract表示将列表中每一个Selector对象中的data对应的字符串提取出来
            content = div.xpath('./a[1]/div/span//text()').extract()
            #join（）将列表转化为字符串
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item #将item提交给管道