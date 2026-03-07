from EmotionDetection import emotion_detector

def test_emotion_detector():
    
    # Test 1
    result = emotion_detector("I am glad this happened")
    assert result['dominant_emotion'] == 'joy'

    # Test 2
    result = emotion_detector("I am really mad about this")
    assert result['dominant_emotion'] == 'anger'

    # Test 3
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result['dominant_emotion'] == 'disgust'

    # Test 4
    result = emotion_detector("I am so sad about this")
    assert result['dominant_emotion'] == 'sadness'

    # Test 5
    result = emotion_detector("I am really afraid that this will happen")
    assert result['dominant_emotion'] == 'fear'

test_emotion_detector()

print("All tests passed successfully!")