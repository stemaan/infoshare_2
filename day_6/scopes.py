name = 'Ola'

def hello(username):
    '''
    Returns uppercased username.
    :param username: str
    :return: str.upper()
    '''
    global name
    name = username.upper()
    lastname = 'Kowalski'
    return name


data = input('Podaj imie: ')
uppercased = hello(data)
print(uppercased)
print(name)