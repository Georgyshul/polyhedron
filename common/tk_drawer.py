# -*- coding: utf-8 -*-
from tkinter import *

SIZE = 900
SCALE = 1.5


def x(p):
    """ преобразование x-координаты """
    return SIZE / 2 + SCALE * p.x


def y(p):
    """" преобразование y-координаты """
    return SIZE / 2 - SCALE * p.y


class TkDrawer:
    """ Графический интерфейс """

    def __init__(self):
        self.root = Tk()
        self.root.title("Изображение проекции полиэдра")
        self.root.geometry(f"{SIZE+5}x{SIZE+5}")
        self.root.resizable(False, False)
        self.root.bind('<Control-c>', quit)
        self.canvas = Canvas(self.root, width=SIZE, height=SIZE)
        self.canvas.pack(padx=5, pady=5)
    
    def close(self):
        self.root.quit()
    
    def clean(self):
        self.canvas.create_rectangle(0, 0, SIZE, SIZE, fill="white")
        self.root.update()
    
    def draw_line(self, p, q):
        self.canvas.create_line(x(p), y(p), x(q), y(q), fill="black", width=1)
        self.root.update()
