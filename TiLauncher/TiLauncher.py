import minecraft_launcher_lib
import tkinter as tk
from tkinter import ttk
import subprocess
from PIL import Image, ImageTk
import os
import uuid
import json
import threading
import time

def StartL():
    window = tk.Tk()
    window.title("TiLauncher")
    window.geometry("300x210")

    # Добавление иконки
    icon_path = os.path.join(os.path.dirname(__file__), "minecraft.png")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    window.iconphoto(True, icon_photo)

    # Получаем список доступных версий
    version_list = minecraft_launcher_lib.utils.get_version_list()

    # Создаем выпадающий список для выбора версии
    version_label = tk.Label(window, text="Выберите версию майнкрафта: ")
    version_label.pack(pady=5)

    version_combobox = ttk.Combobox(window, values=[v['id'] for v in version_list])
    version_combobox.pack()

    username_label = tk.Label(window, text="Введите своё имя: ")
    username_label.pack(pady=5)

    username_entry = tk.Entry(window)
    username_entry.pack()

    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'TiLauncher')

    # Создаем метку для отображения статуса
    status_label = tk.Label(window, text="")
    status_label.pack(side='bottom', pady=5)

    # Создаем индикатор прогресса
    progress_bar = ttk.Progressbar(window, length=280, mode='determinate')
    progress_bar.pack(side='bottom', pady=5)

    def set_status(status: str):
        status_label.config(text=status)
        window.update_idletasks()

    def set_progress(progress: int):
        progress_bar['value'] = progress
        window.update_idletasks()

    def set_max(max_value: int):
        progress_bar['maximum'] = max_value
        window.update_idletasks()

    def install_minecraft(version):
        callback = {
            "setStatus": set_status,
            "setProgress": set_progress,
            "setMax": set_max
        }
        minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory, callback=callback)

    def launch_minecraft():
        version = version_combobox.get()
        username = username_entry.get()
        if version != '' and username != '':
            launch_button.config(state='disabled')
            
            def installation_thread():
                install_minecraft(version)
                
                user_uuid = str(uuid.uuid4())
                
                options = {
                    'username': username,
                    'uuid': user_uuid,
                    'token': '',
                    'launcherName': 'TiLauncher',
                    'launcherVersion': '1.0',
                    'gameDirectory': minecraft_directory,
                    'jvmArguments': ['-Xmx2G'],
                    'demo': False,
                    'customResolution': False,
                    'resolutionWidth': '854',
                    'resolutionHeight': '480',
                }

                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options)
                print(minecraft_command)
                subprocess.Popen(minecraft_command)
                
                launch_button.config(state='normal')
                set_status("Игра запущена!")

            thread = threading.Thread(target=installation_thread)
            thread.start()

    launch_button = tk.Button(window, text="Запустить Майнкрафт", command=launch_minecraft)
    launch_button.pack(pady=10)

    window.mainloop()

def StartC():
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'TiLauncher')
    def install_minecraft(version):
        #callback = {
        #    "setStatus": set_status,
        #    "setProgress": set_progress,
        #    "setMax": set_max
        #}
        minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)#, callback=callback)

    version = input("Введите версию майнкрафта: ")
    username = input("Введите своё имя: ")
    if version != '' and username != '':
        
        def installation_thread():
            install_minecraft(version)
            
            user_uuid = str(uuid.uuid4())
            
            options = {
                'username': username,
                'uuid': user_uuid,
                'token': '',
                'launcherName': 'TiLauncher',
                'launcherVersion': '1.0',
                'gameDirectory': minecraft_directory,
                'jvmArguments': ['-Xmx2G'],
                'demo': False,
                'customResolution': False,
                'resolutionWidth': '854',
                'resolutionHeight': '480',
            }

            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options)
            print(minecraft_command)
            subprocess.Popen(minecraft_command)
            
            set_status("Игра запущена!")

        thread = threading.Thread(target=installation_thread)
        thread.start()

def Help():
    return print('''    Это библиотека для запуска игры Майнкрафт.
    У этой библиотеки есть команды, такие как Help(), которую вы сейчас использовали, а есть ещё две:
    StartL() - Она запускает Лаунчер Майнкрафта (Скачается версия майнкрафта в папку C:\Users\Ваш пользователь\AppData\Roaming\.TiLauncher (Если её нету)),
    StartC() - Она запускает консольную версию Лаунчера Майнкрафт.''')
