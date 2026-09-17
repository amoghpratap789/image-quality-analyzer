import cv2

def load_image(filename):
    image = cv2.imread(filename)

    if image is None:
        raise ValueError("Image could not be loaded. Please check the file path.")

    return image
