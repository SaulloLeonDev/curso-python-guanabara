def notas(*resp, sit=False):
    """_summary_

    Args:
        sit (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    lista = list()
    cont = total = valor = 0
    for i, v in enumerate(resp, start = 1):
        valor += v
        cont += 1
        total += 1
    maior = max(resp)
    menor = min(resp)
    media = valor / total
    resp = dict()
    resp['total'] = total
    resp['maior'] = maior
    resp['menor'] = menor
    resp['media'] = media
    if sit == True:
        if resp['media'] > 7:
            resp['situacao'] = 'Boa'
        if resp['media'] < 7 and resp['media'] > 5:
            resp['situacao'] = 'Razoavel'
        if resp['media'] < 5:
            resp['situacao'] = 'Ruim'
    return resp

# Programa Principal
resp = notas(4.5, 6, 4.2, 5.7, 4, sit=True)
print(resp)
