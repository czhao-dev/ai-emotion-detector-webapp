"""
Emotion Detector Server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the text from user to detect emotion
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion == 'None':
        return "Invalid text! Please try again!"

    emotion_items = [(k, v) for k, v in response.items() if k != "dominant_emotion"]
    parts = [f"'{k}': {v}" for k, v in emotion_items]
    if len(parts) > 1:
        emotion_str = ", ".join(parts[:-1]) + " and " + parts[-1]
    else:
        emotion_str = parts[0]

    return (f"For the given statement, the system response is {emotion_str}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>.")

@app.route("/")
def render_index_page():
    """
    This function runs the render_template function on the HTML template index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
