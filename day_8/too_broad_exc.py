digits = {
    'cztery': 4,
    'dwa': 'dwa'
}

digit = input('Podaj liczbe: ')

try:
    result = digits[digit] - digits['dwa']
except KeyError as keyerror:
    print(f'nie ma takiego klucza jak: {keyerror}')
except TypeError as typeerror:
    print(f'typerror: {typeerror}')
except Exception as exc:
    print('mega fakap')
finally:
    raise ValueError('hahahah looser')

