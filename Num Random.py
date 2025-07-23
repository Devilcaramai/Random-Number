from tkinter import * #นำเข้าlibaryทั้งหมดของ tkinter
from tkinter import ttk #เรียกใช้ theme ของ tk
from tkinter import messagebox #เรียกใช้ libary messagebox ใน tkinter

GUI = Tk() #ให้กราฟฟิก user interface ใช้ ฟังชั่น Tk
GUI.title('โปรแกรมสุ่มตัวเลข') #กำหนดชื่อกราฟฟิก
GUI.geometry('500x400') #กำหนดขนาดหน้าจอกราฟฟิก

def Button1 (): #เปิดฟังชั้น button1
    import random #นำเข้าlibary random
    x1 = random.randint(0,9) #กำหนด x1 ให้สุ่มตัวเลข 0ถึง9
    x2 = random.randint(0,9)
    x3 = str(x1)+str(x2) #กำหนด ให้ x1 x2 เป็นตัวอักษร แล้วนำมาติดกัน
    text = x3
    messagebox.showinfo('ตัวเลขที่ออก',text) #กำหนดข้อความหลังกดปุ่ม ให้นำเข้าจากตัวแปร text

FB1 = LabelFrame(GUI,text='เลขท้าย 2 ตัว') #กำหนดกรอบของปุ่มพร้อมชื่อกรอบ
FB1.place(x=125,y=100) #กำหนดตำแหน่งของปุ่ม
B1 = ttk.Button(FB1,text='กดเพื่อสุ่ม',command=Button1) #ttk.button เป็นปุ่ม กำหนดให้ปุ่มมีกรอบFB1 ชื่อ กดแล้วโชว์ฟังชั่นจาก button1
B1.pack(ipadx=20,ipady=20,padx=40,pady=40) #กำหนดขนาดปุ่ม ขนาดกรอบ


GUI.mainloop()
