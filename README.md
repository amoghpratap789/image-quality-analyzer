# Image Quality Analyzer

## 1. Project Overview

Image Quality Analyzer is a Computer Vision project that analyzes an uploaded image and evaluates its basic quality.

The system checks:
- Image sharpness
- Image brightness
- Edge information
- Overall image quality

The project uses Python and OpenCV.

## 2. Features

### Feature 1: Blur Detection
The system uses the Laplacian operator to determine whether an image is sharp or blurry.

### Feature 2: Brightness Analysis
The system calculates the average brightness of the image and classifies it as dark, normal, or too bright.

### Feature 3: Edge Detection
Canny Edge Detection is used to identify important edges in the image.

### Feature 4: Quality Score
The results of the different analyses are combined to generate an overall quality score out of 100.

## 3. Technologies Used

- Python
- OpenCV
- NumPy
- Google Colab
- GitHub

## 4. Computer Vision Techniques

The project uses:
- Grayscale image conversion
- Laplacian variance
- Canny edge detection
- Pixel intensity analysis

## 5. How to Run

### Step 1: Install Python

Install Python 3.8 or later.

### Step 2: Install Dependencies

Run:

```bash
pip install -r requirements.txt

## 6. Output

The system provides:
- Image resolution
- Blur score
- Blur classification
- Brightness value
- Brightness classification
- Edge density
- Final quality score
- Quality recommendation

## 7. Applications

This project can be useful for:
- Photo quality checking
- Image preprocessing
- Computer Vision applications
- Automatic image screening

## 8. Future Enhancements

Future versions can include:
- Face quality detection
- Noise detection
- Contrast analysis
- Automatic image enhancement
- Web-based interface

## 9. Conclusion

The Image Quality Analyzer demonstrates how basic Computer Vision techniques can be combined to evaluate the quality of digital images.
## 8. Testing

The project includes automated tests for the quality scoring and brightness analysis modules.

Run the tests using:

```bash
python -m unittest discover -s tests
