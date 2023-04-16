import gpt_language_phrase
import inky_display

def main():
    text = gpt_language_phrase.get_language_phrase()
    inky_display.display_string(text)

if __name__ == "__main__":
    main()