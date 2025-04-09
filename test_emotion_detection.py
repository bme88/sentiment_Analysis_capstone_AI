import unittest
from EmotionDetection import emotion_detection as ed

class Test_Emotion_Detection(unittest.TestCase):
    def test_emotion_detector(self):
        self.assertEqual(ed.emotion_detector("I am glad this happened")["dominant_emotion"],'joy')
        self.assertEqual(ed.emotion_detector("I am really mad about this")["dominant_emotion"],'anger')
        self.assertEqual(ed.emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"],'disgust')
        self.assertEqual(ed.emotion_detector("I am so sad about this")["dominant_emotion"],'sadness')
        self.assertEqual(ed.emotion_detector("I am really afraid that this will happen")["dominant_emotion"],'fear')

# Run all the test cases defined in the module when the script is executed.
# This will automatically discover and run all the test cases defined in the module.
unittest.main()