import sys
from main import analyze_image

if len(sys.argv) != 2:
    print("Please provide an image file.")
    print("Example: python run_project.py image.jpg")
else:
    analyze_image(sys.argv[1])
