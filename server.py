"""Flask web application for Emotion Detection using Watson NLP."""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Create Flask app
app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Render the home page of the web application.

    Returns:
        str: Rendered HTML page (index.html)
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to process text input and return emotion analysis.

    Returns:
        str: Formatted string of emotion scores and dominant emotion.
             If input is blank, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format output
    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result


if __name__ == "__main__":
    # Run Flask app on all interfaces and port 5000
    app.run(host="0.0.0.0", port=5000)