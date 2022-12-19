# 数据字段
import scrapy


class MyspiderItem(scrapy.Item):
    href = scrapy.Field()
    title = scrapy.Field()
    total = scrapy.Field()
    unit_price = scrapy.Field()
    room_type = scrapy.Field()
    floors = scrapy.Field()
    area = scrapy.Field()
    community = scrapy.Field()
    address = scrapy.Field()
    # 中介
    mediator = scrapy.Field()
    phone = scrapy.Field()
