import requests
import json

def emotion_detector(text_to_analyze):
    error_payload = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # Handle server error response when the user fails to provide text to analyze
    if not text_to_analyze:
        return error_payload

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)

    # Handler server error response for status_code 400
    if response.status_code == 400:
        return error_payload

    formatted_response = json.loads(response.text)

    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]

    # Extract scores and map to emotion names
    emotion_map = {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"]
    }

    # Find dominant emotion
    dominant_emotion = max(emotion_map, key=emotion_map.get)

    # Extend the emotion_map to be returned to include the dominant_emotion key and value
    emotion_map["dominant_emotion"] = dominant_emotion

    # Returning the complete emotion_map dictionary containing all required key value pairs
    return emotion_map
    