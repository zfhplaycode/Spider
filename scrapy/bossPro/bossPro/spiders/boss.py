# -*- coding: utf-8 -*-
import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
	name = 'boss'
	#allowed_domains = ['www.xxx.com']
	start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=']

	def parse_detail(self, response):
		item = response.meta['item']

		job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()').extract()
		job_desc = ''.join(job_desc)
		
		item['job_desc'] = job_desc

		yield item
	def parse(self, response):
		#匹配不到这个xpa
		li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
		print(li_list)
		for li in li_list:
			print(li)
			item = BossproItem()
			job_name = li.xpath('.//div[@class="info-primary"]/div/div/div/span/a/text()').extract_first()
			print(job_name)
			detail_url = 'https://www.zhipin.com' + li.xpath('./div/div/div/div/div/span/a/@href')
			item['job_name'] = job_name
			#对详情页发请求获取详情页的页面源码数据
			#手动请求发送
			#请求传参，通过meta={}，可以将meta字典传递给请求对应的回调函数
			yield scrapy.Request(detail_url, callback=parse_detail, meta={'item':item})