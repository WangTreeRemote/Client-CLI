class zh_cn:
    system_title = "王果树终端"
    system_ip = "当前设备IP(socket)："
    system_it = "通信版本："
    system_size = "终端窗口大小(字符)："
    system_lang = "操作系统语言: "
    system_aes = "AES随机密钥："
    system_test = "调试模式："
    system_pack = "拓展工具包："
    system_try = "尝试连接服务器中"
    system_suc = "连接成功，连接为"
    system_sit = "目标服务器通信版本："
    level_error = "错误"
    level_warn = "警告"
    level_note = "注意"
    warn_logined = "你已连接到一个服务器，请使用'outlog'断开之前的连接"
    warn_low = "获取目标服务器通信版本失败，请尝试更新版本"
    warn_unmatch = "目标服务器的通信版本与终端不符，可能出现兼容问题"
    warn_confail = "服务器连接失败"
    warn_help1 = "未找到关于命令"
    warn_help2 = "的帮助提示"
    warn_uplog1 = "未找到版本"
    warn_uplog2 = "的更新日志"
    warn_ipv4 = "无效的ipv4地址"
    warn_nocon = "你没有连接到任何服务器"
    warn_rekey = "刷新AES随机密钥可能会导致严重问题，你确定吗？"
    warn_key = "AES随机密钥已更换为："
    warn_fail = "远程命令发送失败，请检查设备可用性"
    warn_error = "发生未知错误"
    warn_outlogc = "命令'outlog'后添加了参数'c'，这会使终端强制与服务器断开连接(无断连请求数据包)！你确定吗？"
    warn_server = "服务器缺失命令"
    warn_terminal = "终端缺失命令"
    info_run = "运行"
    info_fm = "您已进入文件检索模式"
    info_fmout = "使用'out'来退出"
    info_wait = "等待服务器返回信息中"
    info_timeout = "服务器返回信息超时，您可以使用'ref'来手动接收信息"
    info_back = "服务器返回信息"
    info_try = "尝试断开连接中...(添加参数'c'来强制断连) "
    info_it = "兼容性检查："
    info_match = "完全兼容"
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
    "ref":"使socket进行一次数据接收",#，使用'ref auto'来进行大内存信息接收",
    "clear":"清空终端屏幕，使用'clear index'使终端屏幕清空后打印欢迎屏幕",
    "set":"设置子设备，用法：set <ip>，使用'set fm'来进入文件检索模式",
    "rekey":"刷新AES随机密钥",
    "login":"验证并通过目标服务器的安全保护，用法：login <password>",
    "lang":"切换语言，用法：lang <language>，例：lang en_us",
    "":"",
    "":"",
    "":"",
    "":"",
    "":"",
    "":""
    }

class en_us(zh_cn):
    system_title = "WangTree terminal"
    system_ip = "IP(by socket): "
    system_it = "WT network version: "
    system_size = "Terminal window size(by character): "
    system_lang = "OS language: "
    system_aes = "AES random key: "
    system_test = "Test mode: "
    system_pack = "Pro pack: "
    system_try = "Trying to connect server"
    system_suc = "Connection successful, login as"
    system_sit = "Target server communication version: "
    level_error = "Error"
    level_warn = "Warning"
    level_note = "Attention"
    warn_logined = "You have connected to a server, please use 'outlog' to disconnect"
    warn_low = "Failed to get the target server communication version, please try to update"
    warn_unmatch = "The target server's communication version does not match the terminal, There may be a compatibility problem"
    warn_confail = "Fail to connect server"
    warn_help1 = "Didn't found infomation about command "
    warn_help2 = ""
    warn_uplog1 = "Didn't found update log about version "
    warn_uplog2 = ""
    warn_ipv4 = "Invalid ipv4 address"
    warn_nocon = "You are not connected to any server"
    warn_rekey = "Refreshing AES random keys can cause serious problems, are you sure?"
    warn_key = "AES random key was changed to: "
    warn_fail = "Failed to send remote command, please check device availability"
    warn_error = "An unknown error has occurred"
    warn_outlogc = "The command 'log' is followed by the parameter 'c' , which forces the terminal to disconnect from the server (no disconnect request packets) ! Are you sure?"
    warn_server = "Server is missing the command"
    warn_terminal = "Terminal is missing the command"
    info_run = "Run"
    info_fm = "You are in document retrieval mode"
    info_fmout = "Use 'out' to exit"
    info_wait = "Wait for the server to return a message"
    info_timeout = "The server timed out returning information, you can use 'ref' to manually receive the information"
    info_back = "Server return infomation"
    info_try = "Trying to disconnect... (add the parameter' C' to force disconnection) "
    info_it = "Compatibility check: "
    info_match = "Fully compatible"
    helps = {
    "help": "Get help hints about commands，Usage: help <command>，Use 'help all' to get all available commands",
    "cmd": "Run cmd commands on the WT-controlled terminal，Usage: cmd <command>",
    "key": "Simulate keyboard input on the WT-controlled terminal，Usage: key <text>",
    "ser": "Connect to the WT server，Usage: ser <ip> <port>",
    "lock": "Lock the computer controlled by the WT terminal",
    "volue": "Adjust the volume of the target computer on the WT-controlled terminal",
    "uplog": "Get update logs from the PWD database，Usage: uplog <version>",
    "testmode": "Toggle debug mode，Usage: testmode <on/off>",
    #"aes": "Toggle AES encrypted communication，Usage: aes <on/off>",
    "printall": "Print all memory data of the WT terminal",
    "info": "None",
    "index": "Print the welcome screen",
    "outlog": "Disconnect from the connected WT server，Use 'outlog c' to force disconnection",
    "exit": "Exit the WT terminal",
    "ref": "Perform a data reception via socket",  # Usage: ref <data>，Use 'ref auto' for large memory data reception
    "clear": "Clear the terminal screen，Use 'clear index' to print the welcome screen after clearing",
    "set": "Set the sub-device，Usage: set <ip>，Use 'set fm' to enter file search mode",
    "rekey": "Refresh the AES random key",
    "login": "Authenticate and bypass the security protection of the target server，Usage: login <password>",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
    }

class ru_ru(zh_cn):
    system_title = "Терминал WangTree"
    system_ip = "IP (через сокет): "
    system_it = "Версия сети WT: "
    system_size = "Размер окна терминала (в символах): "
    system_lang = "Язык ОС: "
    system_aes = "Случайный ключ AES: "
    system_test = "Режим тестирования: "
    system_pack = "Профессиональный пакет: "
    system_try = "Попытка подключения к серверу"
    system_suc = "Успешное подключение, вход выполнен как"
    system_sit = "Версия связи целевого сервера: "
    level_error = "Ошибка"
    level_warn = "Предупреждение"
    level_note = "Внимание"
    warn_logined = "Вы уже подключены к серверу. Используйте 'outlog', чтобы отключиться"
    warn_low = "Не удалось получить версию связи целевого сервера. Попробуйте обновиться"
    warn_unmatch = "Версия связи целевого сервера не соответствует терминалу. Возможны проблемы с совместимостью"
    warn_confail = "Не удалось подключиться к серверу"
    warn_help1 = "Не найдена информация о команде "
    warn_help2 = ""
    warn_uplog1 = "Не найдены сведения об обновлении для версии "
    warn_uplog2 = ""
    warn_ipv4 = "Недопустимый IPv4-адрес"
    warn_nocon = "Вы не подключены ни к одному серверу"
    warn_rekey = "Обновление случайного ключа AES может вызвать серьезные проблемы. Вы уверены?"
    warn_key = "Случайный ключ AES изменен на: "
    warn_fail = "Не удалось отправить удаленную команду. Проверьте доступность устройства"
    warn_error = "Произошла неизвестная ошибка"
    warn_outlogc = "Команда 'log' содержит параметр 'c', который принудительно отключает терминал от сервера (без пакетов запроса отключения)! Вы уверены?"
    warn_server = "Сервер не отвечает на команду"
    warn_terminal = "Терминал не отвечает на команду"
    info_run = "Запуск"
    info_fm = "Вы находитесь в режиме поиска документов"
    info_fmout = "Используйте 'out', чтобы выйти"
    info_wait = "Ожидание ответа сервера"
    info_timeout = "Сервер не ответил вовремя. Используйте 'ref', чтобы вручную получить информацию"
    info_back = "Сервер вернул информацию"
    info_try = "Попытка отключения... (добавьте параметр 'C', чтобы принудительно отключиться)"
    info_it = "Проверка совместимости:"
    info_match = "Полностью совместимо"
    helps = {
        "help": "Получить подсказки о командах，Использование: help <команда>，Используйте 'help all', чтобы получить все доступные команды",
        "cmd": "Выполнить команды cmd в терминале WT，Использование: cmd <команда>",
        "key": "Эмуляция ввода с клавиатуры в терминале WT，Использование: key <текст>",
        "ser": "Подключение к серверу WT，Использование: ser <IP> <порт>",
        "lock": "Блокировка компьютера, контролируемого терминалом WT",
        "volue": "Настройка громкости целевого компьютера в терминале WT",
        "uplog": "Получение журнала обновлений из базы данных PWD，Использование: uplog <версия>",
        "testmode": "Переключение режима отладки，Использование: testmode <вкл/выкл>",
        #"aes": "Переключение шифрования AES，Использование: aes <вкл/выкл>",
        "printall": "Вывод всех данных памяти терминала WT",
        "info": "Нет",
        "index": "Вывод экрана приветствия",
        "outlog": "Отключение от подключенного сервера WT，Используйте 'outlog c', чтобы принудительно отключиться",
        "exit": "Выход из терминала WT",
        "ref": "Получение данных через сокет",  # Использование: ref <данные>，Используйте 'ref auto' для получения данных с большой памятью
        "clear": "Очистка экрана терминала，Используйте 'clear index', чтобы вывести экран приветствия после очистки",
        "set": "Настройка подустройства，Использование: set <IP>，Используйте 'set fm', чтобы перейти в режим поиска файлов",
        "rekey": "Обновление случайного ключа AES",
        "login": "Аутентификация и обход защиты целевого сервера，Использование: login <пароль>",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": ""
    }

class zh_hk(zh_cn):
    system_title = "王樹果終端機"
    system_ip = "當前設備IP（socket）："
    system_it = "通訊版本："
    system_size = "終端機視窗大小（字符）："
    system_lang = "作業系統語言："
    system_aes = "AES隨機密鑰："
    system_test = "調試模式："
    system_pack = "擴展工具包："
    system_try = "嘗試連接伺服器中"
    system_suc = "連接成功，連接為"
    system_sit = "目標伺服器通訊版本："
    level_error = "錯誤"
    level_warn = "警告"
    level_note = "注意"
    warn_logined = "您已連接到一台伺服器，請使用 'outlog' 斷開之前的連接"
    warn_low = "獲取目標伺服器通訊版本失敗，請嘗試更新版本"
    warn_unmatch = "目標伺服器的通訊版本與終端機不符，可能會出現兼容問題"
    warn_confail = "伺服器連接失敗"
    warn_help1 = "未找到關於命令"
    warn_help2 = "的幫助提示"
    warn_uplog1 = "未找到版本"
    warn_uplog2 = "的更新日誌"
    warn_ipv4 = "無效的 IPv4 地址"
    warn_nocon = "您沒有連接到任何伺服器"
    warn_rekey = "刷新 AES 隨機密鑰可能會導致嚴重問題，您確定嗎？"
    warn_key = "AES 隨機密鑰已更換為："
    warn_fail = "遠端命令發送失敗，請檢查設備可用性"
    warn_error = "發生未知錯誤"
    warn_outlogc = "命令 'outlog' 後添加了參數 'c'，這會使終端機強制與伺服器斷開連接（無斷連請求數據包）！您確定嗎？"
    warn_server = "伺服器缺失命令"
    warn_terminal = "終端機缺失命令"
    info_run = "運行"
    info_fm = "您已進入文件檢索模式"
    info_fmout = "使用 'out' 來退出"
    info_wait = "等待伺服器返回信息中"
    info_timeout = "伺服器返回信息超時，您可以使用 'ref' 來手動接收信息"
    info_back = "伺服器返回信息"
    info_try = "嘗試斷開連接中...(添加參數 'c' 來強制斷連)"
    info_it = "兼容性檢查："
    info_match = "完全兼容"
    helps = {
        "help": "獲取關於命令的幫助提示，用法：help <command>，使用 'help all' 來獲取所有可用命令",
        "cmd": "使 WT 受控終端機運行 cmd 命令，用法：cmd <command>",
        "key": "使 WT 受控終端機模擬鍵盤輸入字符，用法：key <text>",
        "ser": "連接 WT 伺服器，用法：ser <ip> <port>",
        "lock": "使 WT 受控終端機鎖定所在計算機",
        "volue": "使 WT 受控終端機調整目標計算機音量",
        "uplog": "獲取來自 PWD 資料庫的更新日誌，用法：uplog <version>",
        "testmode": "開關調試模式，用法：testmode <on/off>",
        #"aes": "開關 AES 加密通訊，用法：aes <on/off>",
        "printall": "打印 WT 終端機的全部記憶體數據",
        "info": "無",
        "index": "打印歡迎屏幕",
        "outlog": "與所連接的 WT 伺服器斷開連接，使用 'outlog c' 來強制斷連",
        "exit": "退出 WT 終端機",
        "ref": "使 socket 進行一次數據接收",  # 使用 'ref auto' 來進行大記憶體信息接收
        "clear": "清空終端機屏幕，使用 'clear index' 使終端機屏幕清空後打印歡迎屏幕",
        "set": "設置子設備，用法：set <ip>，使用 'set fm' 來進入文件檢索模式",
        "rekey": "刷新 AES 隨機密鑰",
        "login": "驗證並通過目標伺服器的安全保護，用法：login <password>",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": "",
        "": ""

    }
