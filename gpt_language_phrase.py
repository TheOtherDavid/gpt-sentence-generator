#!/usr/bin/env python3

from dotenv import load_dotenv
import openai
import os
import json

def get_language_phrase():
    print("Loading environment variables.")
    load_dotenv()
    api_key = os.environ['API_KEY']
    openai.api_key = api_key

    print("Loading configs.")
    with open('config.json') as f:
        config = json.load(f)

    print("Beginning to get a phrase from GPT.")

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
        messages=messages,
        temperature=1.5
    )
    answer = chat_completion.choices[0].message.content
    print(f"Response: {answer}")
    return answer

if __name__ == '__main__':
    response = get_language_phrase()
    