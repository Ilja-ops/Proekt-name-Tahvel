import customtkinter as ctk

class MyWindow:
  def __init__(self):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
     self.window = ctk.CTk()
     self.window.title("Tahvel")
     self.window.geometry("500x600")
#коробка которая не даст поля ввода быть разбросанными 
#kast, mis hoiab sisestusväljad korras 
    
# Заголовок
# Pealkirja
    ctk.CTkLabel(frame, text="Registreerimine", font=("Arial", 20)).pack(pady=10)
    # Поля ввода
    # Sisestusväljad 
     self.entry_name = ctk.CTkEntry(frame, placeholder_text="Имя")
     self.entry_name.pack(pady=5, fill="x")

     self.entry_surname = ctk.CTkEntry(frame, placeholder_text="Фамилия")
     self.entry_surname.pack(pady=5, fill="x")

     tk.Label(self.window, text="Личный код").grid(row=2, column=0, columnspan=2,sticky="w", padx=15)
#поле ввода для личного кода
#isikliku koodi sisestusväli
     self.entry_code = tk.Entry(self.window)
     self.entry_code.grid(row=3, column=0, columnspan=2, padx=1, pady=5, sticky="w")

# Номер телефона (справа)
#Telefoninumber (paremal)
     tk.Label(self.window, text="Номер телефона").grid(row=0, column=15, sticky="e", padx=10)

     self.entry_phone = tk.Entry(self.window)
     self.entry_phone.grid(row=1, column=15, sticky="e", padx=10)
#под фамилией в центре
#perekonnanime all keskel
     tk.Label(self.window, text="Дата рождения").grid(row=2, column=1, padx=15)
     
     self.entry_surname = tk.Entry(self.window)
     self.entry_surname.grid(row=3, column=1, padx=15)
#под номером телефона
#telefoninumbri all
     tk.Label(self.window, text="Год окончания школы").grid(row=2, column=15, sticky="e", padx=10)

     self.entry_kool = tk.Entry(self.window)
     self.entry_kool.grid(row=3, column=15, sticky="e", padx=10)
#под датой рождения
#sünnikuupäeva all
     tk.Label(self.window, text="Пол").grid(row=4, column=1, padx=15)
     
     self.entry_sugu = tk.Entry(self.window)
     self.entry_sugu.grid(row=5, column=1, padx=15)

  # кнопка сохранить
  #salvestamise nupp
    tk.Button(self.window, text="Сохранить", command=self.save).grid(row=6, column=0, columnspan=2)
#здесь мы пишем то что будет сохранять
#siin kirjutame selle, mis salvestatakse
 def save(self):
      name = self.entry_name.get()
      surname = self.entry_surname.get()
      code = self.entry_code.get()
      phone = self.entry_phone.get()
      age = self.entry_age.get()
      school = self.entry_kool.get()
      gender = self.entry_sugu.get()
# сохраняем в файл
# salvestame faili
     with open("data.txt", "w", encoding="utf-8") as f:
          f.write(name + "\n")
          f.write(surname + "\n")
          f.write(code + "\n")
          f.write(phone + "\n")
          f.write(age + "\n")
          f.write(school + "\n")
          f.write(gender + "\n")
# открываем новое окно
# avame uue akna
      self.open_andme()
# новое окно 
# uus aken 
def open_andme(self):
      andme = tk.Toplevel(self.window)
      andme.title("Andmete sisestamine")
      andme.geometry("450x200")

      tk.Label(self.window, text="Aadress").grid(row=0, column=0)
      tk.Label(self.window, text="Esindaja").grid(row=0, column=1, padx=15)

      self.entry_aadress = tk.Entry(andme)
      self.entry_aadress.grid(row=1, column=0)

      self.entry_esindaja = tk.Entry(andme)
      self.entry_esindaja.grid(row=1, column=1, padx=15)

def run(self):
    self.window.mainloop()

app = MyWindow()
app.run()
