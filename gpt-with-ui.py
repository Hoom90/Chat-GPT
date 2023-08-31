import openai
import requests
from tkinter import *
import tkinter as tk

key = "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"
url = "https://api.openai.com/v1/chat/completions"
openai.api_key = key

def search():
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": question}
    ]
  )
  requests.delete(url)
  answer.insert("1.0", completion.choices[0].message.content)
  requests.delete(url)

window = tk.Tk()
window.title("Chat GPT")

window.geometry("300x600")
window.resizable(False, False)

tk.Label(window,text="Ask Chat GPT").pack()

question = tk.Text(window,height=3,width=30).pack()

tk.Button(window,command=search,height=1,width=30,text="search").pack()

answer = tk.Text(window,height=3,width=30).pack()



