# PROJECT REPORT

## Title
Image Quality Analyzer Using Computer Vision

## 1. Introduction

Image quality is important in many Computer Vision applications. Poor quality images may contain blur, incorrect brightness, or insufficient edge information.

This project develops a simple Image Quality Analyzer that evaluates an image using basic Computer Vision techniques.

## 2. Objective

The main objective of this project is to automatically analyze an image and provide an overall quality assessment.

The system analyzes:

- Blur or sharpness
- Image brightness
- Edge information
- Overall image quality

## 3. Methodology

The project follows these steps:

1. Read the input image.
2. Convert the image to grayscale.
3. Calculate the Laplacian variance for blur detection.
4. Calculate average pixel intensity for brightness analysis.
5. Apply Canny edge detection.
6. Combine the results.
7. Generate a quality score out of 100.
8. Display the final recommendation.

## 4. Algorithms Used

### 4.1 Grayscale Conversion

The input image is converted from a color image into a grayscale image.

### 4.2 Laplacian Blur Detection

The Laplacian operator is used to measure image sharpness. A higher variance generally indicates stronger image details and sharper edges.

### 4.3 Brightness Analysis

The average grayscale intensity is calculated to determine whether the image is dark, normal, or too bright.

### 4.4 Canny Edge Detection

Canny edge detection is used to identify edges present in the image.

### 4.5 Quality Score

The system combines the results of the three analyses:

- Sharpness: 40 points
- Brightness: 30 points
- Edge information: 30 points

The maximum score is 100.

## 5. Technologies Used

- Python
- OpenCV
- NumPy
- Computer Vision
- GitHub

## 6. Input

The system accepts an image file such as:

- JPG
- JPEG
- PNG

## 7. Output

The program displays:

- Image resolution
- Blur score
- Blur classification
- Brightness value
- Brightness classification
- Edge density
- Final quality score
- Quality recommendation

## 8. Applications

The project can be used as a basic image quality checking system for:

- Image preprocessing
- Photo quality assessment
- Computer Vision pipelines
- Automated image screening

## 9. Limitations

The project uses simple threshold-based methods. Image quality can depend on many other factors such as noise, contrast, compression, and camera conditions.

Therefore, the quality score should be considered a basic automated assessment.

## 10. Future Scope

The project can be improved by adding:

- Noise detection
- Contrast analysis
- Face quality assessment
- Image resolution assessment
- Automatic image enhancement
- Machine learning based quality classification

## 11. Conclusion

The Image Quality Analyzer demonstrates how fundamental Computer Vision techniques can be combined to automatically evaluate image quality.

The project provides a simple quality score based on sharpness, brightness, and edge information.
