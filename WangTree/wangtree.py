version = "1.0.9"
it_version = 10003
testmode = False
print("正在载入需要库...",end='\r')
import socket
import sys
import time
import os
import random
import shutil
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

helps = {
    "help":"获取关于命令的帮助提示，用法：help <command>，使用'help all'来获取所有可用命令",
    "cmd":"使WT受控终端运行cmd命令，用法：cmd <command>",
    "key":"使WT受控终端模拟键盘输入字符，用法：key <text>",
    "ser":"连接WT服务器，用法：ser <ip> <port>",
    "lock":"使WT受控终端锁定所在计算机",
    "volue":"使WT受控终端调整目标计算机音量",
    "uplog":"获取来自PWD数据库的更新日志，用法：uplog <version>",
    "testmode":"开关调试模式，用法：testmode <on/off>",
    #"aes":"开关aes加密通信，用法：testmode <on/off>",
    "printall":"打印WT终端的全部内存数据",
    "info":"无",
    "index":"打印欢迎屏幕",
    "outlog":"与所连接的WT服务器断开连接，使用'outlog c'来强制断连",
    "exit":"退出WT终端",
    "ref":"使socket进行一次数据接收，使用'ref auto'来进行大内存信息接收",
    "clear":"清空终端屏幕，使用'clear index'使终端屏幕清空后打印欢迎屏幕",
    "set":"设置子设备，用法：set <ip>，使用'set fm'来进入文件检索模式",
    "rekey":"刷新AES随机密钥",
    "login":"验证并通过目标服务器的安全保护，用法：login <password>",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":""
}

till = [
"__        __                      _____",
"\ \      / /  __ _  _ __    __ _ |_   _| _ __   ___   ___ ",
" \ \ /\ / /  / _` || '_ \  / _` |  | |  | '__| / _ \ / _ |",
"  \ V  V /  | (_| || | | || (_| |  | |  | |   |  __/|  __/",
"   \_/\_/    \__,_||_| |_| \__, |  |_|  |_|    \___| \___|",
"                           |___/"
]

def apple(text):
    appl = input(Fore.RED + f"[ 警告 ] {text} [y/n] ")
    print(Style.RESET_ALL, end="")
    if appl == "y":
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
    print(f"王果树终端 v{version}")
    print(f"当前设备IP(socket)：{ip}")
    print(f"通信版本：{it_version}")
    print(f"终端窗口大小(字符)：{get_window_size()}")
    print(f"AES随机密钥：{randkey}")
    print(f"调试模式：{testmode}")
    print(f"拓展工具包：{Isinstall_toolback}")
    print("-----------------------")

def connect_server(server_ip):
    global login_name,logined
    server = server_ip.split(" ")
    if logined:
        print(Fore.YELLOW + "[ 注意 ] 你已连接到一个服务器，请使用'outlog'断开之前的连接")
    else:
        try:
            print("解析命令中...")
            s_ip = server[0]
            #print(s_ip)
            if len(server) >= 2:
                s_port = int(server[1])
            else:
                s_port = 200
            #print(s_port)
            print("尝试连接服务器中...")
            socket_client.connect((s_ip, s_port))
            login_name = s_ip
            logined = True
            print(f"连接成功，连接为{login_name}")
            socket_client.send("dataget".encode("UTF-8"))
            try:
                sit_version = int(socket_client.recv(2048).decode("UTF-8"))
            except:
                sit_version = "Unknow"
                print(Fore.RED + "[ 警告 ] 获取目标服务器通信版本失败，请尝试更新版本")
            print(f"目标服务器通信版本：{sit_version}")
            if not sit_version == it_version:
                print(Fore.YELLOW + "[ 注意 ] 目标服务器的通信版本与终端不符，可能出现兼容问题")
            socket_client.setblocking(0)
        except:
            print(Fore.RED + "[ 错误 ] 服务器连接失败")

#提示等级：
#错误_红色：用户操作造成的中断
#警告_红色：程序异常造成的中断，或警告提示
#注意_黄色：仅警告无中断

def run_commands(head:str,volue:str):
    global rebacked,socket_client,login_name,logined,testmode,sets,randkey,ref_auto
    rebacked = False
    print(f"-运行{command} :")
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
                if apple("命令'outlog'后添加了参数'c'，这会使终端强制与服务器断开连接(无断连请求数据包)！你确定吗？"):
                    restart()
            else:
                print("尝试断开连接中...(添加参数'c'来强制断连) ")
                socket_client.send("outlog".encode("UTF-8"))
                login_name = Nolog
                logined = False
                socket_client.setblocking(1)
        elif head == "printall":
            WTCv = globals()
            try:
                WTCv.pop("till")
                WTCv.pop("helps")
            except:
                pass
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
                print(f"未找到关于命令'{volue}'的帮助提示")
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
                    print(Fore.RED + f"[ 错误 ] 未找到版本'{volue}'的更新日志")
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
                print(f"调试模式：{testmode}")
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
                        print("您已进入文件检索模式")
                        print("使用'out'来退出")
                else:
                    print(Fore.RED + "[ 错误 ] 无效的ipv4地址")
            else:
                print(Fore.RED + "[ 错误 ] 你没有连接到任何服务器")
        elif head == "clear":
            os.system("cls")
            if volue == "index":
                index()
        elif head == "rekey":
            if apple("刷新AES随机密钥可能会导致严重问题，你确定吗？"):
                randkey = str(random.randint(1000000000000000,9999999999999999))
                print(f"AES随机密钥已更换为：{randkey}")
        elif head in server_command:
            if logined:
                try:
                    socket_client.send(com_msg.encode("UTF-8"))
                    rebacked = True
                except:
                    print(Fore.RED + "[ 警告 ] 远程命令发送失败，请检查设备可用性")
            else:
                print(Fore.RED + "[ 错误 ] 你没有连接到任何服务器")
        else:
            pass

index()

try:
    import UPDATECHECK
    if not testmode:
        UPDATECHECK.check(version,'https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md')
except:
    print(Fore.YELLOW + "[ 注意 ] UPDATECHECK模块未安装！")
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
                    print(f"等待服务器返回信息中...{10-waitedtime}      ",end='\r')
                    try:
                        reback = socket_client.recv(max_bytes).decode("UTF-8")
                        rebackunsuss = False
                    except:
                        time.sleep(1)
                        waitedtime += 1
                        if waitedtime >= 10:
                            print("[ 警告 ] 服务器返回信息超时，您可以使用'ref'来手动接收信息                      ")
                            break
            if not rebackunsuss:
                    hunderd = round((sys.getsizeof(reback)/max_bytes)*100)
                    print(f"服务器返回信息( {min(sys.getsizeof(reback), max_bytes)} bytes / {max_bytes} bytes [{min(hunderd, 100)}%] ):                     ")
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
            print(Fore.RED + "[ 警告 ] 发生未知错误")
    print(Style.RESET_ALL)
