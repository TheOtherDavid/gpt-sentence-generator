#!/usr/bin/env python3

import openai
import os
import json
import random
import logging_utils
from dotenv import load_dotenv

load_dotenv()
logger = logging_utils.get_logger()

def get_language_phrase():
    logger.info("Loading environment variables.")
    api_key = os.environ['API_KEY']
    openai.api_key = api_key

    logger.info("Loading configs.")
    with open('config.json') as f:
        config = json.load(f)

    logger.info("Choosing topic.")
    topics = config['topics']
    topic = random.choice(topics)
    language = config['language']
    level = config['level']

    logger.info("Topic is: " + topic)

    logger.info("Beginning to get a phrase from GPT.")

    messages = [
        {"role": "system", "content": "You are a writer for a language-learning website, writing sample sentences."},
    ]

    prompt = config['base_prompt']
    prompt = prompt + "\nLanguage: " + language
    prompt = prompt + "\nLevel: " + level
    prompt = prompt + "\nTopic: " + topic

    message = prompt
    logger.info("Prompt:" + prompt)


    logger.info("Making call to OpenAI")
    messages.append({"role": "user", "content": message})
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.5
    )
    answer = chat_completion.choices[0].message.content
    logger.info(f"Response: {answer}")
    return answer

def cleanup_language_phrase(phrase):
    logger.info("Loading environment variables.")
    api_key = os.environ['API_KEY']
    openai.api_key = api_key

    logger.info("Loading configs.")
    with open('config.json') as f:
        config = json.load(f)

    logger.info("Beginning to clean up the phrase.")

    messages = [
        {"role": "system", "content": "You are an editor, cleaning up input according to specifications."},
    ]

    prompt = config['cleanup_prompt']
    prompt = prompt + phrase
    
    message = prompt
    logger.info("Prompt:" + prompt)


    logger.info("Making call to OpenAI")
    messages.append({"role": "user", "content": message})
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.5
    )
    answer = chat_completion.choices[0].message.content
    logger.info(f"Response: {answer}")
    return answer

if __name__ == '__main__':
    response = get_language_phrase()
    