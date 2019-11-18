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
    dicc = {}

    def json2register(self):
        """Descargo fichero json en el diccionario."""
        try:
            with open('registered.json', 'r') as jsonfile:
                self.dicc = json.load(jsonfile)
        # Me da igual cual sea la excepcion (error) sigo
        except():
            pass

    def register2json(self):
        """
        escribo la variable dicc
        en formato json en elfichero registered.json
        """
        with open('registered.json', 'w') as jsonfile:
            json.dump(self.dicc, jsonfile, indent=4)

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        # COmpruebo si ya esta creado el json
        self.json2register()

        milinea = ''
        for line in self.rfile:
            milinea += line.decode('utf-8')
        if milinea != '\r\n':
            print("El cliente nos manda ", milinea)
            # Quitamosos el expires: que no usamos con _
            (peticion, address, sip, _, expire) = milinea.split()
            if peticion == 'INVITE':
                print('es un invite')
                self.wfile.write(b"SIP/2.0 100 TRYING\r\n\r\n
                                   SIP/2.0 180 RING\r\n\r\n
                                   SIP/2.0 200 OK\r\n\r\n")
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
        PORTSERVER = int(sys.argv[1])
    except ValueError:
        sys.exit("Port must be a number")
    except IndexError:
        sys.exit("Usage: python3 server.py IP port audio_file")
    serv = socketserver.UDPServer(('', PORTSERVER), SIPRegisterHandler)

    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
