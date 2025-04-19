import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        s1 =  emotion_detector("I am glad this happened")
        self.assertEqual(s1['dominant_emotion'], 'joy')  

        s2 = emotion_detector('I am really mad about this')
        self.assertEqual(s2['dominant_emotion'],'anger')  

        s3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(s3['dominant_emotion'],'disgust') 

        s4 = emotion_detector('I am so sad about this')
        self.assertEqual(s4['dominant_emotion'],'sadness') 

        s5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(s5['dominant_emotion'],'fear') 

unittest.main()
