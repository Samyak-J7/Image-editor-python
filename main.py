from tkinter import filedialog
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image
from PIL import ImageDraw
import time
from functools import partial
import cv2
from PIL import ImageFont
def browseFiles():
    filename = filedialog.askopenfilename(title="Select a Image File",filetypes=[('image files', ('.png', '.jpg'))])
    return filename
def getFolderPath():
    folder_selected = filedialog.askdirectory(title="Select Destination Folder")
    return folder_selected
def submit(a,b,c):
    loc=browseFiles()
    im =Image.open(loc)
    im=im.resize((int(b.get()),int(a.get())))
    saveloc=getFolderPath()
    im.save(saveloc+"/"+c.get()+".jpg")

def sub(a,b):
    l=[]
    for i in range(2):
        loc=browseFiles()
        l.append(loc)
    img = Image.open(l[0])
    img1 = Image.open(l[1])
    sizee=img.size
    img1 = img1.resize(sizee)
    h=sizee[1]
    w=sizee[0]
    if a==2:
        img2 = Image.new("RGB", (w*2,h))
        img2.paste(img, (0, 0))
        img2.paste(img1, (w, 0))
        saveloc=getFolderPath()
        img2.save(saveloc+"/"+b.get()+".jpg")
    if a==1:
        img2 = Image.new("RGB", (w,h*2))
        img2.paste(img, (0, 0))
        img2.paste(img1, (0, h))
        saveloc=getFolderPath()
        img2.save(saveloc+"/"+b.get()+".jpg")
def Combine():
    t = tk.Tk()
    t.eval('tk::PlaceWindow . center')
    t.title("Combine Images")
    t.geometry('290x100')
    name_var=tk.StringVar()
    name_label = tk.Label(t, text = 'Image Save Name', font = ('calibre',10,'bold'))
    name_entry=Entry(t, textvariable = name_var, font = ('calibre',10,'normal'))
    dat=partial(sub,1,name_entry)
    dat2=partial(sub,2,name_entry)
    btn1 = Button(t, text = 'Vertical', width=40,command = dat)
    btn1.grid(row = 2, column = 0)
    btn2 = Button(t, text = 'Horizontal', width=40, command = dat2 )
    btn2.grid(row = 3, column = 0)
    name_label.grid(row=0,column=0)
    name_entry.grid(row=1,column=0)

def addt(a,b):

    loc=browseFiles()
    im =Image.open(loc)
    sizee=im.size
    h=sizee[1]
    w=sizee[0]
    ww=(w*20)/100
    hh=(h*85)/100
    I1 = ImageDraw.Draw(im)
    f = ImageFont.truetype('FreeMono.ttf', 25)
    I1.text((ww, hh),b.get(),font=f, fill=(255, 0, 0))
    saveloc=getFolderPath()
    im.save(saveloc+"/"+a.get()+".jpg")

def Text ():
    r=tk.Tk()
    r.geometry("290x110")
    r.title("Add Text")
    name_var=tk.StringVar()
    name_label = tk.Label(r, text = 'Image Save Name', font = ('calibre',10,'bold'))
    name_entry=Entry(r, textvariable = name_var, font = ('calibre',10,'normal'))
    tt=tk.StringVar()
    n = tk.Label(r, text = 'Text to add', font = ('calibre',10,'bold'))
    na=Entry(r, textvariable = tt, font = ('calibre',10,'normal'))
    dat=partial(addt,name_entry,na)
    btn=tk.Button(r,text = 'Select Image', width=40, command = dat)
    btn.grid(row = 4, column = 0)
    n.grid(row=0,column=0)
    na.grid(row=1,column=0)
    name_label.grid(row=2,column=0)
    name_entry.grid(row=3,column=0)
def Resize():
    roo=tk.Tk()
    roo.geometry("300x100")
    roo.title("Resizer")
    height_var=tk.StringVar()
    width_var=tk.StringVar()
    name_var=tk.StringVar()
    height_label = tk.Label(roo, text = 'Height', font=('calibre',10, 'bold'))
    height_entry = Entry(roo,textvariable = height_var, font=('calibre',10,'normal'))
    width_label = tk.Label(roo, text = 'Width', font = ('calibre',10,'bold'))
    width_entry=Entry(roo, textvariable = width_var, font = ('calibre',10,'normal'))
    name_label = tk.Label(roo, text = 'Image Save Name', font = ('calibre',10,'bold'))
    name_entry=Entry(roo, textvariable = name_var, font = ('calibre',10,'normal'))
    dat=partial(submit,height_entry,width_entry,name_entry)
    sub_btn=tk.Button(roo,text = 'Select Image', command = dat)
    height_label.grid(row=0,column=0)
    height_entry.grid(row=0,column=1)
    width_label.grid(row=1,column=0)
    width_entry.grid(row=1,column=1)
    name_label.grid(row=2,column=0)
    name_entry.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)
def subm(opt,name):
    loc = browseFiles()
    if opt==1:
        q=50
    elif opt==2:
        q=30
    elif opt==3:
        q=10
    im = Image.open(loc)
    saveloc = getFolderPath()
    im.save(saveloc + "/" + name.get() + ".jpg",optimize=True, quality=q)
def Compress():
    ro = Tk()
    ro.title("Compressor")
    ro.geometry('460x100')
    name_var=tk.StringVar()
    name_label = tk.Label(ro, text = 'Image Save Name', font = ('calibre',10,'bold'))
    name_entry=Entry(ro, textvariable = name_var, font = ('calibre',10,'normal'))
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    d1=partial(subm,1,name_entry)
    d2=partial(subm,2,name_entry)
    d3=partial(subm,3,name_entry)
    btn1 = Button(ro, text = 'Light Compress', width=43,command = d1)
    btn1.grid(row = 1, column = 1)
    btn2 = Button(ro, text = 'Medium Compress', width=43, command = d2)
    btn2.grid(row = 2, column = 1)
    btn3 = Button(ro, text = 'High Compress',  width=43,command = d3)
    btn3.grid(row = 3, column = 1)

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.title("Image Modifier")
root.geometry('310x100')
root.configure(background='black')

btn1 = Button(root, text = 'Resize', width=43,command = Resize)
btn1.grid(row = 0, column = 1)
btn2 = Button(root, text = 'Compress', width=43, command = Compress)
btn2.grid(row = 1, column = 1)
btn3 = Button(root, text = 'Combine',  width=43,command = Combine)
btn3.grid(row = 2, column = 1)
btn4 = Button(root, text = 'Add Text', width=43, command = Text)
btn4.grid(row = 3, column = 1)

root.mainloop()
