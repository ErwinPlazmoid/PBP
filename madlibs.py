# # string concatenation
# # create a string that says: 'bla bla bla _____'

hero = 'Zhongli'     # str variable

# possible way's to do so
print('Rex Lapis is  ' + hero)
print('Rex Lapis is {}'.format(hero))
print(f'Rex Lapis is {hero}')

heroName = input('Hero name: ')
noun = input('Noun: ')
verb = input('Verb: ')
famousPerson = input('Famous person: ')

madlib = f'{heroName} is broke! Because he doesn\'t understand {noun}!  \
Try to {verb} like {famousPerson}'
print(madlib)