import os
import socket
import threading
import ctypes
import win32api
import win32con
import json
import keyboard
import time
import tomli
 
version = "1.2.20"
it_version = 10004

try:
    with open("config.toml", mode="rb") as fp:
        config = tomli.load(fp)  
    #print(config)
except:
    print("[WARN]：Can't load config file ! Will use normal config !")
    config = {'server': {'port': 200}, 
              'command': {'white_list': ['login', 'lock', 'cmd', 'key', 'volue']}, 
              'authentication': {'passkey': 'H114514', 'max_try': 5}}

white_list = config['command']['white_list']
passkey = config['authentication']['passkey']
max_try = config['authentication']['max_try']
inf_try = False
if max_try == 0:
    max_try = 10000
    inf_try = True


ip = socket.gethostbyname(socket.gethostname())

def defix(text : str):
    cstr = f"[{text.upper()}][{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}] "
    return cstr

def set_volume(volume):
    win32api.SendMessage(
        win32con.HWND_BROADCAST, win32con.WM_APPCOMMAND, 0x30292, volume * 0xFFFF // 100)

def create_server_socket(host, port):
    socket_server = socket.socket()
    socket_server.bind((host, port))
    socket_server.listen(5)
    print(f"{defix('server')}Successful start!  address : {host} port : {port}")
    while True:
        conn, address = socket_server.accept()
        print(f"{defix('network')}{address} connected!")
        client_handler = threading.Thread(target=handle_client, args=(conn, address))
        client_handler.start()
 
def handle_client(conn, address):
    logined = False
    trys = 0
    while True:
        data_from_client: str = conn.recv(4096).decode("UTF-8")
        print(f"{defix('info')}{address}：{data_from_client}")
        data = data_from_client.split(";")
        try:
            if data_from_client == 'outlog':
                break
            elif data_from_client == "dataget":
                info = {
                    "it":it_version,
                    "ver":version,
                    "wl":white_list
                    }
                msg = json.dumps(info)
            elif data[0] == "login":
                if not logined:
                    if trys < max_try:
                        if data[1] == passkey:
                            logined = True
                            msg = "登录成功！"
                        elif data[1] == "none":
                            msg = '''您没有输入任何passkey！
用法：login <password>'''
                        else:
                            if not inf_try:
                                trys += 1
                            msg = f"错误的密钥，您本次连接还有{max_try-trys}次尝试机会"
                    else:
                        msg = "本次连接的安全验证已禁用，请重新连接"
                else:
                    msg = "您已使用passkey登录"
            else:
                if logined:
                    if data[0] == "cmd":
                        tback = os.popen(data[1])
                        msg = tback.read()
                    elif data[0] == "lock":
                        ctypes.windll.user32.LockWorkStation()
                        msg = "已锁定屏幕"
                    elif data[0] == "volue":
                        set_volume(int(data[1]))
                        msg = f"已调整音量为{data[1]}"
                    elif data[0] == "key":
                        keyboard.write(data[1])
                        msg = f"已控制键盘输入{data[1]}"
                    elif data[0] == "fm":
                        files = os.listdir(f'{data[1]}')
                        #print(files)
                        te = ""
                        for f in files:
                            te += f"{f},"
                        msg = te
                    else:
                        msg = "服务器无法处理的命令"
                else:
                    msg = "未授权的访问，请使用“login <password>”进行安全验证"
        except:
            msg = "运行命令时出现错误"
        conn.send(msg.encode("UTF-8"))
    conn.close()
 
 
if __name__ == '__main__':
    print(f"WangTreeServer v{version}")
    print(f"address: {ip}")
    print("starting...", end='\r')
    server_host = ip
    server_port = config['server']['port']
    create_server_socket(server_host, server_port)