import json
import time
import gpt_language_phrase
import inky_display
import logging_utils
import file_operations
from argparse import ArgumentParser
from dotenv import load_dotenv

load_dotenv()
logger = logging_utils.get_logger()

def main():
    args = parse_arguments()
    config = load_config()
    loop_time = config["loop_time"]

    if args.loop:
        while True:
            logger.info("Executing Hourly GPT Phrase Generator")
            display_gpt_sentence()
            logger.info("Sleeping for" + str(loop_time) + "minutes")
            time.sleep(loop_time * 60)
    else:
        logger.info("Executing Single GPT Phrase Generator")
        display_gpt_sentence()

def display_gpt_sentence():
    text = gpt_language_phrase.get_language_phrase()
    formatted_text = gpt_language_phrase.cleanup_language_phrase(text)

    inky_display.display_string(text)
    file_operations.save_text(text)

def parse_arguments():
    parser = ArgumentParser(description="Run the Raspberry Pi program.")
    parser.add_argument(
        "-l", "--loop", action="store_true", help="Run the program in a loop with an hourly sleep"
    )
    return parser.parse_args()

def load_config():
    with open("config.json") as f:
        config = json.load(f)
    return config

if __name__ == "__main__":
    main()