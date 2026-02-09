import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_joy(self):
        emotions = emotion_detector('I am glad this happened')
        max_emotion = max(emotions, key=emotions.get)

        self.assertEqual(max_emotion, 'joy')
    
    def test_emotion_detector_anger(self):
        emotions = emotion_detector('I am really mad about this')
        max_emotion = max(emotions, key=emotions.get)

        self.assertEqual(max_emotion, 'anger')

    def test_emotion_detector_disgust(self):
        emotions = emotion_detector('I feel disgusted just hearing about this')
        max_emotion = max(emotions, key=emotions.get)

        self.assertEqual(max_emotion, 'disgust')
    
    def test_emotion_detector_sadness(self):
        emotions = emotion_detector('I am so sad about this')
        max_emotion = max(emotions, key=emotions.get)

        self.assertEqual(max_emotion, 'sadness')

    def test_emotion_detector_fear(self):
        emotions = emotion_detector('I am really afraid that this will happen')
        max_emotion = max(emotions, key=emotions.get)

        self.assertEqual(max_emotion, 'fear')



if __name__ == '__main__':
    unittest.main()