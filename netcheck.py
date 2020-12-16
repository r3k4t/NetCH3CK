
import os
import sys
import urllib
os.system(chr(27)+"[32m")
os.system("clear")
os.system("figlet -f standard NetCH3CK")
print(chr(27)+"[33m"+"    Author : Rahat Khan Tusar(RKT)")
print(  chr(27)+"[33m"+"  Github : https://github.com/r3k4t/")
os.system(chr(27)+"[35m")
def connect(host='http://bing.com'):
    try:
        urllib.urlopen(host) 
        return True
    except:
        return False

print( 'Connected' if connect() else 'No Internet !' )