import scrapy

from ..items import ImdbItem


class QuotesSpider(scrapy.Spider):
    name = "imdb"
    page_number = 2
    start_urls = ["https://www.imdb.com/list/ls061697854"]

    def parse(self, response):
        items = ImdbItem()
        title = response.css(".lister-item-header a::text").extract()
        yearReleased = response.css(".text-muted.unbold::text").extract()
        rating = response.css(
            ".ipl-rating-star.small .ipl-rating-star__rating::text"
        ).extract()
        votes = response.css(".text-muted+ span:nth-child(2)::text").extract()
        totalGross = response.css(
            ".text-muted .ghost~ .text-muted+ span::text"
        ).extract()
        imageURL = response.css("#main .loadlate::attr(loadlate)").extract()
        genre = response.css(".genre::text").extract()

        items["title"] = title
        items["yearReleased"] = yearReleased
        items["rating"] = rating
        items["votes"] = votes
        items["totalGross"] = totalGross
        items["imageURL"] = imageURL
        items["genre"] = genre

        yield items

        next_page = "https://www.imdb.com/list/ls061697854/?page=" + str(
            QuotesSpider.page_number
        )
        if QuotesSpider.page_number < 32:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
