import requests, json
def emotion_detector(text_to_analyse):
    """
        This function helps to detect emotion from text
    """
    if text_to_analyse=="":
        return {'anger' : None, 'disgust' : None, 'fear' : None, 'joy' : None, 
                'sadness' : None, 'dominant_emotion' : None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response["emotionPredictions"][0]['emotion']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict.update({'dominant_emotion': dominant_emotion})
    return emotion_dict