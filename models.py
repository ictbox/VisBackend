#coding=utf8


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeixinTask(Base):
    __tablename__ = 'wexin_task'

    query = Column(String(50), primary_key=True)
    date = Column(String(10), primary_key=True)
    begin_time = Column(Integer)
    end_time = Column(Integer)

class WeixinArticle(Base):
    __tablename__ = 'weixin'


    sogou_url =  Column(String(250), primary_key=True)

    sogou_time = Column(String(10), primary_key=True)
    sogou_title = Column(Text)
    sogou_author = Column(String(100), primary_key=True)

    sogou_desc = Column(String(250))

    weixin_html = Column(LONGTEXT)
    weixin_title = Column(String(250))
    weixin_gzh = Column(String(100))
    wexin_author = Column(String(250))    
    wexin_time = Column(Integer)

    # weixin_like = Column(Integer)
    # weixin_read = Column(Integer)
    # weixin_comment = Column(Integer) 
