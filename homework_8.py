# 31
def pwd_gen(length = 8):
    from random import choice
    char = list('_123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')

    return ''.join([choice(char) for x in range(length)])

def pwd_verification():
    import string
    tries = 0

    while tries < 1000:
        pwd = pwd_gen(12)

        comps = [0, 0, 0]
        for c in pwd:
            comps[0] |= c in string.ascii_lowercase
            comps[1] |= c in string.ascii_uppercase
            comps[2] |= c in string.digits

        if sum(comps) < 3:
            print("Dann leer")
            break
        else:
            print("OK: ", pwd)

        tries += 1

pwd_verification()

