import os
import time
import sys

#ini adalah animasi
def animasi():
    for x in range(20):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

#ini adalah logo
def logo():
    print("""
\033[44;1mHello Dunia Termux Lovers\033[00;1m
\033[34;1m（\033[35;1m；\033[36;1m￣\033[32;1mェ\033[36;1m￣\033[34;1m）\033[32;1mTema Linux
  \033[37;1m[\033[32;1mAuthor:Tegar_ID\033[37;1m]
\033[37;1m[\033[32;1mDunia Termux Developer\033[37;1m]
""")

# menu main

def main():
    os.system("clear")
    logo()
    print("\033[36;1m[\033[32;1m1\033[36;1m] \033[32;1mPasang Tema")
    print("\033[36;1m[\033[32;1m2\033[36;1m] \033[32;1mKembali\n")
    pilih()

# aktivitas menu pilihan
def pilih():
    pilih = input("\033[34;1mPilih Nomor \033[36;1m: \033[37;1m")
    if pilih == "":
        print("isi dulu gan")
        time.sleep(2)
        os.system("clear")
        main()
    elif pilih == "1":
        pasang()
    elif pilih == "2":
        kembali()
    else:
        print("nomor",pilih,"tidak ada")
        time.sleep(2)
        main()

# aktivitas memasang tema
def pasang():
    nama = input("Masukan Nama Anda (bebas) : ")
    tema = open(".bashrc", 'w')
    tema.write("""
#Created By Awnsntt
clear
echo "
\033[31;1m█████████████████   \033[37;1m[\033[41;1mAlwan Suesanto\033[00;1m\033[37;1m]
\033[31;1m█████████████████
\033[37;1m█████████████████ \033[37;1m[\033[44;1mWe Are Indonesian Cyber\033[00;1m\033[37;1m]
\033[37;1m█████████████████"
echo ""
PS1='\n\[\033[0;92m\]%s\[\033[00m\]@\[\033[0;92m\]root\[\033[0;96m\]:${PWD/*\//}\[\033[00m\](\#)\[\033[0;92m\]~#\[\033[00m\] '
"""% nama)
    tema.close()
    os.system("rm -rf $HOME/.bashrc")
    os.system("mv .bashrc $HOME")
    os.system("rm -rf $HOME/.termux")
    os.system("mkdir $HOME/.termux")
    os.system("cp colors.properties $HOME/.termux")
    os.system("cp font.ttf $HOME/.termux")
    os.system("cp termux.properties $HOME/.termux")
    animasi()
    print("\n\033[43;1mTema Berhasil Terpasang\033[00;1m")
    print("\n\033[42;1mJangan Lupa Follow instagram @awnsntt_\033[00;1m")
    login = input("\033[32;1m[Enter Untuk Melihat Tema]\n")
    os.system("termux-reload-settings")
    os.system("login")

def kembali():
    os.system("clear")
    exit("\033[34;1mJangan Lupa Follow instagram @awnsntt_:)")
main()
