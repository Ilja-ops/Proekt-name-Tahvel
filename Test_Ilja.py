import tkinter as tk

class MyWindow:
  def __init__(self): 
  self.window = tk.Tk()
  self.window.title("Andmete sisestamine")
  self.window.geometry("600x500")

#name
self.label_name = tk.Label(self.window, text="Имя")
        self.label_name.pack()

#поле ввода
self.entry_name = tk.Entry(self.window)
self.entry_name.pack()
