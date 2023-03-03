import openai

initial_prompt = """
Ling is an AI language model specialized at translation. Specifically Bible translation.
This means that given a verse in Urdu, Ling will translate a back translation in Urdu that matches the Urdu in meaning.
Ling will not add information to the translation or correct it to be more like existing Bible translations.
The conversation starts now: """
openai.api_key = "key"


messages = [
  {"role": "system", "content": initial_prompt},
  {"role": "user", "content": "شروعات میں بلند مقام رکھنے والا خدا نے کائنات کو پیدا کیا۔"},
  {"role": "assistant", "content": " In the very beginning, the Exalted God created the universe"}
]
def respond(text):

  question = {"role": "user", "content": text}
  messages.append(question)
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=1000,
    temperature=.5,
  )

  answer = completion["choices"][0]
  raw = answer['message']['content']
  answer = completion["choices"][0]
  return answer
print(respond("""اب بلند مقام والا خدا نے حکم دیا: "روشنی ہو"""""))