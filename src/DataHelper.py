from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from models import *

USERNAME = 'fangzhong'
PASSWORD = 'vis123'
SERVER = '0.0.0.0:3306'



class DataHelper():
    def __init__():
        engine create_engine('mysql+pymysql://' + username + ':' + PASSWORD + '@' + SERVER + '/vis')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def QueryZhihuInfoByTime(startDateTime, endDateTime):
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

    def QueryWeiboInfoByTime(startDateTime, endDateTime)
        ret = []
        start = startDateTime.timestamp()
        end = startDateTime.timestamp()
        
        weibos = session.query(WeiboItem).filter(a_time>=start and a_time<=end).all()
        for weibo in weibos:
            weiboUser = session.query(WeiboUserItem).filter(user==weibo.user).one()
            ret.append([\
                weibo.retweet, \
                weibo.comment, \
                weibo.vote, \
                weiboUser.follow ] \
            )
        return ret
    