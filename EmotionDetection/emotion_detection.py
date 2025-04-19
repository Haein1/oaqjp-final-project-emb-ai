import requests
import json
import math

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json=myobj, headers=header)
    if response.status_code == 400:
        return {     
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
        }
    else:
        formatted_response = json.loads(response.text)
        emotion_dic = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emo = max(emotion_dic, key=emotion_dic.get)
        
        emotion_dic['dominant_emotion'] = dominant_emo
        return emotion_dic