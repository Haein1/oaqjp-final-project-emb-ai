# from flask import Flask, request, render_template
# from EmotionDetection.emotion_detection import emotion_detector

# app = Flask("Emotion")

# @app.route("/emotionDetector")
# def emotion_dect():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = emotion_detector(text_to_analyze)

#     if response['dominant_emotion'] == None:
#         return "Invalid text! Please try again!."
#     else:
#         return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'],response['dominant_emotion'])

# @app.route("/")
# def render_index_page():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run("0.0.0.0", port=5000)


"""Flask app for detecting emotions from text using a custom emotion detector."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion")

@app.route("/emotionDetector")
def emotion_dect():
    """
    Handle the emotion detection endpoint.

    Returns:
        str: Emotion analysis or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    message = "For the given statement, the system response is "
    message_dominant = "The dominant emotion is "
    anger_disgust = "'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    fear_joy = "'fear': {response['fear']}, 'joy': {response['joy']} and "
    sad = "'sadness': {response['sadness']}. "
    domi = response['dominant_emotion']
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."
    return f"{message}{anger_disgust}{fear_joy}{sad}{message_dominant}{domi}."

@app.route("/")
def render_index_page():
    """
    Render the homepage.

    Returns:
        HTML: Rendered index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
