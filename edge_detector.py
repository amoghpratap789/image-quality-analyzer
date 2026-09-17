import cv2
import numpy as np

def analyze_edges(gray_image):
    edges = cv2.Canny(gray_image, 100, 200)
    edge_density = np.mean(edges > 0)

    if edge_density >= 0.03:
        edge_status = "GOOD"
    else:
        edge_status = "LOW"

    return edge_density, edge_status
