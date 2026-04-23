import customtkinter as ctk

class MyWindow:
  def __init__(self):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    self.window = ctk.CTk()
    self.window.title("Tahvel")
    self.window.geometry("500x600")
# коробка которая не даст поля ввода быть разбросанными 
# kast, mis hoiab sisestusväljad korras 
    
# Заголовок
# Pealkirja
    ctk.CTkLabel(frame, text="Registreerimine", font=("Arial", 20)).pack(pady=10)
# Поля ввода
# Sisestusväljad 

# поле под имя(внутри поля)
# nimeväli (välja sees)
    self.entry_name = ctk.CTkEntry(frame, placeholder_text="Nimi")
    self.entry_name.pack(pady=5, fill="x")
# поле под фамлию(внутри поля)
# perekonnanime väli (välja sees)
    self.entry_surname = ctk.CTkEntry(frame, placeholder_text="perekonnanimi")
    self.entry_surname.pack(pady=5, fill="x")
# поле под личный код(внутри поля)
# isikliku koodi väli (välja sees)
    self.entry_code = ctk.CTkEntry(frame, placeholder_text="isikukood")
    self.entry_code.pack(pady=5, fill="x")
# поле под телефон(внутри поля)
# telefoninumber (välja sees)
    self.entry_phone = ctk.CTkEntry(frame, placeholder_text="Telefon")
    self.entry_phone.pack(pady=5, fill="x")
# поле под дату рождения(внутри поля)
# sünnikuupäeva väli (välja sees)
    self.entry_age = ctk.CTkEntry(frame, placeholder_text="Sünnikuupäev")
    self.entry_age.pack(pady=5, fill="x")
# поле под год окончания школы(внутри поля)
# kooli lõpetamise aasta väli (välja sees)
    self.entry_school = ctk.CTkEntry(frame, placeholder_text="Kooli lõpetamise aasta")
    self.entry_school.pack(pady=5, fill="x")
# поле под пол(внутри поля)
# väli sugu all (välja sees)  
    self.entry_sugu = ctk.CTkEntry(frame, placeholder_text="sugu")
    self.entry_sugu.pack(pady=5, fill="x")
# поле под адрес(внутри поля)
# aadressiväli (välja sees)
    self.entry_sugu = ctk.CTkEntry(frame, placeholder_text="Aadress")
    self.entry_sugu.pack(pady=5, fill="x")

# кнопка сохранить
# salvestamise nupp
    Ctk.CTkButton(frame, text="Registreeruda", command=self.save).pack(padx=20)
# здесь мы пишем то что будет сохранять
# siin kirjutame selle, mis salvestatakse
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

def run(self):
    self.window.mainloop()

app = MyWindow()
app.run()
