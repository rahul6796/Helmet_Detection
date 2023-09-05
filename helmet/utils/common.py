import os
import sys
import yaml
from helmet.logger import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from helmet.exception import HelmetException


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """

    :param path_to_yaml:
    :return:
        ConfigBox: configbox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :: {yaml_file} successfully loaded !")
        return ConfigBox(content)
    except Exception as ex:
        raise HelmetException(ex, sys) from ex


@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """

    :param path_to_directory:
    :param verbose:
    :return:
    """

    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
