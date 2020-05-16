import emoji
import random 

from sync_emojis import *

sync = True
if sync:
  sync_emojis()

emojis_types = ["emoji-objects", "emoji-nature", "emoji-people", "emoji-symbols"]

offical_set = set()
lookup_dict = {}

for emojis_type in emojis_types:
  filepath = "dataset/" + emojis_type.replace("-", "_") + ".txt"

  with open(filepath) as f:
    for line in f:
      names = line.split()
      offical_name = names[0]

      for name in names:
        for term in name.split('-'): 
          if term in lookup_dict.keys():
            lookup_dict[term].append(offical_name)
          else:
            lookup_dict[term] = [offical_name]


# if "apple" is a emoji but it is also an aliases for iphone, we only show "apple" emoji
for key in lookup_dict.keys():  
  if key in lookup_dict[key]:
    lookup_dict[key] = [key]


user_input = input()
user_input = user_input.lower().split()

output = []

for word in user_input:

  output.append(word)

  if word in lookup_dict.keys():
    name = random.choice(lookup_dict[word])

    if len(word) > 2:
      output.append(emoji.emojize(f':{name}:', use_aliases=True))
    else: # for letters and numbers
      output[-1] = emoji.emojize(f':{name}:', use_aliases=True)

print(" ".join(output))