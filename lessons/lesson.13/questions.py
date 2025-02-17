from random import choice


with open('names.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    lucky = choice(names)
    print('This question for...')
    print('*'*10)
    print(lucky.title())
    print('*'*10)
