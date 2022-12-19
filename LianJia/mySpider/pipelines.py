# spider 生命周期
import pymysql


# 测试数据
class MyspiderPipeline:
    @staticmethod
    def process_item(item):
        print(item['href'])
        print(item['title'])
        print(item['total'])
        print(item['unit_price'])
        print(item['room_type'])
        print(item['floors'])
        print(item['area'])
        print(item['community'])
        print(item['address'])
        print(item['mediator'])
        print(item['phone'])
        print('----------------------')
        return item


# 保存到数据库
class DBPipeLine:
    def open_spider(self, spider):
        try:
            self.conn = pymysql.connect(host='localhost', user='root', passwd='root', db='test')
            print('连接到数据库')
        except:
            print('连接数据库失败')
        try:
            self.conn.cursor().execute('create table lianjia(href varchar(300),title varchar(100),total varchar(16),unitPrice varchar(20),room_type varchar(20),floors varchar(20),area varchar(20),community varchar(20),address varchar(20),mediator varchar(20),phone varchar(20))')
            print('建表成功')
        except:
            print('先删除表')
            self.conn.cursor().execute('drop table lianjia')
            self.conn.cursor().execute('create table lianjia(href varchar(300),title varchar(100),total varchar(16),unitPrice varchar(20),room_type varchar(20),floors varchar(20),area varchar(20),community varchar(20),address varchar(20),mediator varchar(20),phone varchar(20))')
            print('建表成功')

    def process_item(self, item, spider):
        self.conn.cursor().execute('insert into lianjia values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (item['href'], item['title'], item['total'], item['unit_price'], item['room_type'], item['floors'],item['area'], item['community'], item['address'], item['mediator'], item['phone']))
        print('插入成功', item['title'])

    def close_spider(self, spider):
        self.conn.cursor().close()
        self.conn.commit()
        self.conn.close()
        print('提交数据，关闭数据库')
