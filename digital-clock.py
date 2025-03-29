from tkinter import *
from time import strftime, gmtime,localtime

# إنشاء نافذة رئيسية
window = Tk()
window.title("digital-clock")
window.configure(background="lavender")
#إنشاء نافذة بأبعاد ثابتة
window.geometry("510x250")
window.resizable(False, False)

# تعريف دالة تعيد لناالتوقيت المحلي والعالمي

def get_time():
    # توقيت GMT\\%I نظام 12 ساعة\\%M الدقائق\\%S الثواني\\%p تعرض AM / PM
    timeFormat1 = strftime("%I:%M:%S %p", gmtime())
    clock_g.config(text="GMT: " + timeFormat1)
    # توقيت محلي بتنسيق 12 ساعة
    timeFormat2 = strftime("%I:%M:%S %p",localtime())
    clock_l.config(text="LOC: " + timeFormat2)
    # جدولة تكرار استدعاء الدالة كل 1000 ميلي ثانية
    window.after(1000, get_time)


clock_l = Label(window, font="Verdana 37 bold", pady=30, bg="lavender")
clock_l.pack(side=TOP)

clock_g = Label(window, font="Verdana 37 bold", pady=30, bg="pink")
clock_g.pack(side=BOTTOM)

# استدعاء دالة عرض الوقت
get_time()

# تشغيل النافذة الرئيسية
mainloop()