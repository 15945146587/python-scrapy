# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from pymysql.converters import escape_string
class NewpymysqlPipeline:
    # 初始化
    def __init__(self, dbpool):

        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)     # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.insert, item)  # 调用插入的方法
        query.addErrback(self.error, item, spider)
        return item

    # 写入数据库
    def insert(self, db, item):
        sql = "INSERT INTO crawler_data(crawler_name,crawler_author,crawler_time,number) VALUES(%s,%s,%s,%s)"
        params = (item['name'], item['author'], item['crawler_time'],item['number'])

        db.execute(sql, params)


    # 错误处理方法
    def error(self, failue, item, spider):
        print(failue)
