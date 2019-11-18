#!/usr/bin/python3
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys
# Constantes. Dirección IP del servidor,Puerto del servidor y
# Linea
try:
    METODO = sys.argv[1]
    if METODO.upper() != ('INVITE' or 'BYE'):
        print()
        sys.exit("Method must be INVITE or BYE")
    LOGIN_IP = sys.argv[2].split(':')[0] #login@ip (me estoy quedando con todo junto)
    IPSERVER = LOGIN.split('@')[1]#la necesito para concetarme solamente
    PORTSERVER = int(sys.argv[2].split(':')[1])

except ValueError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")
except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IPSERVER, PORTSERVER))
    print("Enviando:", METODO.upper() + ' sip:' + LOGIN_IP + ' SIP/2.0')
    # Se lo enviamos al servidor
    my_socket.send(bytes(METODO.upper() + ' sip:' + LOGIN_IP + ' SIP/2.0\r\n'
                            + b'\r\n\r\n'))
    data = my_socket.recv(1024)
    recibido = data.decode('utf-8')
    print('Recibido -- ', data.decode('utf-8'))

    if METODO.upper() == 'INVITE':
         if recibidob[2] == 'Trying' and recb[5] == "Ringing" and recb[8] == "OK":
            my_socket.send(bytes('ACK sip:' + ADRESS + ' SIP/2.0', 'utf-8')
                           + b'\r\n\r\n')
    if METODO == 'BYE':


print("Socket terminado.")
