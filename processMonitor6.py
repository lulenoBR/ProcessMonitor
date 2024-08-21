import psutil, time,subprocess, configparser, logging, pystray, threading, os
import tkinter as tk
from tkinter import messagebox
from PIL import Image

def setup_logger():
    logger = logging.getLogger("process_monitor")
    logger.setLevel(logging.DEBUG)
    
    handler = logging.FileHandler("process_monitor.log")
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() == process_name.lower():
            return True
    return False

def restart_process(executable_path, process_name):
    try:
        subprocess.Popen(executable_path)
        logger.info("Process '{}' restarted.".format(process_name))
    except Exception as e:
        logger.error("Failed to restart process '{}': {}".format(process_name, e))

def create_default_config(config_file):
    config = configparser.ConfigParser()
    config['ProcessConfig'] = {
        'process_name': 'app.exe',
        'executable_path': r'\\Folder\Folder\app.exe',
        # 'executable_path': r'\\Folder\Folder\app.exe /B Parameters',
        'sleep_time_seconds': '15'
    }

    with open(config_file, 'w') as configfile:
        config.write(configfile)

def read_config(config_file):
    if not os.path.exists(config_file):
        create_default_config(config_file)

    config = configparser.ConfigParser()
    config.read(config_file)
    process_name = config.get("ProcessConfig", "process_name")
    executable_path = config.get("ProcessConfig", "executable_path")
    sleep_time_seconds = int(config.get("ProcessConfig", "sleep_time_seconds"))
    return process_name, executable_path, sleep_time_seconds

def open_settings():
    # Lê as configurações atuais do arquivo
    config_file = 'config.cfg'
    process_name, executable_path, sleep_time_seconds = read_config(config_file)

    window = tk.Tk()
    window.title("Configurações")

    process_name_label = tk.Label(window, text="Nome do Processo:")
    process_name_entry = tk.Entry(window)
    process_name_entry.insert(0, process_name)
    process_name_label.pack()
    process_name_entry.pack()

    executable_path_label = tk.Label(window, text="Caminho do Executável:")
    executable_path_entry = tk.Entry(window)
    executable_path_entry.insert(0, executable_path)
    executable_path_label.pack()
    executable_path_entry.pack()

    sleep_time_seconds_label = tk.Label(window, text="Intervalo de Tempo (segundos):")
    sleep_time_seconds_entry = tk.Entry(window)
    sleep_time_seconds_entry.insert(0, sleep_time_seconds)
    sleep_time_seconds_label.pack()
    sleep_time_seconds_entry.pack()

    save_button = tk.Button(window, text="Salvar", command=lambda: save_config(
        process_name_entry.get(),
        executable_path_entry.get(),
        sleep_time_seconds_entry.get()
    ))
    save_button.pack()

    window.mainloop()

def save_config(process_name, executable_path, sleep_time_seconds):
    config = configparser.ConfigParser()
    config['ProcessConfig'] = {
        'process_name': process_name,
        'executable_path': executable_path,
        'sleep_time_seconds': sleep_time_seconds
    }

    with open('config.cfg', 'w') as configfile:
        config.write(configfile)

    messagebox.showinfo("Info", "Configurações salvas!")
    
def close_program(icon, item):
    icon.stop()
    logger.info("Process monitor closed")
    os._exit(0)
    
def main():
    config_file = 'config.cfg'

    while True:
        process_name, process_executable_path, sleep_time_seconds = read_config(config_file)
        
        if is_process_running(process_name):
            continue
        else:
            logger.warning("Process '{}' is not running. Restarting...".format(process_name))
            restart_process(process_executable_path, process_name)

        time.sleep(sleep_time_seconds)

if __name__ == "__main__":
    time.sleep(1)
    
    logger = setup_logger()
    logger.info("Process monitor started")
    
    # Cria um ícone
    image = Image.new('RGB', (64, 64), color = 'red')

    # Cria o ícone da bandeja
    icon = pystray.Icon("name", image, "My System Tray Icon", menu=pystray.Menu(
    pystray.MenuItem('Open Settings', open_settings),
    pystray.MenuItem('Close Program', lambda icon, item: close_program(icon, item))))


    # Inicia a função main() em uma nova thread
    thread = threading.Thread(target=main)
    thread.start()

    icon.run()