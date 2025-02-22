import os
import socket
import threading
import ctypes
import win32api
import win32con
import json
import keyboard
 
version = "1.2.19"
it_version = 10004

white_list = ["login", "lock", "cmd", "key", "volue"]

ip = socket.gethostbyname(socket.gethostname())

def set_volume(volume):
    win32api.SendMessage(
        win32con.HWND_BROADCAST, win32con.WM_APPCOMMAND, 0x30292, volume * 0xFFFF // 100)

def create_server_socket(host, port):
    socket_server = socket.socket()
    socket_server.bind((host, port))
    socket_server.listen(5)
    print(f"服务端已启动  地址{host}，端口{port}")
    while True:
        conn, address = socket_server.accept()
        print(f"服务端接受到{address}的连接请求")
        client_handler = threading.Thread(target=handle_client, args=(conn, address))
        client_handler.start()
 
def handle_client(conn, address):
    logined = False
    trys = 0
    while True:
        data_from_client: str = conn.recv(4096).decode("UTF-8")
        print(f"{address}发送数据：{data_from_client}")
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
                    if trys < 5:
                        if data[1] == "1145":
                            logined = True
                            msg = "登录成功！"
                        else:
                            trys += 1
                            msg = f"错误的密钥，您本次连接还有{5-trys}次尝试机会"
                    else:
                        msg = "本次连接的安全验证已禁用，请重新连接"
                else:
                    msg = "您已登录"
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
    print("正在启动服务端...", end='\r')
    server_host = ip
    server_port = 200
    create_server_socket(server_host, server_port)
