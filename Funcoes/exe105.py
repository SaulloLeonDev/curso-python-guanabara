def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >=5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'Ruim'
    return r
    
resp = notas(4.5, 6, 4.2, 5.7, 4, sit=True)
print(resp)    

