import openai
import requests

key = "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"
url = "https://api.openai.com/v1/chat/completions"
openai.api_key = key

while(True):

  question = input("Chat GPT Ready:\n")
  if question == "close":
    break
  print("\nplease wait....\n")

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": question}
    ]
  )
  requests.delete(url)
  print(completion.choices[0].message.content + "\n")
  requests.delete(url)




