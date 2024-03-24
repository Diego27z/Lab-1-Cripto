import sys
import time
import random
from scapy.all import IP, ICMP, send

def enviar_paquete_caracter(caracter):
   paquete = IP(dst="127.0.0.1")/ICMP(id=1)/(b'\x00' + caracter.encode() + bytes([random.randint(0, 255)]) + b'\x00\x00\x00\x00\x00\x00' + bytes(range(0x10, 0x38)))
   send(paquete)

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 enviar_paquete.py <texto>")
        sys.exit(1)
    
    texto = sys.argv[1]
    for caracter in texto:
        enviar_paquete_caracter(caracter)
        time.sleep(1)  # Esperar 1 segundo entre cada envío

if __name__ == "__main__":
    main()