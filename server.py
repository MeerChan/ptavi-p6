#!/usr/bin/python3
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """

        milinea = ''
        for line in self.rfile:
            milinea += line.decode('utf-8')
            print("El cliente nos manda ", milinea)
        if milinea != '\r\n':
            print("El cliente nos manda ", milinea)
            # Quitamosos el expires: que no usamos con _
            (peticion,sipLOGIN_ip,port) = milinea.split()
            if peticion == 'INVITE':
                print('es un invite')
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n"
                                 + b"SIP/2.0 180 Ringing\r\n\r\n"
                                 + b"SIP/2.0 200 OK\r\n\r\n")
            elif peticion == 'BYE':
                print('es unbyeee')
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            else:
                print('nunca deberia llegar a aqui si se usa mi cliente')
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usage: python3 server.py IP port audio_file")
    try:
        IPSERVER = sys.argv[1]
        PORTSERVER = int(sys.argv[2])
        AUDIO = sys.argv[3]
    except ValueError:
        sys.exit("Port must be a number")
    except IndexError:
        sys.exit("Usage: python3 server.py IP port audio_file")
    serv = socketserver.UDPServer((IPSERVER, PORTSERVER), SIPRegisterHandler)

    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
