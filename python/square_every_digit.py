#crie uma função que eleve cada numero ao quadrado e concatene o resultado 
#exemplo: input=9119, output=811181

def square_digits(num):
    num = str(num)
    n = ''
    for i in range(len(num)):
        n += str(int(num[i])**2)

    return int(n)



