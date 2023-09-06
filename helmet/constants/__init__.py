from pathlib import Path
CONFIG_FILE_PATH = Path("config/config.yaml")
ANNOTATIONS_COCO_JSON_FILE = '_annotations.coco.json'

INPUT_SIZE = 416
HORIZONTAL_FLIP = 0.3
VERTICAL_FLIP = 0.3
RANDOM_BRIGHTNESS_CONTRAST = 0.1
COLOR_JITTER = 0.1
BBOX_FORMAT = 'coco'

RAW_FILE_NAME = 'helmet'