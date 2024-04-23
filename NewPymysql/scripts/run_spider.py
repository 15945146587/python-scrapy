from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from NewPymysql.spiders.spider import SpiderSpider  # 你的spider

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

# 'Spider'是爬虫名称
runner.crawl(SpiderSpider)
runner.join().addBoth(lambda _: reactor.stop())  # 当爬虫结束，停止reactor
reactor.run()  # 开始reactor，同时运行爬虫