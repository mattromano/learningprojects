import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif SequenceMatcher(None, get_close_matches(w,data.keys())[0].lower(), w).ratio() == 1:
        return data[get_close_matches(w, data.keys())[0]]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead - Y/N" % get_close_matches(w,data.keys())[0])
        if yn.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == 'n':
            return 'Well sorry, I have no idea what you are looking for then'
        else:
            return "The options were Y & N, idk wtf you chose but it was wrong"

    else:
        return 'The word does not exist, please double check it.'

w = input('Enter Word: ')

output = (translate(w))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)