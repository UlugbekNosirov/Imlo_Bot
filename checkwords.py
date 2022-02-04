from uzwords import words
from difflib import get_close_matches


def check_words(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    avalable = False

    if word in words:
        avalable = True
        matches = word
    elif 'ҳ' in word:
        word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    return {'avalable': avalable, 'matches': matches}


if __name__ == '__main__':
    print(check_words('ҳато '))
