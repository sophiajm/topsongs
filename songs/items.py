# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SongsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    artist = scrapy.Field()
    lyric = scrapy.Field()
    language = scrapy.Field()
    songlink = scrapy.Field()
    pass

class ErrorItem(scrapy.Item):
    title = scrapy.Field()
    artist = scrapy.Field()
    lyric = scrapy.Field()
    language = scrapy.Field()
    songlink = scrapy.Field()
    pass
