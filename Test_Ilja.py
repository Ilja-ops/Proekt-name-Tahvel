import tkinter as tk

class MyWindow:
  def __init__(self): 
     self.window = tk.Tk()
     self.window.title("Andmete sisestamine")
     self.window.geometry("600x500")

# Заголовки
     tk.Label(self.window, text="Имя").grid(row=0, column=0)
     tk.Label(self.window, text="Фамилия").grid(row=0, column=1, padx=15)
        
        # Поля ввода (под ними)
     self.entry_name = tk.Entry(self.window)
     self.entry_name.grid(row=1, column=0)

     self.entry_surname = tk.Entry(self.window)
     self.entry_surname.grid(row=1, column=1, padx=15)

     tk.Label(self.window, text="Личный код").grid(row=2, column=0, columnspan=2)

        #поле ввода для личного кода
     self.entry_code = tk.Entry(self.window)
     self.entry_code.grid(row=3, column=0, columnspan=2, padx=15, pady=5)

  def run(self):
    self.window.mainloop()

app = MyWindow()
app.run()
