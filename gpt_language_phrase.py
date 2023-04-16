#!/usr/bin/env python3

import openai
import os
import json

def get_language_phrase():
    print("Beginning to get a phrase from GPT.")
    with open('config.json') as f:
        config = json.load(f)

    openai.api_key = os.environ['api_key']

    messages = [
        {"role": "system", "content": "You are a writer for a language-learning website, writing sample sentences."},
    ]

    prompt = config['base_prompt']
    language = config['language']
    prompt = prompt + "\nLanguage: " + language
    level = config['level']
    prompt = prompt + "\nLevel: " + level
    topic = config['topic']
    prompt = prompt + "\nTopic: " + topic

    message = prompt
    print("Prompt:" + prompt)


    print("Making call to OpenAI")
    messages.append({"role": "user", "content": message})
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    answer = chat_completion.choices[0].message.content
    print(f"Response: {answer}")
    return answer

if __name__ == '__main__':
    response = get_language_phrase()
    