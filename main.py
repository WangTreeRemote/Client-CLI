version = "1.1.1"
it_version = 10004
testmode = False
print("loading...",end='\r')
import socket
import sys
import locale
import time
import os
import json
import random
import shutil
try:
    import lang
    default_locale = locale.getdefaultlocale()
    try:
        exec(f"ulp = lang.{default_locale[0].lower()}")
    except:
        ulp = lang.en_us
        print(f"WT language file is missing '{default_locale[0].lower()}', so this time it will start in 'en_us'")
    #if default_locale[0].lower() == "en_us":
    #    ulp = lang.en_us
    #else:
    #    ulp = lang.zh_cn
except:
    print('''
A fatal error has occurred:
Unable to load "lang.py"

Please give feedback on Github issues:
https://github.com/Squirrel963/WangTree/issues

Info:
''')
    WTCv = globals()
    for Ckey in list(WTCv.items()):
        print(f"{Ckey}")
    www = input("Press enter to exit...")
    sys.exit(1)
from colorama import Fore, Style
try:
    from Crypto.Cipher import AES
except:
    appl = input("Crypto未安装，您希望现在安装它吗？(y/n)")
    if appl == "y":
        os.system("pip uninstall crypto pycryptodome")
        os.system("pip install pycryptodome")
        print("正在载入需要库...",end='\r')
        from Crypto.Cipher import AES
    else:
        sys.exit(1)
try:
    import tool_back
    Isinstall_toolback = True
except:
    Isinstall_toolback = False
socket_client = socket.socket()
Nolog = "localhost"
Nosets = ""
fm = "File_Manager"
login_name = Nolog
sets = Nosets
ip = socket.gethostbyname(socket.gethostname())
max_bytes = 8192
logined = False
rebacked = False
ref_auto = False
randkey = str(random.randint(1000000000000000,9999999999999999))

server_command = ["cmd","login","key","volue","lock"]

helps = ulp.helps

till = [
"__        __                      _____",
"\ \      / /  __ _  _ __    __ _ |_   _| _ __   ___   ___ ",
" \ \ /\ / /  / _` || '_ \  / _` |  | |  | '__| / _ \ / _ |",
"  \ V  V /  | (_| || | | || (_| |  | |  | |   |  __/|  __/",
"   \_/\_/    \__,_||_| |_| \__, |  |_|  |_|    \___| \___|",
"                           |___/"
]

def apple(text):
    appl = input(Fore.RED + f"[ {ulp.level_warn} ] {text} [y/n] ")
    print(Style.RESET_ALL, end="")
    if appl.lower() == "y":
        return True
    else:
        return False

def get_window_size():
    terminal_width = shutil.get_terminal_size().columns
    return terminal_width

def max_word_size(words):
    avg_word_length = sum(len(f) for f in words) // len(words)
    word_per_line = get_window_size() // (avg_word_length + 1)
    return word_per_line

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)

def aes(text):
    password = randkey.encode("utf-8")
    atext = add_to_16(text)
    aes = AES.new(password,AES.MODE_ECB)
    en_text = aes.encrypt(atext)
    print("密文：",en_text)
    return en_text

def unaes(text):
    password = randkey.encode("utf-8")
    atext = add_to_16(text)
    aes = AES.new(password,AES.MODE_ECB)
    den_text = aes.decrypt(atext)
    print("明文：",den_text)
    return den_text

def restart():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def index():
    print("-----------------------              ")
    print(Fore.BLUE,end='\r')
    for t in till:
        print(t)
    print(Style.RESET_ALL,end='\r')
    print(f"{ulp.system_title} v{version}")
    print(f"{ulp.system_ip}{ip}")
    print(f"{ulp.system_it}{it_version}")
    print(f"{ulp.system_size}{get_window_size()}")
    print(f"{ulp.system_lang}{default_locale[0]}")
    print(f"{ulp.system_aes}{randkey}")
    print(f"{ulp.system_test}{testmode}")
    print(f"{ulp.system_pack}{Isinstall_toolback}")
    print("-----------------------")

def connect_server(server_ip):
    global login_name,logined,server_command
    server = server_ip.split(" ")
    if logined:
        print(Fore.YELLOW + f"[ {ulp.level_error} ] {ulp.warn_logined}")
    else:
        try:
            #print("解析命令中...")
            s_ip = server[0]
            #print(s_ip)
            if len(server) >= 2:
                s_port = int(server[1])
            else:
                s_port = 200
            #print(s_port)
            print(f"{ulp.system_try}...")
            socket_client.connect((s_ip, s_port))
            login_name = s_ip
            logined = True
            print(f"{ulp.system_suc}{login_name}")
            socket_client.send("dataget".encode("UTF-8"))
            try:
                sit_info = json.loads(socket_client.recv(2048).decode("UTF-8"))
                sit_version = sit_info["it"]
                print(f"+-{ulp.info_it}")
                nomuch = False
                for i in server_command:
                    if not i in sit_info["wl"]:
                        print(Fore.RED + f"    {ulp.warn_server}'{i}'")
                        print(Style.RESET_ALL, end="")
                        nomuch = True
                for i in sit_info["wl"]:
                    if not i in server_command:
                        print(Fore.YELLOW + f"    {ulp.warn_terminal}'{i}'")
                        print(Style.RESET_ALL, end="")
                        server_command.append(i)
                if not nomuch:
                    print(Fore.GREEN + f"    -{ulp.info_match}")
                    print(Style.RESET_ALL, end="")
            except: #Exception as e:
                #print(e)
                sit_info = {"it":"Unknow","ver":"Unknow","wl":server_command}
                sit_version = sit_info["it"]
                print(Fore.RED + f"[ {ulp.level_warn} ] {ulp.warn_low}")
            print(f"{ulp.system_sit}{sit_version}")
            if not sit_version == it_version:
                print(Fore.YELLOW + f"[ {ulp.level_note} ] {ulp.warn_unmatch}")
            socket_client.setblocking(0)
        except:
            print(Fore.RED + f"[ {ulp.level_error} ] {ulp.confail}")

#提示等级：
#错误_红色：用户操作造成的中断
#警告_红色：程序异常造成的中断，或警告提示
#注意_黄色：仅警告无中断

def run_commands(head:str,volue:str):
    global rebacked,socket_client,login_name,logined,testmode,sets,randkey,ref_auto,ulp,helps
    rebacked = False
    print(f"-{ulp.info_run} {command} :")
    com_msg = head + ";" + volue
    if testmode:
        print(volue)
        print(len(volue))
        print()
    if sets == fm:
        if not head == "out":
            socket_client.send(f"fm;{head}".encode("UTF-8"))
            rebacked = True
        else:
            sets = Nosets
    else:
        if head == "ser":
            connect_server(volue)
        elif head == "outlog":
            if volue == "c":
                if apple(f"{ulp.warn_outlogc}"):
                    restart()
            else:
                print(f"{ulp.info_try}")
                socket_client.send("outlog".encode("UTF-8"))
                login_name = Nolog
                logined = False
                socket_client.setblocking(1)
        elif head == "printall":
            WTCv = globals()
            #try:
            #    WTCv.pop("till")
            #    WTCv.pop("helps")
            #except:
            #    pass
            print("=====  All Data  ================================================")
            for Ckey in list(WTCv.items()):
                print(f"{Ckey}")
        elif head == "index":
            index()
        elif head == "help":
            print(f"===== Help: {volue}  =====")
            try:
                if volue != "none" and volue != "all":
                    temp_help = helps[volue].split("，")
                elif volue == "all":
                    for Ckey in list(helps.items()):
                        print(f"{Ckey}")
                else:
                    temp_help = helps["help"].split("，")
                if volue != "all":
                    for help_co in temp_help:
                        print(help_co)
            except:
                print(f"{ulp.warn_help1}'{volue}'{ulp.warn_help2}")
        elif head == "uplog":
            uplog = UPDATECHECK.getlog("https://squirrel963.github.io/parrot_web_database/WTC_allinfo/index.md")
            if volue == "none":
                print(f"===== Uplog: {version}  =====")
                temp_uplog = str(uplog[version]).split(" ")
                for i in temp_uplog:
                    print(i)
            else:
                try:
                    print(f"===== Uplog: {volue}  =====")
                    temp_uplog = str(uplog[volue]).split(" ")
                    for i in temp_uplog:
                        print(i)
                except:
                    print(Fore.RED + f"[ {ulp.level_error} ] {ulp.warn_uplog1}'{volue}'{ulp.warn_uplog2}")
        elif head == "info":
            print(f"Python：{sys.version}")
            print("开源许可证：GPL-2.0")
            print("仓库地址：https://github.com/Squirrel963/WangTree")
            print("您可以使用'uplog'来获取该版本的更新日志")
            print("请勿用于非法用途")
        elif head == "testmode":
            if volue == "on":
                testmode = True
            elif volue == "off":
                testmode = False
            else:
                print(f"{ulp.system_test}{testmode}")
        elif head == "ref":
            rebacked = True
            if volue == "auto":
                ref_auto = True
        elif head == "aes":
            aes(volue)
        elif head == "unaes":
            unaes(volue)
        elif head == "set":
            if logined:
                if len(volue.split(".")) == 4:
                    sets = volue.split(" ")[0]
                elif volue == "fm":
                        sets = fm
                        print("===== File_Manager =====")
                        print(f"{ulp.info_fm}")
                        print(f"{ulp.info_fmout}")
                else:
                    print(Fore.RED + f"[ {ulp.level_error} ] {ulp.warn_ipv4}")
            else:
                print(Fore.RED + f"[ {ulp.level_error} ] {ulp.warn_nocon}")
        elif head == "clear":
            os.system("cls")
            if volue == "index":
                index()
        elif head == "rekey":
            if apple(f"{ulp.warn_rekey}"):
                randkey = str(random.randint(1000000000000000,9999999999999999))
                print(f"{ulp.warn_key}{randkey}")
        elif head == "lang":
            try:
                exec(f"ulp = lang.{volue.lower()}")
                exec("helps = ulp.helps")
            except:
                print("Failed to switch language")
        elif head in server_command:
            if logined:
                try:
                    socket_client.send(com_msg.encode("UTF-8"))
                    rebacked = True
                except:
                    print(Fore.RED + f"[ {ulp.level_warn} ] {ulp.warn_fail}")
            else:
                print(Fore.RED + f"[ {ulp.level_error} ] {ulp.warn_nocon}")
        else:
            pass

index()

try:
    import UPDATECHECK
    #if not testmode:
    #    UPDATECHECK.check(version,'https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md')
except:
    print(Fore.YELLOW + f"[ {ulp.level_note} ] UPDATECHECK模块未安装！")
while True:
    if sets == Nosets:
        command = input(f"{login_name} >>")
    else:
        command = input(f"{login_name} > {sets} >")
    if command == "":
        continue
    else:
        command_li = command.split(" ")
        command_volue = ""
        i = 0
        for command_ in command_li:
            if i != 0:
                if i == len(command_li):
                    command_volue += command_
                else:
                    command_volue += (command_ + " ")
            i += 1
        if len(command_li) == 1:
            command_volue = "none"
        else:
            if command_volue[-1] == " ":
                command_volue = command_volue[:-1]
        if testmode:
            print("command:",command)
            print("command_li:",command_li)
            print("command_volue:",command_volue)
            print("len command_volue:",len(command_volue))
        if command_li[0] == "exit":
                sys.exit(0)
        try:
            reback = ""
            run_commands(command_li[0],command_volue)
            rebackunsuss = True
            waitedtime = 0
            if rebacked:
                while rebackunsuss:
                    print(f"{ulp.info_wait}...{10-waitedtime}      ",end='\r')
                    try:
                        reback = socket_client.recv(max_bytes).decode("UTF-8")
                        rebackunsuss = False
                    except:
                        time.sleep(1)
                        waitedtime += 1
                        if waitedtime >= 10:
                            print(f"[ {ulp.level_warn} ] {ulp.info_timeout}                      ")
                            break
            if not rebackunsuss:
                    hunderd = round((sys.getsizeof(reback)/max_bytes)*100)
                    print(f"{ulp.info_back}( {min(sys.getsizeof(reback), max_bytes)} bytes / {max_bytes} bytes [{min(hunderd, 100)}%] ):                     ")
                    if not sets == fm:
                        print(reback)
                        if ref_auto:
                            if hunderd >= 100:
                                run_commands("ref","none")
                            else:
                                ref_auto = False
                    else:
                        if not len(reback.split(",")) == 1:
                            files = reback.split(",")
                            files.pop(-1)
                            for i, f in enumerate(files):
                                print(f, end="   ")
                                if (i + 1) % max_word_size(files) == 0:
                                    print()
                        else:
                            print(reback)
        except:
            print(Fore.RED + f"[ {ulp.level_warn} ] {ulp.warn_error}")
    print(Style.RESET_ALL)
