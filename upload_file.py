#!/usr/bin/python3
import os,sys

try:
        file = sys.argv[1]
        ip = os.system("ifconfig | grep 'inet' -w | cut -d ' ' -f 10 > /tmp/test")

        ips = open("/tmp/test", "r")
        for ip in ips:
                ip = ip.strip("\n")
                print (f"\nwget http://{ip}/{file}\n")
        os.system("python3 -m http.server 80 ")
        if file == "":
                os.system(f"python3 -m http.server 80")

except :
        script = sys.argv[0]
        print (f"usage :\n\t{script} <file_name> ")
