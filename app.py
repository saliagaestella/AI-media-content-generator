import requests
from bs4 import BeautifulSoup
import openai
import customtkinter


class GetText:
    def __init__(self, url):
        self.url = url
        self.name = None

    def retrieve(self):
        # Making a GET request
        r = requests.get(self.url, verify=False)

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        # Gets all the links in the website
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))

        # Opens new link, which is the first news article in the website
        r2 = requests.get(links[3], verify=False)

        soup2 = BeautifulSoup(r2.content, 'html.parser')

        self.name = soup2.find('h1', class_='article__title').text
        article_text = soup2.find('div', class_='article-content').text

        return article_text

    def get_title(self):
        return self.name


class GeneratePost:
    def __init__(self, key, text):
        self.key = key
        self.text = text

    def response(self):
        openai.api_key = self.key
        messages = [{"role": "system",
                     "content": f"Act as a professional reporter.\
                                Summarize this news article and write it as \
                                if it was for an Instagram post, then write 'Prompt:'\
                                in a new line and write a prompt for a generative image AI \
                                to generate an image that represents it. This is the article:\n\n{self.text}"}]

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content

        return reply


if __name__ == "__main__":

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    root = customtkinter.CTk()
    root.geometry('800x600')
    root.title('AI News')


    def generate(event=None):
        gc = GetText(url='https://techcrunch.com/category/cryptocurrency/')
        text = gc.retrieve()
        title = gc.get_title()

        ai = GeneratePost(key=api.get(), text=text)
        gpt_response = ai.response()

        label2 = customtkinter.CTkLabel(master=frame, text=title, font=('Roboto', 18))
        label2.pack(pady=12, padx=10)

        textbox = customtkinter.CTkTextbox(master=frame, font=('Roboto', 18), width=600, height=300)
        textbox.insert(index='1.0', text=gpt_response)
        textbox.pack(pady=12, padx=10)

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = customtkinter.CTkLabel(master=frame, text='AI Generated News Summary', font=('Roboto', 24))
    label.pack(pady=12, padx=10)

    api = customtkinter.CTkEntry(master=frame, placeholder_text="API Key")
    api.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text='Generate', command=generate)
    button.pack(pady=12, padx=10)

    root.bind('<Return>', generate)

    root.mainloop()
