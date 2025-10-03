#!bin/python

#importing modules
import sys
import socket
import subprocess
import argparse
import threading

class scanner:
    def __init__(self, args):
       self.args = args
       self.buffer = ""

       if self.args.tcp:
           self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       elif self.args.udp:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        if self.args.tcp:
            self.tcp_scan()


    def tcp_scan(self):
        print(f"[*] Starting TCP scan on {self.args.target} ...")

        # If a specific port is given
        if self.args.port:
            self._check_tcp_port(self.args.port)
        else:
            for i in range(1, 1001):
                self._check_tcp_port(i)

    def _check_tcp_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect((self.args.target, port))  # connect_ex returns 0 if success
            if result == 0:
                print(f"[+] TCP Port Open: {port}")
            else:
                print("not open")
            sock.close()
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ROHANS PORT SCANNER")

    parser.add_argument("-t", "--target", help="Target machine IP/DOMAIN")
    parser.add_argument("-p", "--port", type=int, help="Scan specific port")
    parser.add_argument("--tcp", action="store_true", help="Enable TCP port scan 1 to 1000")
    parser.add_argument("--udp", action="store_true",  help="Enable UDP port scan 1 to 1000")
    
    args = parser.parse_args()

    print(args.target)

    nport = scanner(args)
    nport.run()
