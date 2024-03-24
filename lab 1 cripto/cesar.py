import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ''
    for caracter in texto:
        if caracter.isalpha():  # Solo cifra letras, ignora otros caracteres
            if caracter.islower():
                nuevo_codigo = (ord(caracter) - ord('a') + corrimiento) % 26 + ord('a')
            elif caracter.isupper():
                nuevo_codigo = (ord(caracter) - ord('A') + corrimiento) % 26 + ord('A')
            texto_cifrado += chr(nuevo_codigo)
        else:
            texto_cifrado += caracter
    return texto_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cifrado_cesar.py <texto> <corrimiento>")
        sys.exit(1)
    
    texto_original = sys.argv[1]
    corrimiento = int(sys.argv[2])

    texto_cifrado = cifrar_cesar(texto_original, corrimiento)
    print(texto_cifrado)