def genTable(head, body):
    """
    Função responsável por gerar uma tabela com os dados do head e body \n
    head = ['item1', 'item2', 'item3', ...]\n
    body = [
    \t['cel1', 'cel2', 'cel3', 'cel4']
    \t['cel1', 'cel2', 'cel3', 'cel4']
    \t...
    \t]\n
    """

    resH = '|  #  | '
    resB = ''
    divisor = '+' + '-' * 5 + '+' + '-'*34 + '+' + '-'*9 + \
        '+' + '-'*9 + '+' + '-'*9 + '+' + '-'*9 + '+' + '\n'
    res = divisor
    for i in range(len(head)):
        if i == 0:
            pass
        elif i == 1:
            resH += head[i].ljust(32, ' ') + ' | '
        else:
            resH += head[i].ljust(7, ' ') + ' | '
    resH += '\n' + divisor
    for data in body:
        for items in range(len(data) - 1):
            if items == 0:
                if len(data[items]) == 1:
                    resB += '|  ' + data[items] + '  | '
                elif len(data[items]) == 2:
                    resB += '| ' + data[items] + '  | '
                elif len(data[items]) == 3:
                    resB += '| ' + data[items] + ' | '
            elif items == 1:
                resB += data[items].ljust(25, ' ') + '\t | '
            else:
                resB += data[items].ljust(7, ' ') + ' | '

        resB += '\n'
    res += resH + resB
    res += divisor
    return res
