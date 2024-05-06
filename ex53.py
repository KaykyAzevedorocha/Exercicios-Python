frase= str(input('digite uma frase:\n')).strip().upper()
palavras = frase.split()
junto= ''.join(palavras)
for letra in range(len(junto) -1 , -1, -1):
    print(junto[letra])
