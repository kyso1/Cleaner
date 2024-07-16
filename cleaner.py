import os
import sys
import shutil
import ctypes
import subprocess
import platform
from time import sleep
import psutil
from colorama import init, Fore, Back, Style

init(autoreset=True)
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def print_message(message, success=True):
    border_color = Fore.GREEN if success else Fore.RED
    message_color = Fore.BLACK if success else Fore.RED
    border_line = border_color + "╭" + "─" * 58 + "╮"
    content_line = border_color + "│" + message_color + f"{message.center(56)}" + border_color + "│"
    print(border_line)
    print(content_line)
    print(border_line.replace("╭", "╰").replace("╮", "╯"))

def clean(folder):
    if not os.path.exists(folder):
        print_message(f"Pasta {folder} não encontrada.", success=False)
        return

    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print_message(f"Removido com sucesso: {file_path}")
            except Exception as e:
                print_message(f"Erro ao excluir {file_path}: {e}", success=False)
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                shutil.rmtree(dir_path)
                print_message(f"Removido com sucesso: {dir_path}")
            except Exception as e:
                print_message(f"Erro ao excluir {dir_path}: {e}", success=False)

    try:
        shutil.rmtree(folder)
        print_message(f"Removido com sucesso: {folder}")
    except Exception as e:
        print_message(f"Erro ao excluir {folder}: {e}", success=False)

def clean_system_cache():
    temp_folder = os.getenv('TEMP')
    clean(temp_folder)

def resetIp():
    os.system("ipconfig /flushdns")

def clean_browser(browser, cookie):
    base_path = os.getenv('LOCALAPPDATA')
    browser_paths = {
        'Opera': os.path.join(base_path, 'Opera', 'User Data', 'Default'),
        'Opera GX': os.path.join(base_path, 'Opera Software', 'Opera GX Stable'),
        'Brave': os.path.join(base_path, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default'),
        'Firefox': os.path.join(base_path, 'Mozilla', 'Firefox', 'Profiles'),
        'Chrome': os.path.join(base_path, 'Google', 'Chrome', 'User Data', 'Default'),
        'Edge': os.path.join(base_path, 'Microsoft', 'Edge', 'User Data', 'Default')
    }

    if browser in browser_paths:
        path = browser_paths[browser]
        try:
            if cookie:
                shutil.rmtree(os.path.join(path, 'Cookies'))
            shutil.rmtree(os.path.join(path, 'Cache'))
            shutil.rmtree(os.path.join(path, 'History'))
            print_message(f"Dados do navegador {browser} limpos com sucesso.")
        except Exception as e:
            print_message(f"Erro ao limpar dados do navegador {browser}: {e}", success=False)
    else:
        print_message(f"Navegador {browser} não encontrado.", success=False)

def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def menu():
    print(Fore.CYAN + "╭──────────────────────────────────────────╮")
    print(Fore.CYAN + "│           KysoCleaner v1.0   :)          │")
    print(Fore.CYAN + "╰──────────────────────────────────────────╯")
    print(Fore.YELLOW + "╭──────────────────────────────────────────╮")
    print(Fore.YELLOW + "│Escolha uma opção:                        │")
    print(Fore.YELLOW + "╰──────────────────────────────────────────╯")
    print(Fore.MAGENTA + "╭──────────────────────────────────────────╮")
    print(Fore.MAGENTA + "│1 - Limpar somente a pasta '%temp%'       │")
    print(Fore.MAGENTA + "│2 - Limpar somente a pasta 'temp'         │")
    print(Fore.MAGENTA + "│3 - Limpar somente a pasta 'recent'       │")
    print(Fore.MAGENTA + "│4 - Limpar todas as pastas                │")
    print(Fore.MAGENTA + "│5 - Limpar cache do sistema e resetar IP  │")
    print(Fore.MAGENTA + "│6 - Limpar dados de navegadores           │")
    print(Fore.MAGENTA + "│7 - Limpar tudo (sem navegador)           │")
    print(Fore.MAGENTA + "│8 - Limpar tudo (com navegador)           │")
    print(Fore.MAGENTA + "│9 - Resetar IP                            │")
    print(Fore.MAGENTA + "│10 - Sair                                 │")
    print(Fore.MAGENTA + "╰──────────────────────────────────────────╯")

def browserMenu():
    print(Fore.CYAN + "╭───────────────────────────╮")
    print(Fore.CYAN + "│      BrowserCleaner       │")
    print(Fore.CYAN + "╰───────────────────────────╯")
    print(Fore.YELLOW + "╭───────────────────────────╮")
    print(Fore.YELLOW + "│ Escolha seu navegador:    │")
    print(Fore.YELLOW + "╰───────────────────────────╯")
    print(Fore.MAGENTA + "╭───────────────────────────╮")
    print(Fore.RED + "│1 - Opera                  │")
    print(Fore.RED + "│2 - Opera GX               │")
    print(Fore.LIGHTYELLOW_EX + "│3 - Brave                  │")
    print(Fore.LIGHTBLUE_EX + "│4 - Firefox                │")
    print(Fore.BLUE + "│5 - Chrome                 │")
    print(Fore.LIGHTGREEN_EX + "│6 - Edge                   │")
    print(Fore.MAGENTA + "│7 - Voltar                 │")
    print(Fore.MAGENTA + "╰───────────────────────────╯")
    
def cookiePrompt():
    print(Fore.CYAN + "╭───────────────────────────╮")
    print(Fore.CYAN + "│      CookiesCleaner       │")
    print(Fore.CYAN + "╰───────────────────────────╯")
    print(Fore.YELLOW + "╭───────────────────────────╮")
    print(Fore.YELLOW + "│ Escolha sua opção:        │")
    print(Fore.YELLOW + "╰───────────────────────────╯")
    print(Fore.MAGENTA + "╭───────────────────────────╮")
    print(Fore.MAGENTA + "│1- Sim                     │")
    print(Fore.MAGENTA + "│2- Não                     │")
    print(Fore.MAGENTA + "│3- Cancelar                │")
    print(Fore.MAGENTA + "╰───────────────────────────╯")
    
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    while True:
        menu()
        op = input(Fore.LIGHTBLACK_EX + "Digite o número da operação: ")
        if op == '1':
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
        elif op == '2':
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
        elif op == '3':
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
        elif op == '4':
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
        elif op == '5':
            clean_system_cache()
            resetIp()
            print_message("Cache do sistema limpo e IP resetado.")
            sleep(5)
            clearscreen()
        elif op == '6':
            clearscreen()
            while True:
                browserMenu()
                browser = input("Escolha a opção do seu navegador: ")
                browser_options = {
                    '1': 'Opera',
                    '2': 'Opera GX',
                    '3': 'Brave',
                    '4': 'Firefox',
                    '5': 'Chrome',
                    '6': 'Edge',
                    '7': 'Voltar'
                }
                if browser in browser_options:
                    nav = browser_options[browser]
                    if nav == 'Voltar':
                        clearscreen()
                        break

                    while True:
                        clearscreen()
                        cookiePrompt()
                        cookie = input("Opção: ")
                        if cookie == '1':
                            clean_browser(nav, True)
                            break
                        elif cookie == '2':
                            clean_browser(nav, False)
                            break
                        elif cookie == '3':
                            clearscreen()
                            break
                        else:
                            print_message(Fore.RED + "Opção inválida. Digite somente 1 ou 2.", success=False)
                
        elif op == '7':
            clean_system_cache()
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
            print_message(Fore.GREEN + "Tudo foi limpo com sucesso.")
            sleep(5)
            clearscreen()
        elif op == '8':
            clearscreen()
            while True:
                browserMenu()
                browser = input("Escolha a opção do seu navegador: ")
                browser_options = {
                    '1': 'Opera',
                    '2': 'Opera GX',
                    '3': 'Brave',
                    '4': 'Firefox',
                    '5': 'Chrome',
                    '6': 'Edge',
                    '7': 'Voltar'
                }
                if browser in browser_options:
                    nav = browser_options[browser]
                    if nav == 'Voltar':
                        clearscreen()
                        break
                    while True:
                        clearscreen()
                        cookiePrompt()
                        cookie = input("Opção: ")
                        if cookie == '1':
                            clean_browser(nav, True)
                            break
                        elif cookie == '2':
                            clean_browser(nav, False)
                            break
                        elif cookie == '3':
                            clearscreen()
                            break
                        else:
                            print_message("Opção inválida. Digite somente 1 ou 2.", success=False)
                        
            clean_system_cache()
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
            print_message("Tudo foi limpo com sucesso.")
            sleep(5)
            clearscreen()
        elif op == '9':
            resetIp()
            clearscreen()
        elif op == '10':
            print_message("Saindo...")
            sleep(3)
            break
        else:
            print_message("Opção inválida. Por favor, escolha uma opção de 1 a 10.", success=False)
            sleep(3)
            clearscreen()

    run_as_admin()

if __name__ == "__main__":
    main()
