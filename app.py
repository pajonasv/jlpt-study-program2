import json

import datetime as dt

with open("all_data.json",encoding='utf-8') as json_file:

    all_data = json.load(json_file)

 

filtered_data = list()

freq = list()

def getScore(dic):

    return dic['score']

for kanji in all_data:

    if 'study_word' in all_data[kanji]:

        filtered_data.append(all_data[kanji])

        filtered_data[len(filtered_data)-1]['kanji'] = kanji

 

filtered_data.sort(key=getScore,reverse=True)

c=0

for d in filtered_data:

    if (d['correct_guesses']+0.0001)/(d['incorrect_guesses']+0.0001) > 5 and d['correct_guesses'] >= 5:

        c+=1

   

 

print("Total Kanji 'mastered' :", (c / len(filtered_data)*100), '%')

print(c, "/", len(filtered_data))

while True:

    next =filtered_data[0]

    print(next['kanji'])

    input()

    print(next['study_word'])

    print(next['furigana'])

    print(next['translation'])

    print("O : " , next['correct_guesses'] , " X : " , next['incorrect_guesses'])

    print("score :" , next['score'])

    print("z: Correct | x : Incorrect | else : Unsure")

    i = input()

    if(i == 'z'):

        filtered_data[0]["score"] -= 7

        filtered_data[0]["correct_guesses"] +=1

    elif(i == 'a'):

        filtered_data[0]["correct_guesses"] +=1

        filtered_data[0]["score"] -= 14

       

    elif(i == 'x'):

        filtered_data[0]["score"] -= 3

       

        filtered_data[0]["incorrect_guesses"] +=1

    else:

        filtered_data[0]["score"] -= 4.5

 

 

    all_data[next['kanji']]['score'] =filtered_data[0]['score']

    with open('all_data.json', 'w', encoding='utf-8') as outfile:

        json.dump(all_data, outfile)

    filtered_data.sort(key=getScore,reverse=True)

   

    print("----------------------------------------")
