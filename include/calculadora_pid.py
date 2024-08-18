def pid():
    x = float(input('Digite quanto foi recebido: R$ '))
    p = x * 0.18
    i = x * 0.42
    d = x * 0.4 

    print('''
        Poupança: R$ {:,.2f}
        Investimentos : R$ {:,.2f}
        Débito : R$ {:,.2f}
    '''.format(p, i, d))
    return x
