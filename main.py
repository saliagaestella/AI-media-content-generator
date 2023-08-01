import get_content as gc
import ai

gc = gc.GetText(url='https://techcrunch.com/category/cryptocurrency/')
text = gc.retrieve()
title = gc.get_title().replace(' ', '-')

ai = ai.GeneratePost(key='YOUR-API-KEY', text=text)
gpt_response = ai.response()

with open(f'content/{title}', 'w', encoding="utf-8") as file:
    file.write(gpt_response)

try:
    post, prompt = gpt_response.split(';;;prompt')
except ValueError:
    post, prompt = gpt_response.split(';;;')

print(f'Post: {post}\n\nPrompt: {prompt}')
