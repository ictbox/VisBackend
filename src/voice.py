__author__ = 'hpp'
import random
import json
import numpy as np
from DataHelper import DataHelper

class VoiceMeasure(object):
    def __init__(self):
        self.m_topicNumber = 10     # 10 topic
        self.m_dateNumber =72       # 72 day
        self.m_fansSurpot = 2       #each fans brings 2 reader
        self.db=DataHelper()
        self.getArticleFans()       #get fans of each article
        self.getArticleTopic()      #get topic of each article
        self.getFeatures()          #get features of each article
        self.getArticleAOI()        #get amount of infomation of each article


    def getRandomVoice(self):
        '''
        :return:return random Voice in (0,100) in json for test
        '''
        voiceData = {}
        for i in range(self.m_topicNumber):
            topicVoice = []
            for j in range(self.m_dateNumber):
                topicVoice.append(random.uniform(0,100))
            topicName = 'topic' + str(i)
            voiceData[topicName]=topicVoice
        voiceDataJson = json.dumps(voiceData,sort_keys= True)
        return voiceDataJson

    def getFeatures(self):
        self.features=self.db.getRandomfeatures()

    def getArticleTopic(self):
        self.articleTopic = self.db.getRandomArticlesTopic()

    def getArticleFans(self):
        self.articleFans =self.db.getRandomArticleFans()

    def getArticleAOI(self):
        self.articleAOI =self.db.getRandomArticlesAOI()

    def computeVoiceWithFeatures(self,VoiceParameter):
        voiceData = {}
        for i in range(self.m_topicNumber):
            topicName = 'topic' + str(i)
            voiceData[topicName] = []

        for i in range (len(self.features)):
            dayFeaturePeopleNumber = np.matmul(self.features[i],np.mat(VoiceParameter).T).tolist()   #dayVoice Nx9 *9x1 =N * 1  people number support by feature
            fansPeopleNumber = self.articleFans[i] * self.m_fansSurpot                        #N*1
            expectPeopleNumber = np.maximum(fansPeopleNumber,dayFeaturePeopleNumber).tolist()        #N*1
            dayVoice =expectPeopleNumber * self.articleAOI[i]                               #N*1 * N*1     expect people number *  amount of information


            dayTopicVoice = np.matmul(np.mat(self.articleTopic[i]).T,dayVoice).tolist()     #10xN * N*1 = 10*1


            for j in range(self.m_topicNumber):
                topicName = 'topic' + str(j)
                voiceData[topicName].append(dayTopicVoice[j])
        voiceDataJson = json.dumps(voiceData,sort_keys=True)
        return voiceDataJson
