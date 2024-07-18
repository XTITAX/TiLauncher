import TiLauncher as Ti
import Pas

x = input('Введите пароль для запуска Майнкрафт Лаунчера')
if(Pas.Pas() == x):
    Ti.StartL()