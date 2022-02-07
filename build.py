from curses import A_HORIZONTAL, has_key
import openpyxl
import json
import requests

def convert_to_dict(lst, res_dct):
    for l in lst:
        if l[0] == 'all':
            continue
        if l[0] in res_dct:
            res_dct[l[0]]['freq_count'] += l[1]
            res_dct[l[0]]['freq_percent'] += l[2]
        else:
            res_dct[l[0]] = {'freq_count' : l[1], 'freq_percent' : l[2]}
    
    return res_dct


#open xl
output_name = 'kanji_excel.xlsx'
wb_obj = openpyxl.load_workbook(filename=output_name) 
sheet_ranges = wb_obj.active
#reset scores
if False:
    for row in range(1,2138):
        sheet_ranges['I' + str(row)] = 0
    wb_obj.save(filename=output_name)

#build dict
with open("aozora.json",encoding='utf-8') as json_file:
    aozora = json.load(json_file)
data = convert_to_dict(aozora, {})

with open("news.json",encoding='utf-8') as json_file:
    news = json.load(json_file)
data = convert_to_dict(news, data)

with open("twitter.json",encoding='utf-8') as json_file:
    twitter = json.load(json_file)
data = convert_to_dict(twitter, data)

with open("wikipedia.json",encoding='utf-8') as json_file:
    wikipedia = json.load(json_file)
data = convert_to_dict(wikipedia, data)

#


with open("kanjiapi_full.json",encoding='utf-8') as json_file:
    stroke_data = json.load(json_file)


stroke_data['kanjis']['溺 '] = {'stroke_count' : 15}

grade = {'G1': 200,'G2' : 190,'G3' : 180,'G4' : 170,'G5' : 160, 'G6' : 150, 'S' :140}

jlpt = {'N1': 200,'N2' : 190,'N3' : 160,'N4' : 120,'N5' : 100}

for row in range(2, 2138):
    kanji = sheet_ranges['B' + str(row)].value
    if kanji not in data:
        data[kanji] = {'freq_count' : 0, 
        'freq_percent' : 0.0}
    data[kanji]['study_word'] = sheet_ranges['C' + str(row)].value
    data[kanji]['furigana'] = sheet_ranges['D' + str(row)].value
    data[kanji]['translation'] = sheet_ranges['E' + str(row)].value
    data[kanji]['grade'] = sheet_ranges['F' + str(row)].value
    data[kanji]['jlpt'] = sheet_ranges['G' + str(row)].value
    

    data[kanji]['strokes']  = stroke_data['kanjis'][kanji]['stroke_count']
    
    data[kanji]['correct_guesses'] = 0
    data[kanji]['incorrect_guesses'] = 0


    x = data[kanji]
    freq_count = 0.0001 * x['freq_count']

    if(freq_count > 100):
        freq_count = 100
    data[kanji]['score'] = freq_count+(x['strokes']) + grade[x['grade']] + jlpt[x['jlpt']]


with open('all_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile)



