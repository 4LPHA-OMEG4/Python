def main():
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
    sentence = sentence.split()
    for letter in range(len(sentence)):
        i = sentence[letter]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[letter] = i + 'a'
        elif t(i) in lst:
            sentence[letter] = i[2:] + i[:2] + 'a'
        elif i.isalpha() == False:
            sentence[letter] = i
        else:
            sentence[letter] = i[1:] + i[0] + 'a'
    return ' '.join(sentence)


def t(str):
    return str[0] + str[1]


if __name__ == "__main__":
    x = main()
    print(x)
