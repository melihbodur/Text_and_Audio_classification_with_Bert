#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import webbrowser
from simpletransformers.classification import ClassificationModel
model = ClassificationModel(
    "bert", "checkpoint-117-epoch-3/",use_cuda=False)
root = Tk()
root.geometry("500x600")
root.configure(background="white")
Label(root, text="Türkçe Metin Sınıflandırma ", font=("Helvetica", 11, "bold"),
      bg="khaki", width=30).place(x=0, y=10)
Label(root, text="Metin Ekle", font=("Helvetica", 10, "bold"),
      bg="gray64", relief="solid", width=18).place(x=10, y=60)
Label(root, text="Türkçe Ses Sınıflandırma", font=("Helvetica", 11, "bold"),
      bg="khaki",  width=30).place(x=110, y=360)
Label(root, text="BERT", font=("Helvetica", 1),
      bg="dark slate gray", width=600).place(x=0, y=320)
def getTextInput():
    global c
    
    result=textExample.get("1.0","end")
    tahmin=model.predict([result])
    if tahmin[0][0] ==0:
        c="BİLİM VE TEKNOLOJİ"
    elif tahmin[0][0]==1:
        c="EKONOMİ"
    elif tahmin[0][0]==2:
        c="SAĞLIK"
    elif tahmin[0][0]==3:
        c="SİYASET"
    elif tahmin[0][0]==4:
        c="SPOR"
    else:
        c="BULUNAMADI"
    Label(root, text=c, bg="gray80", relief="solid", width=30).place(x=250, y=290)
textExample=Text(root, height=10)
textExample.place(x=10, y=90,width=480,height=200)
btnRead=Button(root, text="Metin Kategorisini Tahmin Et:", width=25,command=getTextInput).place(x=20, y=290)

def anka10():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=10)
    try:
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        c="BİLİM VE TEKNOLOJİ"
    elif tahmin[0][0]==1:
        c="EKONOMİ"
    elif tahmin[0][0]==2:
        c="SAĞLIK"
    elif tahmin[0][0]==3:
        c="SİYASET"
    elif tahmin[0][0]==4:
        c="SPOR"
    else:
        c="BULUNAMADI"
    Label(root, text=c, bg="gray80", relief="solid", width=25).place(x=280, y=420)
button =Button(root, text='Ses Kaydını Başlat (10sn)', width=20,command=anka10)
button.place(x=20, y=390)

def anka30():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=10)
    try:
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        c="BİLİM VE TEKNOLOJİ"
    elif tahmin[0][0]==1:
        
        c="EKONOMİ"
    elif tahmin[0][0]==2:
        c="SAĞLIK"
    elif tahmin[0][0]==3:
        c="SİYASET"
    elif tahmin[0][0]==4:
        c="SPOR"
    else:
        c="BULUNAMADI"
    Label(root, text=c, bg="gray80", relief="solid", width=25).place(x=280, y=420)
button =Button(root, text='Ses Kaydını Başlat (30sn)',width=25, command=anka30)
button.place(x=20, y=425)

def anka1():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = recognizer.listen(source, timeout=10)
    try:
        text = recognizer.recognize_google(
                recorded_audio, 
                language="tr-tr")

    except Exception as ex:
        print(ex)
    tahmin=model.predict([text])
    if tahmin[0][0] ==0:
        c="BİLİM VE TEKNOLOJİ"
    elif tahmin[0][0]==1:
        
        c="EKONOMİ"
    elif tahmin[0][0]==2:
        c="SAĞLIK"
    elif tahmin[0][0]==3:
        c="SİYASET"
    elif tahmin[0][0]==4:
        c="SPOR"
    else:
        c="BULUNAMADI"
    Label(root, text=c, bg="gray80", relief="solid", width=25).place(x=280, y=420)
button =Button(root, text='Ses Kaydını Başlat (1 dk)', width=30,command=anka1)
button.place(x=20, y=460)

def ankam():
    term=c
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)

    
button =Button(root, text='    Google    ', width=13,command=ankam)
button.place(x=190, y=57)
imgg = Image.open("mö.jpg")
imgg = imgg.resize((200, 87))
photoo=ImageTk.PhotoImage(imgg)
labb=Label(image=photoo).place(x=300, y=0)

imggg = Image.open("seso.jpg")
imggg = imggg.resize((550, 100))
photooo=ImageTk.PhotoImage(imggg)
labb=Label(image=photooo).place(x=0, y=500)
root.resizable(0, 0)
root.mainloop()

