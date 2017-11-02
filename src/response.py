__author__ = 'hpp'
from flask import  Flask
from flask import request
import json
import  numpy as np
from voice import VoiceMeasure
app = Flask(__name__)
voice = VoiceMeasure()

@app.route('/post/compute/',methods=['POST','GET'])
def compute():
    #data_string=request.get_data()
    #dict=json.loads(data_string)
    voiceParameter = np.random.randint(0,10,(9))
    return voice.computeVoiceWithFeatures(voiceParameter)


if __name__ == '__main__':
    app.run()
   # voice = VoiceMeasure()
   # voice.getRandomVoice()
