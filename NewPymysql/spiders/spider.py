import scrapy
from NewPymysql.items import MyprojectItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["meijutt.tv"]  # 域名
    start_urls = ["https://www.meijutt.tv/new100.html"]  # 补充完整网址

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')  # 选中所有的属性class值为"top-list  fn-clear"的ul下的li标签内容
        for each_movie in movies:
            item = MyprojectItem()
            item['number'] = each_movie.xpath('.//div[@class="lasted-num fn-left"]//text()').extract()[0]  # 提取影片序号
            item['name'] = each_movie.xpath('.//h5/a//text()').extract()[0]  # 提取影片名
            item['author'] = each_movie.xpath('.//h5/a/@href').extract()[0]  # 提取影片网址
            item['crawler_time'] = \
            each_movie.xpath('.//div[@class="lasted-time new100time fn-right"]//text()').extract()[
                0]  # 提取影片更新时间
            yield item  # 一种特殊的循环




