import cv2

def calculate_blur_score(gray_image):
    return cv2.Laplacian(gray_image, cv2.CV_64F).var()

def classify_blur(blur_score):
    if blur_score < 100:
        return "BLURRY"
    else:
        return "SHARP"
