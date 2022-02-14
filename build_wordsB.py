import json

with open("all_words.json",encoding='utf-8') as json_file:
    all_words = json.load(json_file)

with open("VocabList.N5.json",encoding='utf-8') as json_file:
    N5_data = json.load(json_file)
  