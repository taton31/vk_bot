import config
import re


with open(config.path_to_list_verb, 'r') as inp:
    verbs=inp.read().strip()
    verbs = re.sub(r'\s+', ' ', verbs)
    verbs = verbs.split(' ')

def get_verb(tmp):
    tmp=tmp.lower()
    if tmp in verbs:
        ind = verbs.index(tmp)
        if ind % 3 != 0:
            return 'Это правильный глагол\nИли допущена орфографическая ошибка'
        result = str(verbs[ind+1]) + ' ' + str(verbs[ind + 2])
        return result
    else:
        return 'Это правильный глагол\nИли допущена орфографическая ошибка'
