#Save the variable text inside a file called phrases.txt
# Path: file_operations.py
import os
import logging_utils
from dotenv import load_dotenv

load_dotenv()
filename = os.environ.get('PHRASES_FILE_LOCATION', 'phrases.txt')
logger = logging_utils.get_logger()

def save_text(text):
    logger.info("Saving phrase to file.")
    with open(filename, 'a') as f:
        f.write(text + "\n")
    logger.info("Text saved to file.")