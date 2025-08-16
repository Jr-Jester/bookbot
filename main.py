from stats import get_num_words, get_num_char, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def pretty_output(sorted_dic, filepath):
    print(f'''
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------''')
    print(f'Found {get_num_words(get_book_text(filepath))} total words')
    print('--------- Character Count -------')
    for i in sorted_dic:
        if list(i.values())[0].isalpha():
            print(f'{list(i.values())[0]}: {list(i.values())[1]}')
    print('============= END ===============')

def main():
    filepath = 'books/frankenstein.txt'
    sorted_dic = (get_sorted_dict(get_num_char(get_book_text(filepath))))
    pretty_output(sorted_dic, filepath)


main()
