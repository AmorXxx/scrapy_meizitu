import scrapy
from meizitu.items import MeizituItem
import os


class MeizituSpider(scrapy.spiders.Spider):
    name = 'meizitu'  # 爬虫名
    allowed_domians = ["http://www.mzitu.com"]  # 允许域名列表
    start_urls = ['http://www.mzitu.com/150001']  # 起始链接列表

    def parse(self, response):
        pic_name = response.xpath('/html/body/div[2]/div[1]/h2/text()').extract()[0]
        pic_src = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract()[0]
        file_path = pic_name + '.jpg'
        yield scrapy.Request(pic_src, meta={'file_path': file_path}, callback=self.imageDownload)
        next_url = response.xpath('/html/body/div[2]/div[1]/div[4]/a/@href').extract()[-1]
        if next_url:
           yield scrapy.Request(next_url)

    def imageDownload(self, response):
            file_path = response.meta['file_path']
            with open(file_path, 'wb') as f:
                f.write(response.body)