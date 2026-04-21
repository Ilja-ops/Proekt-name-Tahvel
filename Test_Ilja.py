import tkinter as tk

class MyWindow:
  def __init__(self): 
     self.window = tk.Tk()
     self.window.title("Andmete sisestamine")
     self.window.geometry("450x200")

# Заголовки
     tk.Label(self.window, text="Имя").grid(row=0, column=0)
     tk.Label(self.window, text="Фамилия").grid(row=0, column=1, padx=15)
        
        # Поля ввода (под ними)
     self.entry_name = tk.Entry(self.window)
     self.entry_name.grid(row=1, column=0)

     self.entry_surname = tk.Entry(self.window)
     self.entry_surname.grid(row=1, column=1, padx=15)

     tk.Label(self.window, text="Личный код").grid(row=2, column=0, columnspan=2,sticky="w", padx=15)

#поле ввода для личного кода
     self.entry_code = tk.Entry(self.window)
     self.entry_code.grid(row=3, column=0, columnspan=2, padx=1, pady=5, sticky="w")

# Номер телефона (справа)
     tk.Label(self.window, text="Номер телефона").grid(row=0, column=15, sticky="e", padx=10)

     self.entry_phone = tk.Entry(self.window)
     self.entry_phone.grid(row=1, column=15, sticky="e", padx=10)
#под фамилией в центре
     tk.Label(self.window, text="Дата рождения").grid(row=2, column=1, padx=15)
     
     self.entry_surname = tk.Entry(self.window)
     self.entry_surname.grid(row=3, column=1, padx=15)
#под номером телефона
     tk.Label(self.window, text="Год окончания школы").grid(row=2, column=15, sticky="e", padx=10)

     self.entry_kool = tk.Entry(self.window)
     self.entry_kool.grid(row=3, column=15, sticky="e", padx=10)
#под датой рождения
     tk.Label(self.window, text="Пол").grid(row=4, column=1, padx=15)
     
     self.entry_sugu = tk.Entry(self.window)
     self.entry_sugu.grid(row=5, column=1, padx=15)

  # кнопка сохранить
    tk.Button(self.window, text="Сохранить", command=self.save).grid(row=6, column=0, columnspan=2)

       
  def run(self):
    self.window.mainloop()

app = MyWindow()
app.run()
