
def stringConsistRusOnly(text):
    try:
        alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        for symb in text:
            if symb.lower() not in alphabet:
                raise TypeError
    except TypeError:
        return False
    return True

def stringConsistEngOnly(text):
    try:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        for symb in text:
            if symb.lower() not in alphabet:
                raise TypeError
    except TypeError:
        return False
    return True