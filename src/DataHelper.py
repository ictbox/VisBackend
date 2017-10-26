from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from models import *
import json

USERNAME = 'fangzhong'
PASSWORD = 'vis123'
SERVER = '145.239.136.200:3306'

class LocalData():
    def __init__(self):
        with open('weibo_user.json', 'r') as f:
            self.weibo_user = json.load(f)
    
    def query(self, user):
        return filter(lambda x:x['url'] == user, self.weibo_user)

local = LocalData()


class DataHelper():
    def __init__(self):
        engine = create_engine('mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + SERVER + '/vis')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def QueryZhihuInfoByTime(self, startDateTime, endDateTime):
        ret = []
        start = startDateTime.timestamp()
        end = startDateTime.timestamp()
        zhihuAnswer = session.query(ZhihuAnswerItem).filter(a_time>=start and a_time<=end).all()
        for zhas in zhihuAnswer:
            if (zhas.a_user == ""):
                continue
            zhihuUser = session.query(ZhihuUserItem).filter(user==zhas.a_user).one()
            ret.append([\
                zhas.a_agree_num, \
                zhas.a_comment_num, \
                zhas.a_thanks_num, \
                zhihuUser.follow ] \
            )
        return ret

    def QueryWeiboInfoByTime(self, startDateTime, endDateTime):
        ret = []
        #start = startDateTime.timestamp()
        #end = startDateTime.timestamp()
        
        weibos = self.session.query(WeiboItem).filter(WeiboItem.weibo_comment > 5000).all()
        for weibo in weibos:
            #weiboUser = session.query(WeiboUserItem).filter(user==weibo.user).one()
            weiboUser = local.query(weibo.weibo_profile)
            ret.append([\
                weibo.weibo_retweet, \
                weibo.weibo_comment, \
                weibo.weibo_vote, \
                int(weiboUser[0][u"\u7c89\u4e1d"]) ] \
            )
        return ret

if __name__ == "__main__":
    dataHelper = DataHelper()
    print dataHelper.QueryWeiboInfoByTime(datetime.now, datetime.now)

