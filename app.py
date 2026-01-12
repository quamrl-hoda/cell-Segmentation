from src.cellSegmentation.logger import logging
from src.cellSegmentation.exception import CustomException
import sys


logging.info("Starting the application...")

try:
    1/"0"
except Exception as e:
    raise CustomException(e, sys)