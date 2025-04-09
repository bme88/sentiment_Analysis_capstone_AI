"""
    This server hosts API for sentiment detector
"""
from flask import Flask, request
from EmotionDetection import emotion_detection as ed

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector():
    """
     This function receive textToAnalyze from the interface and send
     back the sentimental analysis
    """
    text = request.args.get('textToAnalyze')
    result = ed.emotion_detector(text)
    dominant_emotion=result.pop("dominant_emotion",None)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    string = ', '.join([f"'{key}' : {value}" for key, value in result.items()])
    re_string = f"For the given statement, the system response \
    is {string}.The dominant emotion is {dominant_emotion}."
    return re_string

if __name__ == "__main__":

    app.run(host='127.0.0.1', port=5000)
