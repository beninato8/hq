import pytesseract
from PIL import Image
from apiclient.discovery import build
import pprint
import json
from unidecode import unidecode
import config
<<<<<<< HEAD
import pyscreenshot
=======
>>>>>>> 94a7141003b1cb665a47145682beb2523b63fe13

class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        if type(object) is str:
            return (object.encode('utf8'), True, False)
        return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api)
    res = service.cse().list(q=search_term, cx=cse, **kwargs).execute()
    return res

def google(question, answer):
    data = {}
    data['Total Hits'] = 0
    data['Title'] = 0
    data['Body'] = 0
    data['Title Text'] = []
    data['Body Text'] = ''
    res = google_search(question + answer, api, cse, num=10)
    data['Total Hits'] = res['searchInformation']['totalResults']
    for i, s in enumerate(res['items']):
        data['Title'] += countL(s['title'].lower(), answer.lower())
        data['Body'] += countL(s['snippet'].lower(), answer.lower())
        data['Title Text'].append(unidecode(s['title']))
        if i == 0:
            data['Body Text'] = unidecode(s['snippet'][:min(len(s['snippet'].lower()), 70)]).replace('\n', '')
    return data

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def countL(text, words):
    words = [x for x in words.split() if x.lower() not in ('the', 'a')]
    num = 0
    for word in words:
        num += text.count(word)
    return num

<<<<<<< HEAD
screenshot = pyscreenshot.grab(bbox=(844,120,1264,535))
screenshot.save('hq.png')
=======
>>>>>>> 94a7141003b1cb665a47145682beb2523b63fe13
text = pytesseract.image_to_string(Image.open('hq.png'))
print(unidecode(text) + '\n')
answers = unidecode(text[text.index('?')+1:])
question = text.split('?')[0] + '?'
question = unidecode(' '.join(question.split('\n'))).replace("\"", "")
a_list = answers.split('\n')
a_list = [x.replace("\"", "") for x in a_list if x not in ('\n', '', '\'', '\"','  ')]

manual = False
<<<<<<< HEAD
# manual = True
if manual:
    question = 'Which living organism has more teeth?'
    a_list = ['Snail', 'Human Child', 'Snake']

cse = config.cse
api = config.api
=======
#manual = True
if manual:
    question = 'CRISPR is a tool geneticists use to do what?'
    a_list = ['Overcook chicken', 'Edit human genes', 'Store lettuce']

cse = config.cse
api = config.api_personal_2
>>>>>>> 94a7141003b1cb665a47145682beb2523b63fe13

print(question)
print('\n' + str(a_list) + '\n')
"""
#search_results is list of dictionaries
search_results = google_search(question, api, cse, num=10)
results_info = search_results['searchInformation']
print(results_info)
results_list = search_results['items']
results_url = search_results['url']
#print(results_info['totalResults'])
for i, result in enumerate(results_list):
    break;
    print('********************************')
    print(i+1)
    print(result['title'].encode('utf-8'))
    print(result['snippet'].encode('utf-8'))
    #print(result)
    #print(json.dumps(result, indent=2))
    #MyPrettyPrinter().pprint(results_list)
"""
a_score = {}
for answer in a_list:
    print('********************************')
    print(answer)
    a_results = google(question, answer)
    k = list(a_results.keys())[:-2]
    hits = a_results[k[0]]
    title = a_results[k[1]]
    body = a_results[k[2]]
<<<<<<< HEAD
    score = (max(1, int(hits)))/10 + 120*(max(1, (6*int(title))) * (max(1, 4*int(body))))/100
    for key in k:
        print(key + ': ' + str(a_results[key]) + '    ', end="")
    print('\n' + str(a_results['Title Text'][0:2]))
    print(a_results['Body Text'])
    a_score[answer] = score

num = dict(sorted(a_score.items(), key=lambda x: x[1]))
for k, v in num.items():
    print(k, v)

biggest = keywithmaxval(a_score)
print('\n' + biggest)
=======
    score = (max(1, int(hits)))/10 * (3*max(1, (int(title))) * (2*max(1, int(body)))/100)
    for key in k:
        print(key + ': ' + str(a_results[key]))
    print(a_results['Title Text'][0:2])
    print(a_results['Body Text'])
    a_score[answer] = score

for key in a_score:
    print(key + ': ' + str(a_score[key]))
biggest = keywithmaxval(a_score)
for i in range(20):
    print(biggest)
>>>>>>> 94a7141003b1cb665a47145682beb2523b63fe13
