# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    yearReleased = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()
    totalGross = scrapy.Field()
    imageURL = scrapy.Field()
    genre = scrapy.Field()
