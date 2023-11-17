digits = [1, 2, 3, 4, 5]


def decorator(func):

    def wrapper(*args):

        print(f'Before func: {func.__name__}')

        func(*args)

        print(f'After func: {func.__name__}')

    return wrapper

@decorator
def function_one(*args):
    for num in args:
        print(f'Hi number {num}')

@decorator
def good_luck(*args):
    my_list = []
    for num in args:
        if len(my_list) > 0:
            my_list.pop(0)
        my_list.append(num)
        print(my_list)




function_one(*digits)
good_luck(*digits)