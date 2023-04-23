import sys
import time
import gpt_language_phrase
import inky_display
from argparse import ArgumentParser

def main():
    args = parse_arguments()
    config = load_config()
    loop_time = config["loop_time"]

    if args.loop:
        while True:
            print("Executing Hourly GPT Phrase Generator")
            display_gpt_sentence()
            print("Sleeping for an hour...")
            time.sleep(loop_time)
    else:
        print("Executing Single GPT Phrase Generator")
        display_gpt_sentence()

def display_gpt_sentence():
    text = gpt_language_phrase.get_language_phrase()
    inky_display.display_string(text)

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