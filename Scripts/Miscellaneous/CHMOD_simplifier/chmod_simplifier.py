notation = {
    '---': '0',
    '--x': '1',
    '-w-': '2',
    '-wx': '3',
    'r--': '4',
    'r-x': '5',
    'rw-': '6',
    'rwx': '7'
}

def perm_to_num(symbolic):
    '''
        Convert symbolic permission notation to numeric notation.
    '''

    if len(symbolic) == 9:
        group = (symbolic[:-6], symbolic[3:-3], symbolic[6:])
        try:
            numeric = notation[group[0]] + notation[group[1]] + notation[group[2]]
        except:
            numeric =  "Invalid Symbolic Representation!"
    else:
        numeric = "Symbolic input should be for lengh 9!"

    return numeric

def num_to_perm(num):
    '''
        Convert number permission notation to symbolic notation.
    '''

    num = str(num)
    if len(num) == 3:
        group = (num[0], num[1], num[2])
        symbolic = ""

        for key, value in notation.items():
            for g in group:
                if int(g) > 8 or int(g) < 0:
                    symbolic = "Invalid Numerical Representation!"
                elif g == value:
                    symbolic = symbolic + key
    else:
        symbolic = "Number input should be of length 3!"

    return symbolic


print(num_to_perm(700))