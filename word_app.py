import json
import pykakasi

my_words = None

def checkIfJustKana(word,except_):
    all_kana ="""
    あいうえお
    かきくけこ
    がぎぐげご
    さしすせそ
    ざじずぜぞ
    たちつてと
    だぢづでど
    はひふへほ
    ばびぶべぼ
    ぱぴぷぺぽ
    なにぬねの
    まみむめも
    らりるれろ
    やゆよ
    わを
    ん
    っ
    ゃゅょ

    """
    for char_ in word:
        if char_ == word:
            continue
    
        if char_ not in all_kana:
            return False
    return True


def getWords():
    with open("all_data.json",encoding='utf-8') as json_file:
        all_kanji = json.load(json_file)
    
    kanji_list = []
    for kanji in all_kanji:
        if 'correct_guesses' not in all_kanji[kanji]:
            continue
        if (all_kanji[kanji]['correct_guesses']+0.0001)/(all_kanji[kanji]['incorrect_guesses']+0.0001) > 5 and all_kanji[kanji]['correct_guesses'] >= 5:
            kanji_list.append(all_kanji[kanji]['kanji'])
    
    all_kanji = None

    with open("all_words.json",encoding='utf-8') as json_file:
        all_words = json.load(json_file)

    to_return = []
    combined_kanji = ""
    for word in all_words:
        if 'added' not in all_words[word]:
            continue
        if all_words[word]['added'] == True:
            to_return.append(all_words[word])
        
        else:
            for kanji in kanji_list:
                if 'kanji' not in all_words[word]:
                            continue
                if kanji in all_words[word]['kanji']:
                    
                    if checkIfJustKana(word,kanji):
                        to_return.append(all_words[word])
                        break
                    for kanjiB in kanji_list:
                        
                        if kanji in all_words[word]['kanji'] and kanjiB in all_words[word]['kanji']:
                            all_words[word]['added'] = True
                            to_return.append(all_words[word])
                            break
                    else:
                        continue
                    break
    with open('all_words.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_words, outfile)
    return to_return



def furiganaGame():
    kks = pykakasi.kakasi()
    for word in my_words:
        input_ = input(word['kanji'])
        comp = kks.convert(word['kana'])[0]['passport']
        if input_ == comp:
            print("Correct!")
        else:
            print(word['kana'])

        print("---------------------------------------------")


kks = pykakasi.kakasi()
print(kks.convert('橋')[0])
my_words = getWords()
furiganaGame()





