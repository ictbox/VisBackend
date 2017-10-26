__author__ = 'hpp'
from flask import  Flask
from flask import request
import json
from voice import VoiceMeasure
app = Flask(__name__)
voice = VoiceMeasure()

@app.route('/post/compute/',methods=['POST','GET'])
def compute():
    #data_string=request.get_data()
    #dict=json.loads(data_string)
    return voice.getRandomVoice()


if __name__ == '__main__':
    app.run()
   # voice = VoiceMeasure()
   # voice.getRandomVoice()