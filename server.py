from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Create Flask app
app = Flask("Emotion Detector")

# Home page
@app.route("/")
def render_index_page():
    return render_template('index.html')

# Emotion detection route
@app.route("/emotionDetector")
def emotion_detector_route():
    
    # Get text from input
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Run emotion detection
    response = emotion_detector(text_to_analyze)

    # Handle blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract scores
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

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)