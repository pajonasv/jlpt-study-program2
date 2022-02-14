
import json
from jisho_api.sentence import Sentence

def getSentence(word):
    try:
        slash = word.find('/')
        if slash != -1:
            word = word[:slash]

        sentence = Sentence.request(word)
        if sentence == None:
            return
        sentence = sentence.dict()
        
        return sentence['data'][0]

    except:
        return


with open("VocabList.N5.json",encoding='utf-8') as json_file:
    N5_data = json.load(json_file)
  

all_dict = {}
for word in N5_data[1][1]['c'][4]:
    kanji = ""
    kana = ""
    definition = ""
    
    if len(word[1]) > 0:
        kana = word[1][0]['c'][0]['c']

    if len(word[0]) > 0:
        kanji = word[0][0]['c'][0]['c']
    else:
        kanji=kana
    if len(word[2]) > 0:
        for subword in word[2][0]['c']:
            if subword['c'] != []:
                definition += subword['c']
            else:
                definition += " "     
    if kanji != kana:
        all_dict[kanji] = {'kanji' : kanji, 'kana' : kana, 'meaning' : definition} 
    else:
        all_dict[kanji] = {'kana' : kana, 'meaning' : definition}
    
    sentence = getSentence(kanji)
    if getSentence(kanji) != None:
        all_dict[kanji]['sentence'] = sentence

    all_dict[kanji]['jlpt'] = 'N5'

N5_data = None
with open("VocabList.N4.json",encoding='utf-8') as json_file:
    N4_data = json.load(json_file)

for word in N4_data[1][2]['c'][4]:
    kanji = ""
    kana = ""
    definition = ""
    
    if len(word[1]) > 0:
        kana = word[1][0]['c'][0]['c']

    if len(word[0]) > 0:
        kanji = word[0][0]['c'][0]['c']
    else:
        kanji=kana
    if len(word[2]) > 0:
        for subword in word[2][0]['c']:
            if subword['c'] != []:
                definition += subword['c']
            else:
                definition += " "     
    if kanji != kana:
        all_dict[kanji] = {'kanji' : kanji, 'kana' : kana, 'meaning' : definition} 
    else:
        all_dict[kanji] = {'kana' : kana, 'meaning' : definition} 
    
    sentence = getSentence(kanji)
    if getSentence(kanji) != None:
        all_dict[kanji]['sentence'] = sentence

    all_dict[kanji]['jlpt'] = 'N4'

N2_data = None
with open("VocabList.N3.json",encoding='utf-8') as json_file:
    N3_data = json.load(json_file)



for word in N3_data[1][2]['c'][4]:
    kanji = ""
    kana = ""
    definition = ""
    
    if len(word[1]) > 0:
        kana = word[1][0]['c'][0]['c']

    if len(word[0]) > 0:
        kanji = word[0][0]['c'][0]['c']
    else:
        kanji=kana
    if len(word[2]) > 0:
        for subword in word[2][0]['c']:
            if subword['c'] != []:
                definition += subword['c']
            else:
                definition += " "     
    if kanji != kana:
        all_dict[kanji] = {'kanji' : kanji, 'kana' : kana, 'meaning' : definition} 
    else:
        all_dict[kanji] = {'kana' : kana, 'meaning' : definition} 
    
    sentence = getSentence(kanji)
    if getSentence(kanji) != None:
        all_dict[kanji]['sentence'] = sentence

    all_dict[kanji]['jlpt'] = 'N3'

N3_data = None

with open("VocabList.N2.json",encoding='utf-8') as json_file:
    N2_data = json.load(json_file)



for word in N2_data[1][2]['c'][4]:
    kanji = ""
    kana = ""
    definition = ""
    
    if len(word[1]) > 0:
        kana = word[1][0]['c'][0]['c']

    if len(word[0]) > 0:
        kanji = word[0][0]['c'][0]['c']
    else:
        kanji=kana
    if len(word[2]) > 0:
        for subword in word[2][0]['c']:
            if subword['c'] != []:
                definition += subword['c']
            else:
                definition += " "     
    if kanji != kana:
        all_dict[kanji] = {'kanji' : kanji, 'kana' : kana, 'meaning' : definition} 
    else:
        all_dict[kanji] = {'kana' : kana, 'meaning' : definition} 

    
    sentence = getSentence(kanji)
    if getSentence(kanji) != None:
        all_dict[kanji]['sentence'] = sentence

    
    all_dict[kanji]['jlpt'] = 'N2'


N2_data = None
with open("VocabList.N1.json",encoding='utf-8') as json_file:
    N1_data = json.load(json_file)  

for word in N1_data[1][2]['c'][4]:
    kanji = ""
    kana = ""
    definition = ""
    
    if len(word[1]) > 0:
        kana = word[1][0]['c'][0]['c']

    if len(word[0]) > 0:
        kanji = word[0][0]['c'][0]['c']
    else:
        kanji=kana
    if len(word[2]) > 0:
        for subword in word[2][0]['c']:
            if subword['c'] != []:
                definition += subword['c']
            else:
                definition += " "     
    if kanji != kana:
        all_dict[kanji] = {'kanji' : kanji, 'kana' : kana, 'meaning' : definition} 
    else:
        all_dict[kanji] = {'kana' : kana, 'meaning' : definition} 

    sentence = getSentence(kanji)
    if getSentence(kanji) != None:
        all_dict[kanji]['sentence'] = sentence

    all_dict[kanji]['jlpt'] = 'N1'

for word in all_dict:
    all_dict[word]['correct_guesses'] = 0
    all_dict[word]['incorrect_guesses'] = 0
    all_dict[word]['added'] = False
    all_dict[word]['my_score'] = 0

with open('all_words.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_dict, outfile)


