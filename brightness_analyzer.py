import numpy as np

def calculate_brightness(gray_image):
    return np.mean(gray_image)

def classify_brightness(brightness):
    if brightness < 70:
        return "TOO DARK"
    elif brightness > 190:
        return "TOO BRIGHT"
    else:
        return "NORMAL"
