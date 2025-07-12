"""
Flask web application for emotion detection.

This module provides a web interface to analyze text for emotions using the
EmotionDetection.emotion_detection module. It includes routes for rendering
the main page and processing text to detect emotions, returning the emotion
scores and the dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the web application.

    Returns:
        str: The rendered HTML content of the index.html template.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes text input for emotions and returns the emotion scores and dominant emotion.

    Retrieves text from the 'textToAnalyze' query parameter, processes it using
    the emotion_detector function, and returns a formatted string with emotion
    scores and the dominant emotion. Returns an error message for invalid input.

    Returns:
        str: A formatted string containing emotion scores and the dominant
             emotion, or an error message if the input is invalid.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
