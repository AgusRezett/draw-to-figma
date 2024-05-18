import os
from dotenv import load_dotenv
from src.instantneo_integration import classify_contours_model

import cv2
import numpy as np

load_dotenv()

figma_token = os.getenv("FIGMA_TOKEN")
file_id = os.getenv("FILE_ID")
