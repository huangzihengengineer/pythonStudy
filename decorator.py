@log('s')
def print_now():
    print('2018-05-15')


f = print_now

print(f.__name__)

def log(ii):
    print(ii)
