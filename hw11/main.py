import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/posts')
response_json = json.loads(response.text)

result = ''

for idx, el in enumerate(response_json):
    result += el['title'].capitalize() + '\n'
    list_sent = [i.capitalize() + '.' for i in el['body'].split('\n')]
    result += ' '.join(list_sent)

    if idx >= len(response_json) - 1:  # Чтобы не было вконце 2 пустые строки после последней.
        break

    result += '\n\n'

with open('./text.txt', 'w') as file:
    file.write(result)
