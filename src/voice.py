__author__ = 'hpp'
import random
import json
class VoiceMeasure(object):
    def __init__(self):
        self.m_topicNumber = 10     # 10 topic
        self.m_dateNumber =72       # 72 day

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
    