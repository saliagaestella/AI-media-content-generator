import openai


class GeneratePost:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def response(self):
        openai.api_key = self.key
        messages = [{"role": "system",
                     "content": f"Act as a professional reporter.\
                                Summarize this news article and write it as \
                                if it was for an Instagram post, then write three semicolons\
                                (;;;) and in a new line write a prompt for a generative image AI \
                                to generate an image that represents it:\n\n{self.text}"}]

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content

        return reply
