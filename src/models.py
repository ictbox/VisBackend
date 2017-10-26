#coding=utf8


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeiboItem(Base):
    __tablename__ = 'weibo'

    weibo_author = Column(String(255))
    weibo_profile = Column(String(255))
    weibo_content = Column(String(255))
    weibo_dom = Column(String(255))
    weibo_time = Column(String(255))
    weibo_url = Column(String(255), primary_key=True)
    weibo_device = Column(String(255))
    weibo_retweet = Column(Integer)
    weibo_comment = Column(Integer)
    weibo_vote = Column(Integer)
    

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

class ZhihuQuestionTask(Base):
    __tablename__ = 'zhihu_question_task'

    q_id = Column(Integer,primary_key = True)
    q_url = Column(String(250),unique = True)
    q_create_time = Column(Integer)
    q_finished_time = Column(Integer)

class ZhihuAnswerCommentTask(Base):
    __tablename__ = 'zhihu_answer_comment_task'

    a_id = Column(Integer,primary_key = True)
    ac_create_time = Column(Integer)
    ac_finished_time = Column(Integer)

class ZhihuQuestionItem(Base):
    __tablename__ = 'zhihu_question'

    q_id = Column(String(20),primary_key = True)
    q_url =  Column(String(250), unique=True)
    q_title = Column(String(1000))#question title
    q_des = Column(Text)# question description
    q_view_num = Column(Integer) #被浏览 157885 次
    q_follow_num =  Column(Integer) #5567 人关注该问题
    q_answer_num =  Column(Integer) #25 个回答
    q_topic = Column(Text) # topic的(topic,url)
    q_data = Column(LONGTEXT) # 原JSON文件

class ZhihuAnswerItem(Base):
    __tablename__ = 'zhihu_answer'
    
    a_id = Column(String(20),primary_key = True)
    a_qid = Column(String(20))
    a_user = Column(String(100)) # username url
    a_user_url = Column(String(250))
    a_agree_num = Column(Integer) #赞同数量
    a_content = Column(Text) 
    a_time = Column(Integer)#时间
    a_comment_num = Column(Integer) #评论数量
    a_thanks_num = Column(Integer)
    a_data = Column(LONGTEXT) # 原JSON文件 

class ZhihuAnswerCommentItem(Base):
    __tablename__ = 'zhihu_answer_comment'
    
    ac_id = Column(String(20),primary_key = True)
    ac_a_id = Column(String(20))
    ac_user = Column(Text)
    ac_v_count = Column(Integer)
    ac_content = Column(Text) 
    ac_time = Column(Integer)
    ac_data = Column(LONGTEXT) # 原JSON文件

class ZhihuQuestionLogItem(Base):
    __tablename__ = 'zhihu_log'

    q_id = Column(Integer) 
    action_id= Column(String(20),primary_key=True) # #113421760
    action_time =  Column(String(200)) #2015-04-04 00:24:27
    action_somebody =  Column(String(100)) # url
    action_do =  Column(String(20)) #移除了话题
    action_something =  Column(Text) # 包括后面的修改理由
    action_data = Column(Text)