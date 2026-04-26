import customtkinter as ctk

class MyWindow:
  def __init__(self):
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    self.window = ctk.CTk()
    self.window.title("Tahvel")
    self.window.geometry("500x600")
# создает по типу коробки в котором будут поля ввода  #fill=both делает коробку
# loob kasti tüüpi, milles on sisestusväljad   #fill=both loob raami
    frame = ctk.CTkFrame(self.window)
    frame.pack(pady=20, padx=20, fill="both", expand=True) 
# Заголовок  #pady=10 делает отступ по вертикали
# Pealkirja  #pady=10 loob vertikaalse taanduse
    ctk.CTkLabel(frame, text="Registreerimine", font=("Arial", 20)).pack(pady=10)
# Поля ввода
# Sisestusväljad 

# поле ввода под имя(внутри поля)  #fill="x" заставляет растягиватся по горизонтали на всю доступную ширину
# nime sisestusväli (välja sees)  #fill=„x“ sunnib seda horisontaalselt kogu kättesaadava laiuseni venima
    self.entry_name = ctk.CTkEntry(frame, placeholder_text="Nimi")
    self.entry_name.pack(pady=5, fill="x")
# поле ввода под фамлию(внутри поля)   #.pack размещает все слова в столбик
# perekonnanime sisestusväli (välja sees)   #.pack paigutab kõik sõnad ühte veergu
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

    self.entry_email = ctk.CTkEntry(frame, placeholder_text="Email")
    self.entry_email.pack(pady=5, fill="x")

    self.entry_lang = ctk.CTkEntry(frame, placeholder_text="suhtluskeel")
    self.entry_lang.pack(pady=5, fill="x")

# кнопка сохранить   # padx=20 делает горизонтальный отступ
# salvestamise nupp  # padx=20 loob horisontaalse tühiku
    ctk.CTkButton(frame, text="Registreeruda", command=self.save).pack(padx=20)
# здесь мы пишем то что будет сохранять
# siin kirjutame selle, mis salvestatakse
def save(self):
andmed = [
      self.entry_name.get(),
      self.entry_surname.get(),
      self.entry_code.get(),
      self.entry_phone.get(),
      self.entry_age.get(),
      self.entry_school.get(),
      self.entry_sugu.get(),
      self.entry_address.get(),
# сохраняем в файл
# salvestame faili
with open("andmed.txt", "w") as f:
     for i in andmed:
         f.write(i + "\n")
       
print("Registreeritud")
#закрывает окно с регистрацией и открывает окно с профилем
#sulgeb registreerimisakna ja avab profiiliakna
self.window.destroy()
self.open_profile()
#создает новое окно под профиль
#loob profiili jaoks uue akna
def open_profile(self):
    profile = ctk.CTk()
    profile.title("Профиль")
    profile.geometry("600x600")
#создал по типу коробки что бы в нем находились все данные
#Lõin kasti tüüpi struktuuri, et kõik andmed oleksid seal olemas
frame = ctk.CTkFrame(profile)
frame.pack(pady=20, padx=20, fill="both", expand=True)
#добавил надпись окна
#lisasin akna sildi
ctk.CTkLabel(frame, text="Profiil", font=("Arial", 22)).pack(pady=15)
# читает текстовый файл и потом данные с файла возвращает в окно с профилем 
# loeb tekstifaili ja kuvab seejärel faili andmed profiiliaknas 
with open("andmed.txt", "r") as f:
     andmed = f.readlines()

lists = [
            "Nimi",
            "perekonnanimi",
            "isikukood",
            "Telefon",
            "Sünnikuupäev",
            "Kooli lõpetamise aasta",
            "sugu",
            "Aadress",
            "Email",
            "suhtluskeel"
        ]

        table = ctk.CTkFrame(frame)
        table.pack(pady=10, fill="both", expand=True)

        for i in range(len(lists)):

          
def run(self):
    self.window.mainloop()

app = MyWindow()
app.run()
