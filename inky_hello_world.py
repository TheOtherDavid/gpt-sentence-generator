#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys

from inky.auto import auto

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

print("""Inky wHAT: Hello World

Display Hello World on Inky wHAT.
""")

# Set up the correct display and scaling factors

inky_display = auto(ask_user=True, verbose=True)
inky_display.set_border(inky_display.WHITE)
# inky_display.set_rotation(180)

# This function will take a quote as a string, a width to fit
# it into, and a font (one that's been loaded) and then reflow
# that quote with newlines to fit into the space required.


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


WIDTH = inky_display.width
HEIGHT = inky_display.height

# Create a new canvas to draw on

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# Load the fonts

font_size = 24

author_font = ImageFont.truetype(SourceSerifProSemibold, font_size)
quote_font = ImageFont.truetype(SourceSansProSemibold, font_size)


# The amount of padding around the quote. Note that
# a value of 30 means 15 pixels padding left and 15
# pixels padding right.
#
# Also define the max width and height for the quote.

padding = 50
max_width = WIDTH - padding
max_height = HEIGHT - padding - author_font.getsize("ABCD ")[1]

below_max_length = False

# Only pick a quote that will fit in our defined area
# once rendered in the font and size defined.

while not below_max_length:
    quote = "Hello, World!"

    reflowed = reflow_quote(quote, max_width, quote_font)
    p_w, p_h = quote_font.getsize(reflowed)  # Width and height of quote
    p_h = p_h * (reflowed.count("\n") + 1)   # Multiply through by number of lines

    if p_h < max_height:
        below_max_length = True              # The quote fits! Break out of the loop.

    else:
        continue

# x- and y-coordinates for the top left of the quote

quote_x = (WIDTH - max_width) / 2
quote_y = ((HEIGHT - max_height) + (max_height - p_h - author_font.getsize("ABCD ")[1])) / 2

# x- and y-coordinates for the top left of the author

author_x = quote_x
author_y = quote_y + p_h


# Write our quote and author to the canvas

draw.multiline_text((quote_x, quote_y), reflowed, fill=inky_display.BLACK, font=quote_font, align="left")

print(reflowed + "\n")

# Display the completed canvas on Inky wHAT

inky_display.set_image(img)
inky_display.show()
