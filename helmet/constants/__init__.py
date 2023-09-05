import os
import torch
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%M_%S")

# data ingestion = constants:
ARTIFACTS_DIR = os.path.join("artifact", TIMESTAMP)
BUCKET_NAME = 'helmet-object-detection'
ZIP_FILE_NAME = 'data.zip'
ANNOTATION_COCO_JSON_FILE = '_annotation.coco.json'

INPUT_SIZE=416
HORIZONTAL_FLIP=0.3
VERTICAL_FLIP=0.3
RANDOM_BRIGHTNESS_CONTRAST = 0.1
COLOR_JITTER = 0.1
BBOX_FORMAT = 'coco'

RAW_FILE_NAME = 'helemt'

# data ingestion constant:
DATA_INGESTION_ARTIFACT_DIR = 'DataIngestionArtifact'
DATA_INGESTION_TRAIN_DIR = 'train'
DATA_INGESTION_TEST_DIR = 'test'
DATA_INGESTION_VALID_DIR = 'val'












# AWS Constant:
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "ap-south-1"

