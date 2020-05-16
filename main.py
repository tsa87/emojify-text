import requests
from bs4 import BeautifulSoup 
import emoji

url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

emojis_html = soup.find(id="emoji-objects").find_all('li')
emojis_set = set()

for emoji_html in emojis_html: 
  emoji_html = emoji_html.contents[0].contents[-2]
  try:
    descriptions = [name.strip() for name in emoji_html['data-alternative-name'].split(',')]
    emoji_name = emoji_html.string
    emojis_set.add(emoji_name)
  except:
    print("[Warning] This didn't work")
    print(emoji_html)
    continue

# for emoji_name in emojis_list:
#   print(emoji_name)
#   print(emoji.emojize(f':{emoji_name}:', use_aliases=True))

user_input = input()
user_input = user_input.lower().split()

output = []

for word in user_input:
  output.append(word)
  if word in emojis_set:
    output.append(emoji.emojize(f':{word}:', use_aliases=True))

print(" ".join(output))