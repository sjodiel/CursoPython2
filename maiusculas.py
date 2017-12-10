def maiusculas(frase):
    pos = 0
    string1 = ''
    while pos < len(frase):
        if ord(frase[pos]) >= 65 and ord(frase[pos]) <=90:
            string1 += frase[pos]
        pos += 1
    return string1




#print(maiusculas('Programamos em python 2?'))
# deve devolver 'P'

#print(maiusculas('Programamos em Python 3.'))
# deve devolver 'PP'

#print(maiusculas('PrOgRaMaMoS em python!'))
# deve devolver 'PORMMS'