'''Runs Flask server for emotion recognition app interface'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    '''Render index template on homepage for app'''
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    '''Get response from emotion detection API and analyzes user input'''
    text_to_analyze = request.args.get('textToAnalyze')

    # If no text
    if not text_to_analyze:
        return "Invalid text! Please try again."

    # Call emotion detector function
    result = emotion_detector(text_to_analyze)
    dominant_emotion = max(result, key=result.get)
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']

    # Format output
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
