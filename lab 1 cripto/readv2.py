import sys
from scapy.all import rdpcap
from collections import Counter

def obtener_byte_más_significativo(paquete):
    if 'ICMP' in paquete:
        icmp_paquete = paquete['ICMP']
        if 'Raw' in icmp_paquete:
            datos_crudos = icmp_paquete['Raw'].load
            if datos_crudos:
                return datos_crudos[0]
    return None


def descifrar_cesar(texto, corrimiento):
    texto_descifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                nuevo_caracter = chr(((ord(caracter) - corrimiento - 65) % 26) + 65)
            else:
                nuevo_caracter = chr(((ord(caracter) - corrimiento - 97) % 26) + 97)
            texto_descifrado += nuevo_caracter
        else:
            texto_descifrado += caracter
    return texto_descifrado

def main(nombre_archivo):
    paquetes = rdpcap(nombre_archivo)
    payload = "".join(chr(obtener_byte_más_significativo(paquete)) for paquete in paquetes if obtener_byte_más_significativo(paquete) is not None)

    # Calcular frecuencia de letras en español
    frecuencia_letras_español = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    probabilidades = {}

    for corrimiento in range(26):
        texto_descifrado = descifrar_cesar(payload, corrimiento)
        recuento_letras = Counter(texto_descifrado.upper())
        total_letras = sum(recuento_letras.values())
        puntaje = 0
        for letra, frecuencia in recuento_letras.items():
            if letra in frecuencia_letras_español:
                indice = frecuencia_letras_español.index(letra)
                puntaje += frecuencia * (1 / (indice + 1))
        probabilidades[corrimiento] = puntaje / total_letras

    max_prob_corrimiento = max(probabilidades, key=probabilidades.get)
    for corrimiento, probabilidad in probabilidades.items():
        if corrimiento == max_prob_corrimiento:
            print(f"\033[92m{corrimiento}  {descifrar_cesar(payload, corrimiento)}\033[0m")
        else:
            print(f"{corrimiento} {descifrar_cesar(payload, corrimiento)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python decode_icmp.py archivo.pcapng")
    else:
        main(sys.argv[1])
