import requests
import html_parse
import pymysql
from bs4 import BeautifulSoup
from html_parse import html_prase_object

if __name__ == '__main__':
    db = pymysql.connect('47.240.7.200', 'root', 'abc-123', 'javmoo')
    cursor = db.cursor()

    res = html_prase_object.get_content('https://www.ivsky.com/tupian/renwutupian/')
    soup = BeautifulSoup(res,'lxml')
    res_list = soup.find_all('div','il_img')
    for item in  res_list:
         a = item.a
         sql = "insert into picture_info(href,title,src) values ('%s','%s','%s')" % (a['href'],a['title'],'22')
         cursor.execute(sql)
    db.commit()

