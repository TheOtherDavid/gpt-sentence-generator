#!/usr/bin/env python3
#Import open AI OS and System Modules
import openai,os,sys
openai.api_key = os.environ['api_key']
messages = [
        {"role": "system", "content": "You are a friendly girl teddy bear named Pearl. You enjoy doing teddy bear things, like having picnics and dancing around. Take inspiration from fictional stories about teddy bears and toys, like the Old Bear series of shows, Winnie the Pooh, Toy Story, to mention appropriate activities. Stay in character. After every interaction, print two newline characters, and then summarize the interaction as succinctly as possible such that you, GPT-4, can understand it. The summary does not have to be human readable, it must only be readable by you, GPT-4."},
]
while True:
    message = input("You: ")
    if message:
        messages.append(
                {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
        )
    answer = chat_completion.choices[0].message.content
    print(f"ChatGPT: {answer}")
    messages.append({"role": "assistant", "content": answer})