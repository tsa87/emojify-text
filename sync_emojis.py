"""Crawls a website to get UNICODE emoji names from different categories and writes them into text files.
"""

import requests
from bs4 import BeautifulSoup

def sync_emojis():
  url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'

  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  emojis_types = ["emoji-objects", "emoji-nature", "emoji-people", "emoji-symbols"]
  common_words = ["and"]

  for emojis_type in emojis_types:
    emojis_htmls = soup.find(id=f"{emojis_type}").find_all('li')

    filename = emojis_type.replace('-', '_')
    with open(f"dataset/{filename}.txt", "w+") as f:

      for emoji_html in emojis_htmls:
        
        # navigate to the <span></span> that we are looking for
        emoji_html = emoji_html.contents[0].contents[-2]

        offical_name = emoji_html.string

        try: # Sometimes data-alternative-name tag does not exist
          aliases = []
          for name in emoji_html['data-alternative-name'].split(","):
            name = name.strip().split()
            print(name)
            for term in name:
              if term not in common_words:
                aliases.append(term)
        except:
          aliases = []
        
        

        all_names = [offical_name] + aliases

        f.write(" ".join(all_names) + "\n")
