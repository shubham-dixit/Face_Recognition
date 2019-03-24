# Project By
# Shubham Dixit

# Importing Libraries
import cv2
import os
import numpy as np

# Importing Python Image Library (PIL)
from PIL import Image

# Creating Local Binary Patterns Histograms for Face Recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Using prebuilt frontal face training model, for face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
