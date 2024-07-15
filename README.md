# TiLauncher

TiLauncher - это библиотека для запуска игры Майнкрафт.

## Установка

Вы можете установить TiLauncher с помощью pip:

```bath
python -m pip install git+https://github.com/XTITAX/TiLauncher.git
```

## Использование

Импортируйте функции из пакета и вызовите их:

```python
import TiLauncher

# Запустить графический лаунчер (Скачается версия майнкрафта в папку C:\Users\Ваш пользователь\AppData\Roaming\.TiLauncher (Если её нету))
TiLauncher.StartL()

# Запустить консольный лаунчер (Скачается версия майнкрафта в папку C:\Users\Ваш пользователь\AppData\Roaming\.TiLauncher (Если её нету))
TiLauncher.StartC()

# Получить справку
TiLauncher.Help()
```
