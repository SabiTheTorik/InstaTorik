import os
import sys

os.system("cls")

os.system("color a")

print(r"""

 _____ _   _  _____ _____ ___  
|_   _| \ | |/  ___|_   _/ _ \ 
  | | |  \| |\ `--.  | |/ /_\ \
  | | | . ` | `--. \ | ||  _  |
 _| |_| |\  |/\__/ / | || | | |
 \___/\_| \_/\____/  \_/\_| |_/
                               
                               
 _____ ___________ _____ _   __
|_   _|  _  | ___ \_   _| | / /
  | | | | | | |_/ / | | | |/ / 
  | | | | | |    /  | | |    \ 
  | | \ \_/ / |\ \ _| |_| |\  \
  \_/  \___/\_| \_|\___/\_| \_/


Insta Torik Hacker Aracına Hoşgeldiniz!!!

Yardım için help yazınız.

Çıkış Yapmak için Ctrl + C tuşlarına basınız.
""")

mode = input("""
modlar: 0 = 32 bot
        1 = 16 bot
        2 = 8 bot
        3 = 4 bot

Mod Giriniz: """)


username = input("""
Hedefinizin Instagram Kullanıcı Adını Yazınız: """)


wordlist = input("""
Olası Şifrelerin Bulunduğu(Wordlist) Dosya Konumunu Yazınız yada
Bu Dosyanın İçine Atarak Sadece Dosya İsmini Atınız

Dosya Konumu: """)

if mode and username and wordlist != "x" or "99":
    os.system(f"instagram.py -m {mode} {username} {wordlist}")