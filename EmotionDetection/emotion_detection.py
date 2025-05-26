import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyse} }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = input_json, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
    # Extracting the set of emotions along with their scores
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_scores['anger']
        disgust_score = emotion_scores['disgust']
        fear_score = emotion_scores['fear']
        joy_score = emotion_scores['joy']
        sadness_score = emotion_scores['sadness']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)    
    elif response.status_code == 400:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_emotion = 'None'

    # Returning a dictionary containing emotion detection results
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }