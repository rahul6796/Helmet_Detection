from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_transform_train_dir: Path
    data_transform_test_dir: Path
    data_transform_train_file_name: Path
    data_transform_test_file_name: Path
    data_transform_train_split: Path
    data_transform_test_split: Path



