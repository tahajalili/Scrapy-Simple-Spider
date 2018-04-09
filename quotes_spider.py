# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log('visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'Quote': quote.css('span.text::text')[0].extract(),
                'author_name': quote.css('small.author::text')[0].extract(),
                'Tag': quote.css('a.tag::text').extract(),
            }
            yield item

        #next page url
        next_page_url = response.css('li.next > a::attr(href)')[0].extract()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        


                

