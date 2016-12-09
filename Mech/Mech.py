# coding=utf-8


# Основной класс механик
class MechObject (object):
    pass


# Повреждение
class Damage (MechObject):
    pass


# Движение
class Moving (MechObject):
    pass


# Игрок
class Player (Moving, Damage):
    pass


# Враг
class Enemy (Player):
    pass
