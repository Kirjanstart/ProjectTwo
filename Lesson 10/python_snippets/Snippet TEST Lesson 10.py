import warnings


def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn('Опять этот Роберт...', category=RuntimeWarning)
    print(f'Hi there {person_name}')
warnings.simplefilter("error")


greet_person('Robert')

for i in range(10):
    print(f'i={i}')