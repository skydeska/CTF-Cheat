#!/usr/bin/python3
import os,time,sys

def ctf():
        try:
                ctf_type = input("\x1b[38;5;46m[+]Quelle est la platforme de CTF 😀 du jour : \x1b[0m")
                if ctf_type == "THM" or ctf_type == "HTB" or ctf_type == "VULN":
                        ctf_name = input(f"\x1b[38;5;4m[+]Entrer le nom du CTF {ctf_type} du jour 😁 : \x1b[0m")
                        create_dir = os.system(f"mkdir /root/{ctf_type}/{ctf_name}")
                        car = ".."
                        while car != "..........":
                                cac = "."
                                sys.stdout.write("\r\x1b[38;5;136m[+] Creation du dossier en cours"+car+"\x1b[0m")
                                time.sleep(0.5)
                                sys.stdout.write("\x1b[38;5;136m\r[*] Creation du dossier en cours"+car+"\x1b[0m")
                                car += cac
                                time.sleep(0.5)
                        print ("\n\x1b[38;5;226m[+] Dossier creer avec succes ✅✅✅\x1b[0m")
                        print (f"\x1b[38;5;129mle chemin du dossier: cd /root/{ctf_type}/{ctf_name} && clear  \nBon chance a toi pour le CTF {ctf_name} de {ctf_type} 😎\x1b[0m")
                else:
                        print ("\r\x1b[38;5;196m\rErreur cette platforme n'a pas ete initialisé 😞 je regrette !\x1b[0m")
        except KeyboardInterrupt:
                print ("\r\x1b[38;5;196mAction annulé par l'utilisateur                                              \x1b[0m")

ctf()
