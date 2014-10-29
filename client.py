#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
#Excepciones
try:
    # Dirección IP del servidor.
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    # Si quieres METHOD= sys.argv[3]
    EXPIRES = int(sys.argv[5])
except IndexError:
    sys.exyt(Usage: client.py ip puerto register sip_address expires_value)
except ValueError:
    sys.exit(Usage: client.py ip puerto register sip_address expires_value)

# Contenido que vamos a enviar
#En tu línea no tienes que enviar el puerto y la dirección IP,
# con sería 4 porque tienes que añadir el Expires
con = 3
linea = ""
while con < len(sys.argv):
    linea = linea + sys.argv[con] + " "
    con = con + 1

LINE = linea

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
