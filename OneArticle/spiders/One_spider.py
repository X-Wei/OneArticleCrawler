# -*- coding: utf-8 -*-
from OneArticle.items import OnearticleItem
import scrapy
import re

class OneSpider(scrapy.spider.Spider):
    name = "one_spider"
    allowed_domains = ["wufazhuce.com"]
    start_urls = [
        "http://wufazhuce.com/one/vol.%d#articulo"%i for i in range(1,924)
    ]

    def parse(self, response):
        nb = re.findall('\d+',response.url)[0]
        title_path = '//*[@id="tab-articulo"]/div/h2/text()' 
        author_path = '//*[@id="tab-articulo"]/div/p/text()' 
        #~ content_path = '//div[@class="articulo-contenido"]/p/text()' 
        content_path = '//div[@class="articulo-contenido"]/descendant-or-self::text()' 
        title = response.xpath(title_path).extract()[0].strip()
        author = response.xpath(author_path).extract()[0].strip()
        content = '\n'.join(  response.xpath(content_path).extract()   ).strip()
        if len(content)==0:
            with open('log.txt','a+') as flog:
                flog.write(nb+'\t')
            #~ raise Exception('null content!'+nb)
        else:
            print nb,title,author
            item = OnearticleItem()
            item['vol'] = nb
            item['title'] = title
            item['author'] = author
            item['content'] = content
            return item
        #~ yield item

