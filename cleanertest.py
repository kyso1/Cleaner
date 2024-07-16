import os
import sys
import ctypes
import subprocess
import platform
from time import sleep

os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def clean(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print("╭──────────────────────────────────────────────────────╮")
                print("│Removido com sucesso: " + file_path + "               │")
                print("╰──────────────────────────────────────────────────────╯")
            except Exception as e:
                print("╭──────────────────────────────────────────────────────╮")
                print(f"Erro ao excluir {file_path}: {e}")
                print("╰──────────────────────────────────────────────────────╯")
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
                print("╭──────────────────────────────────────────────────────╮")
                print("│Removido com sucesso: " + dir_path + "               │")
                print("╰──────────────────────────────────────────────────────╯")
            except Exception as e:
                print("╭──────────────────────────────────────────────────────╮")
                print(f"Erro ao excluir {dir_path}: {e}")
                print("╰──────────────────────────────────────────────────────╯")

    try:
        os.rmdir(folder)
        print("╭──────────────────────────────────────────────────────╮")
        print("│Removido com sucesso: " + folder + "               │")
        print("╰──────────────────────────────────────────────────────╯")
    except Exception as e:
        print("╭──────────────────────────────────────────────────────╮")
        print(f"Erro ao excluir {folder}: {e}")
        print("╰──────────────────────────────────────────────────────╯")

def clean_system_cache():
    os.system("del /s /q /f %temp%\\*")  

def resetIp():
    os.system("ipconfig /flushdns")      

def clean_browser(browser, cookie):
    if cookie:
        try:
            subprocess.run(['cmd', '/c', f'rmdir /q /s %LOCALAPPDATA%\\{browser}\\User Data\\Default\\Cache'], check=True)
            subprocess.run(['cmd', '/c', f'rmdir /q /s %LOCALAPPDATA%\\{browser}\\User Data\\Default\\Cookies'], check=True)
            subprocess.run(['cmd', '/c', f'rmdir /q /s %LOCALAPPDATA%\\{browser}\\User Data\\Default\\History'], check=True)
        except subprocess.CalledProcessError as e:
            print("╭──────────────────────────────────────────────────────╮")
            print(f"Erro ao limpar dados do navegador {browser}: {e}")
            print("╰──────────────────────────────────────────────────────╯")
    else:
        try:
            subprocess.run(['cmd', '/c', f'rmdir /q /s %LOCALAPPDATA%\\{browser}\\User Data\\Default\\Cache'], check=True)
            subprocess.run(['cmd', '/c', f'rmdir /q /s %LOCALAPPDATA%\\{browser}\\User Data\\Default\\History'], check=True)
        except subprocess.CalledProcessError as e:
            print("╭──────────────────────────────────────────────────────╮")
            print(f"Erro ao limpar dados do navegador {browser}: {e}")
            print("╰──────────────────────────────────────────────────────╯")
    
def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def menu():
    print("╭──────────────────────────────────────────╮")
    print("│           KysoCleaner v1.0   :)          │")
    print("╰──────────────────────────────────────────╯")
    print("╭──────────────────────────────────────────╮")
    print("│Escolha uma opção:                        │")
    print("╰──────────────────────────────────────────╯") 
    print("╭──────────────────────────────────────────╮")
    print("│1 - Limpar somente a pasta '%temp%'       │")
    print("│2 - Limpar somente a pasta 'temp'         │")
    print("│3 - Limpar somente a pasta 'recent'       │")
    print("│4 - Limpar todas as pastas                │")
    print("│5 - Limpar cache do sistema e resetar IP  │")
    print("│6 - Limpar dados de navegadores           │")
    print("│7 - Limpar tudo (sem navegador)           │")
    print("│8 - Limpar tudo (com navegador)           │")
    print("│9 - Resetar IP                            │")
    print("│10 - Sair                                 │")
    print("╰──────────────────────────────────────────╯")

def browserMenu():
    print("╭───────────────────────────╮")
    print("│      BrowserCleaner       │")
    print("╰───────────────────────────╯")
    print("╭───────────────────────────╮")
    print("│ Escolha seu navegador:    │")
    print("╰───────────────────────────╯")
    print("╭───────────────────────────╮")
    print("│1 - Opera                  │")
    print("│2 - Opera GX               │")
    print("│3 - Brave                  │")
    print("│4 - Firefox                │")
    print("│5 - Chrome                 │")
    print("│6 - Edge                   │")
    print("│7 - Voltar                 │")
    print("╰───────────────────────────╯")
    
def cookiePrompt():
    print("╭───────────────────────────╮")
    print("│      CookiesCleaner       │")
    print("╰───────────────────────────╯")
    print("╭───────────────────────────╮")
    print("│ Escolha sua opção:        │")
    print("╰───────────────────────────╯")
    print("╭───────────────────────────╮")
    print("│1- Sim                     │")
    print("│2- Não                     │")
    print("│3- Cancelar                │")
    print("╰───────────────────────────╯")
    
def clearscreen():
    os.system('cls')
    
def main():
    while True:
        menu()
        op = input("Digite o número da operação: ")
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
            print("Cache do sistema limpo e IP resetado.")
            sleep(5)
            clearscreen()
        elif op == '6':
            clearscreen()
            while True:
                browserMenu()
                browser = input("Escolha a opção do seu navegador: ")
                if browser == '1':
                    nav = "Opera"
                elif browser == '2':
                    nav = "Opera Software"
                elif browser == '3':
                    nav = "BraveSoftware\\Brave-Browser"
                elif browser == '4':
                    nav = "Mozilla\\Firefox"
                elif browser == '5':
                    nav = "Google\\Chrome"
                elif browser == '6':
                    nav = "Microsoft\\Edge"
                elif browser == '7':
                    clearscreen()
                    break
                else:
                    print("Navegador inválido. Por favor, escolha um navegador de 1 a 6.")
                    continue

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
                        print("Opção inválida. Digite somente 1 ou 2.")
                
        elif op == '7':
            clean_system_cache()
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
            print("Tudo foi limpo com sucesso.")
            sleep(5)
            clearscreen()
        elif op == '8':
            clearscreen()
            while True:
                browserMenu()
                browser = input("Escolha a opção do seu navegador: ")
                if browser == '1':
                    nav = "Opera"
                elif browser == '2':
                    nav = "Opera Software"
                elif browser == '3':
                    nav = "BraveSoftware\\Brave-Browser"
                elif browser == '4':
                    nav = "Mozilla\\Firefox"
                elif browser == '5':
                    nav = "Google\\Chrome"
                elif browser == '6':
                    nav = "Microsoft\\Edge"
                elif browser == '7':
                    clearscreen()
                    break
                else:
                    print("Navegador inválido. Por favor, escolha um navegador de 1 a 6.")
                    continue
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
                        print("Opção inválida. Digite somente 1 ou 2.")
                        
            clean_system_cache()
            clean(os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp'))
            clean(os.path.join(os.path.expanduser('~'), 'temp'))
            clean(os.path.join(os.path.expanduser('~'), 'Recent'))
            print("Tudo foi limpo com sucesso.")
            sleep(5)
            clearscreen()
        elif op == '9':
            resetIp()
            clearscreen()
        elif op == '10':
            print("Saindo...")
            sleep(3)
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 8.")
            sleep(3)
            clearscreen()

    run_as_admin()

if __name__ == "__main__":
    main()
