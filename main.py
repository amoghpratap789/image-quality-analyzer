import cv2

from image_loader import load_image
from blur_detector import calculate_blur_score, classify_blur
from brightness_analyzer import calculate_brightness, classify_brightness
from edge_detector import analyze_edges
from quality_scorer import calculate_quality_score, get_recommendation


def analyze_image(filename):

    try:
        image = load_image(filename)
    except ValueError as error:
        print("Error:", error)
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur analysis
    blur_score = calculate_blur_score(gray)
    blur_status = classify_blur(blur_score)

    # Brightness analysis
    brightness = calculate_brightness(gray)
    brightness_status = classify_brightness(brightness)

    # Edge analysis
    edge_density, edge_status = analyze_edges(gray)

    # Quality score
    score = calculate_quality_score(
        blur_status,
        brightness_status,
        edge_status
    )

    recommendation = get_recommendation(score)

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

    print("Recommendation:", recommendation)

    print("\n" + "=" * 45)


if __name__ == "__main__":

    if len(__import__("sys").argv) < 2:
        print("Usage: python main.py image.jpg")
    else:
        analyze_image(__import__("sys").argv[1])
