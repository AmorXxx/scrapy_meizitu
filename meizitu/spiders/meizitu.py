import scrapy
import os
import re


class MeizituSpider(scrapy.spiders.Spider):
    name = 'meizitu'  # 爬虫名
    allowed_domians = ["http://www.mzitu.com"]  # 允许域名列表
    start_urls = ['http://www.mzitu.com/150067']  # 起始链接列表

    def parse(self, response):
        pic_name = response.xpath('/html/body/div[2]/div[1]/h2/text()').extract()[0]
        pic_src = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract()[0]
        file_name = pic_name + '.jpg'
        folder_name = response.xpath('/html/body/div[2]/div[1]/h2/text()').extract()[0]
        base_path = os.path.join("pic", re.sub('（.*?）', '', folder_name))
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        yield scrapy.Request(pic_src, meta={'file_path': file_name, 'base_path': base_path},
                             callback=self.imageDownload)
        next_url = response.xpath('/html/body/div[2]/div[1]/div[4]/a/@href').extract()[-1]
        if next_url:
            yield scrapy.Request(next_url)

    def imageDownload(self, response):
        file_name = response.meta['file_path']
        base_path = response.meta['base_path']
        os.chdir(base_path)
        with open(file_name, 'wb') as f:
            f.write(response.body)
        os.chdir('C:\meizitu\scrapy_meizitu')
