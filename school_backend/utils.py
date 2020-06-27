def hash(length=16):
    s = ''
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(length):
        s += alph[randint(0, len(alph) - 1)]