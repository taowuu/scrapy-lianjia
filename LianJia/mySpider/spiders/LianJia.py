# 爬虫逻辑
import scrapy

from LianJia.mySpider.items import MyspiderItem


class LianJia(scrapy.Spider):
    name = 'LianJia'
    start_urls = ['http://sz.lianjia.com/ershoufang/']

    def parse(self, response):
        ls = response.xpath("//ul[@class='sellListContent']//li")
        for i in ls:
            href = i.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=href, callback=self.helper)

    @staticmethod
    def helper(response):
        item = MyspiderItem()

        item['href'] = response.url
        title = response.xpath("//div[@class='title']//h1[@class='main']/text()").extract_first()
        item['title'] = title
        total = str(response.xpath("//div[@class='price-container']//span[@class='total']/text()").extract_first()) + str(response.xpath("//div[@class='price-container']//span[@class='unit']/span/text()").extract_first())
        item['total'] = total if total != 'NoneNone' else '暂无数据'
        unit_price = response.xpath("//div[@class='price-container']//span[@class='unitPriceValue']//text()").extract()
        item['unit_price'] = ''.join(unit_price) if ''.join(unit_price) != '' else '暂无数据'
        room_type = response.xpath("//div[@class='houseInfo']//div[@class='mainInfo']/text()").extract_first()
        item['room_type'] = room_type
        floors = response.xpath("//div[@class='houseInfo']//div[@class='subInfo']/text()").extract_first()
        item['floors'] = floors
        area = response.xpath("//div[@class='area']//div[@class='mainInfo']/text()").extract_first()
        item['area'] = area
        community = response.xpath("//div[@class='aroundInfo']//div[@class='communityName']/a/text()").extract_first()
        item['community'] = community
        address = response.xpath("//div[@class='aroundInfo']//div[@class='areaName']/span[@class='info']//text()").extract()
        item['address'] = ''.join(address)
        mediator = response.xpath("//div[@class='ke-agent-sj-info']/a/text()").extract_first().strip()
        item['mediator'] = mediator
        phone = response.xpath("//div[@class='ke-agent-sj-phone ']//text()").extract()
        item['phone'] = ''.join(phone).strip()

        yield item
