#crie uma função que retorne o comprimento da maior sequencia consecutiva de um determinado elemento. 
'''
Exemplo: 90000, 0  -->  4
"abcdaaadse", "a"  -->  3
"abcdaaadse", "z"  -->  0
'''

def get_consective_items(items, key): 
    items = str(items)
    key = str(key)
    sequence_list = []
    for index, el in enumerate(items):
        if el == key:
            if len(sequence_list) == 0:
                sequence_list.append(el)
            else:
                if sequence_list[-1][0] == items[index-1]:
                    sequence_list[-1] += el
                else:
                    sequence_list.append(el)

    if sequence_list == []:
        return 0 
    return max([len(el) for el in sequence_list])


resultado1 = get_consective_items(90000, 0)
resultado2 = get_consective_items('abcdaaadse', 'a')
resultado3 = get_consective_items("abcdaaadse", 'z')

print(resultado1, resultado2, resultado3)