def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_num_char(text):
    text = text.lower()
    char = {}
    for i in text:
        if i not in char:
            char[i] = 1
        else:
            char[i] += 1
    return char

def sort_on(items):
    return items['num']

def get_sorted_dict(dic):
    new_list_of_dic = []
    for i in dic:
        new_list_of_dic.append({'char':i, 'num':dic[i]})
    new_list_of_dic.sort(key=sort_on, reverse=True)
    return new_list_of_dic


