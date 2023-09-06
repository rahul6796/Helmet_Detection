import os
import sys
from pycocotools.coco import COCO
import albumentations as A
from albumentations.pytorch import ToTensorV2
from helmet.logger import logger
from helmet.exception import HelmetException
from helmet.ml.feature.helmet_detection import HelmetDetection
from helmet.utils.main_utils import save_object
from helmet.entity import DataTransformationConfig
from helmet.constants import ANNOTATIONS_COCO_JSON_FILE, INPUT_SIZE, HORIZONTAL_FLIP, VERTICAL_FLIP, \
    COLOR_JITTER, BBOX_FORMAT


class DataTransformation:

    def __init__(self,
                 config: DataTransformationConfig):
        self.config = config

    def number_of_classes(self):
        try:
            coco = COCO(os.path.join(self.config.data_transform_train_split, ANNOTATIONS_COCO_JSON_FILE))
            categories = coco.cats
            classes = [i[1]['name'] for i in categories.items()]
            n_classes = len(classes)
            return n_classes

        except Exception as ex:
            raise HelmetException(ex, sys) from ex

    def get_transforms(self, train=False):
        try:
            if train:
                transform = A.Compose([
                    A.Resize(INPUT_SIZE, INPUT_SIZE),
                    A.HorizontalFlip(p=HORIZONTAL_FLIP),
                    A.VerticalFlip(p=VERTICAL_FLIP),
                    A.ColorJitter(p=COLOR_JITTER),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format=BBOX_FORMAT))
                return transform
            else:
                transform = A.Compose([
                    A.Resize(INPUT_SIZE, INPUT_SIZE),
                    ToTensorV2()
                ], bbox_params=A.BboxParams(format=BBOX_FORMAT))
                return transform
        except Exception as ex:
            raise HelmetException(ex, sys) from ex



