from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models import WeiboItem
from datetime import datetime
import time # fuck python 

USERNAME = 'fangzhong'
PASSWORD = 'vis123'
SERVER = '145.239.136.200:3306'

print time.mktime(datetime.now().timetuple())

engine = create_engine('mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + SERVER + '/vis')
DBSession = sessionmaker(bind=engine)
session = DBSession()

weiboItems = session.query(WeiboItem).all()
for weibo in weiboItems:
    str_time = weibo.weibo_time
    print str_time.isnumeric()


'''
for weibo in weiboItems:
    try:
        str_time = weibo.weibo_time + ":2017"
        if ' ' in str_time:
            str_time = str_time.replace(' ','')
        wbtime = datetime.strptime(str_time, '%m?%d?%H:%M:%Y')
        #print time.mktime(wbtime.timetuple())
        weibo.weibo_time = str(int(time.mktime(wbtime.timetuple())))
    except AttributeError:
        pass
    except ValueError:
        pass

session.commit()
'''