import cv2
import numpy as np
import sys

def analyze_image(filename):

    image = cv2.imread(filename)

    if image is None:
        print("Error: Image could not be loaded.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur detection
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    if blur_score < 100:
        blur_status = "BLURRY"
    else:
        blur_status = "SHARP"

    # Brightness analysis
    brightness = np.mean(gray)

    if brightness < 70:
        brightness_status = "TOO DARK"
    elif brightness > 190:
        brightness_status = "TOO BRIGHT"
    else:
        brightness_status = "NORMAL"

    # Edge detection
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.mean(edges > 0)

    if edge_density >= 0.03:
        edge_status = "GOOD"
    else:
        edge_status = "LOW"

    # Quality score
    score = 0

    if blur_status == "SHARP":
        score += 40

    if brightness_status == "NORMAL":
        score += 30

    if edge_status == "GOOD":
        score += 30

    print("=" * 45)
    print("       IMAGE QUALITY ANALYZER")
    print("=" * 45)

    print("\nResolution:", image.shape[1], "x", image.shape[0])

    print("\n1. BLUR ANALYSIS")
    print("Blur Score:", round(blur_score, 2))
    print("Result:", blur_status)

    print("\n2. BRIGHTNESS ANALYSIS")
    print("Brightness:", round(brightness, 2))
    print("Result:", brightness_status)

    print("\n3. EDGE ANALYSIS")
    print("Edge Density:", round(edge_density, 4))
    print("Result:", edge_status)

    print("\n4. FINAL QUALITY SCORE")
    print(score, "/100")

    if score >= 80:
        print("Recommendation: GOOD QUALITY IMAGE")
    elif score >= 50:
        print("Recommendation: AVERAGE QUALITY IMAGE")
    else:
        print("Recommendation: LOW QUALITY IMAGE")

    print("\n" + "=" * 45)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python main.py image.jpg")
    else:
        analyze_image(sys.argv[1])
