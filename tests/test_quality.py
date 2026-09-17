import unittest

from quality_scorer import calculate_quality_score, get_recommendation
from brightness_analyzer import classify_brightness


class TestQualityAnalyzer(unittest.TestCase):

    def test_quality_score(self):
        score = calculate_quality_score("SHARP", "NORMAL", "GOOD")
        self.assertEqual(score, 100)

    def test_low_quality_score(self):
        score = calculate_quality_score("BLURRY", "TOO DARK", "LOW")
        self.assertEqual(score, 0)

    def test_good_recommendation(self):
        recommendation = get_recommendation(100)
        self.assertEqual(recommendation, "GOOD QUALITY IMAGE")

    def test_brightness_classification(self):
        self.assertEqual(classify_brightness(50), "TOO DARK")
        self.assertEqual(classify_brightness(120), "NORMAL")
        self.assertEqual(classify_brightness(210), "TOO BRIGHT")


if __name__ == "__main__":
    unittest.main()
