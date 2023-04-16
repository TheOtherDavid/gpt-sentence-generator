#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

from inky.auto import auto

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold


# Set up the correct display and scaling factors

inky_display = auto(ask_user=True, verbose=True)
inky_display.set_border(inky_display.WHITE)

def reflow_quote(quote, width, font):
    words = quote.split(" ")
    reflowed = '"'
    line_length = 0

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n  " + word

    reflowed = reflowed.rstrip() + '"'

    return reflowed


def display_string(input_string):
    print("Beginning display string function")
    WIDTH = inky_display.width
    HEIGHT = inky_display.height

    img = Image.new("P", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    font_size = 24

    author_font = ImageFont.truetype(SourceSerifProSemibold, font_size)
    quote_font = ImageFont.truetype(SourceSansProSemibold, font_size)

    padding = 50
    max_width = WIDTH - padding
    max_height = HEIGHT - padding - author_font.getsize("ABCD ")[1]

    below_max_length = False

    while not below_max_length:
        quote = input_string

        print("Reflowing string")
        reflowed = reflow_quote(quote, max_width, quote_font)
        p_w, p_h = quote_font.getsize(reflowed)
        p_h = p_h * (reflowed.count("\n") + 1)

        if p_h < max_height:
            below_max_length = True
        else:
            continue

    quote_x = (WIDTH - max_width) / 2
    quote_y = ((HEIGHT - max_height) + (max_height - p_h - author_font.getsize("ABCD ")[1])) / 2

    draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.BLACK, font=quote_font, align="left")

    print(reflowed + "\n")

    print("Displaying text on device")
    inky_display.set_image(img)

    inky_display.show()

if __name__ == "__main__":
    print("""Inky wHAT: Display String

    Display a passed-in string on Inky wHAT.
    """)

    #If there's more than one argument, throw an error.

    #Get the first argument, and pass it in

    input_string = "Es gibt viele verschiedene Biersorten in Deutschland.\nThere are many different types of beer in Germany."
    display_string(input_string)