def hello(username):
    '''
    Returns uppercased username.
    :param username:
    :return:
    '''
    name = username.upper()
    print('locals', locals())
    return name

name = 'Ania'
lastname = 'Kowalska'


if __name__ == '__main__':
    print(hello(name))
    print('globals', globals())