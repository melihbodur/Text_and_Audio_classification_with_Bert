#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import speech_recognition as sr
import webbrowser
from simpletransformers.classification import ClassificationModel

#-- Functions --#

def getTextInput():
    global c
    result = textExample.get("1.0","end")
    tahmin=model.predict([result])
    if tahmin[0][0] ==0:
        messagebox.showinfo("Sonuç","Konu: Bilim ve Teknoloji")
        c="Bilim ve Teknoloji"
    elif tahmin[0][0]==1:
        messagebox.showinfo("Sonuç","Konu: Ekonomi")
        c="Ekonomi"
    elif tahmin[0][0]==2:
        messagebox.showinfo("Sonuç","Konu: Sağlık")
        c="Sağlık"
    elif tahmin[0][0]==3:
        messagebox.showinfo("Sonuç","Konu: Siyaset")
        c="Siyaset"
    elif tahmin[0][0]==4:
        messagebox.showinfo("Sonuç","Konu: Spor")
        c="Spor"
    else:
        messagebox.showwarning("Sonuç","Kategori Listesinde Konunuza Ulaşamadık!")

def record_10s():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=10)
    try:
        messagebox.showinfo("Sonuç","Kayıt Tamamlandı. Sonuç için Tamam'a basın.")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        messagebox.showinfo("Sonuç","Konu: Bilim ve Teknoloji")
        c="Bilim ve Teknoloji"
    elif tahmin[0][0]==1:
        messagebox.showinfo("Sonuç","Konu: Ekonomi")
        c="Ekonomi"
    elif tahmin[0][0]==2:
        messagebox.showinfo("Sonuç","Konu: Sağlık")
        c="Sağlık"
    elif tahmin[0][0]==3:
        messagebox.showinfo("Sonuç","Konu: Siyaset")
        c="Siyaset"
    elif tahmin[0][0]==4:
        messagebox.showinfo("Sonuç","Konu: Spor")
        c="Spor"
    else:
        messagebox.showwarning("Sonuç","Kategori Listesinde Konunuza Ulaşamadık!")

def record_30s():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=30)
        
    try:
        messagebox.showinfo("Sonuç","Kayıt Tamamlandı. Sonuç için Tamam'a basın.")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        messagebox.showinfo("Sonuç","Konu: Bilim ve Teknoloji")
        c="Bilim ve Teknoloji"
    elif tahmin[0][0]==1:
        messagebox.showinfo("Sonuç","Konu: Ekonomi")
        c="Ekonomi"
    elif tahmin[0][0]==2:
        messagebox.showinfo("Sonuç","Konu: Sağlık")
        c="Sağlık"
    elif tahmin[0][0]==3:
        messagebox.showinfo("Sonuç","Konu: Siyaset")
        c="Siyaset"
    elif tahmin[0][0]==4:
        messagebox.showinfo("Sonuç","Konu: Spor")
        c="Spor"
    else:
        messagebox.showwarning("Sonuç","Kategori Listesinde Konunuza Ulaşamadık!")

def record_1m():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=60)
    try:
        messagebox.showinfo("Sonuç","Kayıt Tamamlandı. Sonuç için Tamam'a basın.")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        messagebox.showinfo("Sonuç","Konu: Bilim ve Teknoloji")
        c="Bilim ve Teknoloji"
    elif tahmin[0][0]==1:
        messagebox.showinfo("Sonuç","Konu: Ekonomi")
        c="Ekonomi"
    elif tahmin[0][0]==2:
        messagebox.showinfo("Sonuç","Konu: Sağlık")
        c="Sağlık"
    elif tahmin[0][0]==3:
        messagebox.showinfo("Sonuç","Konu: Siyaset")
        c="Siyaset"
    elif tahmin[0][0]==4:
        messagebox.showinfo("Sonuç","Konu: Spor")
        c="Spor"
    else:
        messagebox.showwarning("Sonuç","Kategori Listesinde Konunuza Ulaşamadık!")

def search_google():
    term=c
    if term == "":
        messagebox.showwarning("Eşleşen bir kategori bulunamadı!")
    url = "https://www.google.com.tr/search?q={}+hakkında+yazılar".format(term)
    webbrowser.open_new_tab(url)
        
def help_page():
    help_text="""    Metinden veya Sesten Konu Sınıflandırma Programımızı tercih ettiğiniz için teşekkür ederiz.
    Programımız 2 kısımdan oluşmaktadır. Bunlar:
    
    1-)Metinden Konu Sınıflandırma
    
    •İlk olarak, konusunu merak ettiğiniz Türkçe bir metni metin kutusuna yapıştırın.
    •Daha sonra 'Metnin Kategorisini Tahmin Et' adlı butona tıklayarak, konusunu merak 
    ettiğiniz metnin konusunu öğrenebilirsiniz.
    •Ayrıca konu ile ilgili daha fazla içeriğe 'Nette Ara' adlı buton ile ulaşabilirsiniz.
        
    2-)Sesten Konu Sınıflandırma
    
    •İlk olarak, konusunu merak ettiğiniz Türkçe cümle veya cümle öbeklerini ne kadar sürede 
    anlatabileceğinizi belirleyin(10s,30s ya da 1dk).
    •Daha sonra belirlediğiniz süreye ait butona tıklayarak, içeriğin konusunu öğrenebilirsiniz.
    •Ayrıca konu ile ilgili daha fazla içeriğe 'Nette Ara' adlı buton ile ulaşabilirsiniz.
        
    Yapımcı ve Fikir Sahibi: Melih BODUR
    Arayüz Tasarımcısı: Furkan İZGİ
    """
    
    helppage = Toplevel(root)
    helppage.title("Yardım")
    helppage.geometry("820x330")
    helppage.resizable(False, False)
    
    textbox = Text(helppage,width=820,height=330,bg="#DFEEE8",fg="black")
    textbox.insert(END,help_text)
    textbox['state'] = 'disabled' #It do not allow to write anything in textbox.
    textbox.pack()
    
#-- Main Codes --#
  
model = ClassificationModel(
    "bert", "checkpoint-117-epoch-3/",use_cuda=False)
root = Tk()
root.geometry("500x600")
root.resizable(False, False)
root.title("Metinden veya Sesten Konu Sınıflandırma Programı")
root.configure(background="#3D4866")
#-- Widgets and Buttons --#

Label(root, text="Türkçe Metin Sınıflandırma ", font=("Helvetica", 11, "bold"),
      bg="#E3AC54", width=30,anchor="center").place(x=0, y=10)


Label(root, text="Türkçe Ses Sınıflandırma", font=("Helvetica", 11, "bold"),
      bg="#E3AC54",  width=30,anchor="center").place(x=0, y=340)

textExample=Text(root, height=10)
textExample.place(x=10, y=90,width=480,height=200)

btn_guess=Button(root, text="Metnin Kategorisini Tahmin Et", width=25,command=getTextInput,anchor="center").place(x=10, y=295)
btn_rec10s =Button(root, text='Ses Kaydını Başlat (10sn)', width=30,command=record_10s,anchor="center").place(x=145, y=390)
btn_rec30s =Button(root, text='Ses Kaydını Başlat (30sn)',width=30, command=record_30s,anchor="center").place(x=145, y=425)
btn_rec1m =Button(root, text='Ses Kaydını Başlat (1 dk)', width=30,command=record_1m,anchor="center").place(x=145, y=460)
btn_search =Button(root, text='Nette Ara', width=13,command=search_google,anchor="center").place(x=10, y=50)
btn_help =Button(root, text='Yardım', width=13,command=help_page,anchor="center").place(x=390, y=50)

img_bot = Image.open("photo_bot.jpg")# Image in bottom side
img_bot = img_bot.resize((500, 100))
photo_bot=ImageTk.PhotoImage(img_bot)
label_bot=Label(image=photo_bot)
label_bot['bg'] = root['bg']# Now background and picture in the bottom has a same colour.
label_bot.place(x=0, y=500)

root.resizable(0, 0)
root.mainloop()
