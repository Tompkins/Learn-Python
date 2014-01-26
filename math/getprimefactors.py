def getprimefactors(n):
    factorlist = []
    factor = 2
    while factor <=n:
        if n % factor == 0:
            if factor not in factorlist:
                factorlist.append(factor)
            n /= factor
        else:
            factor += 1
    return factorlist
    
