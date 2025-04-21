#!/usr/bin/env python3
# coding: utf-8

from googlesearch import search
import time
import sys

# ASCII Art Banner
banner = """
    ▓█████▄  ▒█████   ██▀███   ██ ▄█▀  ██████    ▓█████▓██   ██▓▓█████
    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒    ▓█   ▀ ▒██  ██▒▓█   ▀
    ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄      ▒███    ▒██ ██░▒███
    ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄
    ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒   ░▒████▒ ░ ██▒▓░░▒████▒
    ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
    ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░    ░ ░  ░▓██ ░▒░  ░ ░  ░
    ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░        ░   ▒ ▒ ░░     ░
    ░        ░ ░     ░     ░  ░         ░        ░  ░░ ░        ░  ░
    ░                                                  ░ ░  v1.0
"""

for col in banner:
    print(f"\033[91m{col}", end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = """
    Author: Muhammad Arya Arjuna Habibullah | AryzXploit
    Github: https://github.com/AryzXploit
    Website: https://AryzXploit.com
    Twitter: https://twitter.com/aryzXploit
    Telegram: https://t.me/aryzXploit
"""
for col in x:
    print(f"\033[94m{col}", end="")
    sys.stdout.flush()
    time.sleep(0.0040)

print("\n\t\tHi there, Shall we play a game..? 😃\n")

def main():
    domain = input("\n[+] Masukkan domain target (contoh: nasa.gov): ").strip()
    jumlah = int(input("[+] Berapa banyak hasil per dork?: "))

    simpan = input("[+] Mau save hasil ke file? (Y/N): ").strip().lower()
    nama_file = None
    if simpan == 'y':
        nama_file = input("[+] Masukkan nama file (contoh: hasil.txt): ").strip()

    dorks = [
        f"site:{domain} drive.google.com/drive/u/0/folders/",
        f"site:{domain} docs.google.com/spreadsheets/d/",
        f"site:{domain} docs.google.com/document/d/"
    ]

    print("\n[+] Mulai Dorking...\n")

    hasil_semua = []

    for dork in dorks:
        print(f"[*] Dork: {dork}\n")
        try:
            hasil = search(dork, num_results=jumlah)
            for idx, url in enumerate(hasil, 1):
                print(f"[{idx}] {url}")
                hasil_semua.append(url)
        except Exception as e:
            print(f"[!] Error saat search dork: {dork}\n    Error: {e}")
        print("\n" + "-"*60 + "\n")
        time.sleep(1)

    if nama_file:
        with open(nama_file, "w") as file:
            for url in hasil_semua:
                file.write(url + "\n")
        print(f"\n[+] Semua hasil tersimpan di file: {nama_file}")

    print("\n[+] Dorking selesai!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Proses dihentikan oleh pengguna.")
        sys.exit(1)
