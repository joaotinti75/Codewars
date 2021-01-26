#crie uma função que retorne o único elemento diferente de um array
#exemplo: input = [1,1,1,2,1,1,1], output = 2
def find_uniq(arr):
    arr_bol = [num == arr[0] for i,num in enumerate(arr)]

    if arr_bol.count(True) > 1:
        return arr[arr_bol.index(False)]
    else:
        return arr[arr_bol.index(True)]


arr = [1,1,1,1,1,1,1,1,1,1,5]

n = find_uniq(arr)
print(n)

