from tkinter import *
import time
from playsound import playsound

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.config(bg='blanched almond')
root.title('Đồng hồ đếm ngược - Countdown Timer')

Label(root, text="CountDown Timer", font='arial 20 bold', bg='papaya whip').pack()
Label(root, font='arial 15 bold', text='Giờ hiện tại:', bg='papaya whip').place(x=40, y=20)
curr_time = Label(root, font='arial 15 bold', text='', fg='gray25', bg='papaya whip')
curr_time.place(x=190, y=70)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text=clock_time)
    curr_time.after(1000, clock)


clock()

# Khai báo biến cho giờ, phút, giây
sec = StringVar()
Entry(root, textvariable=sec, width=2, font='arial 12').place(x=250, y=155)
sec.set('00')

mins = StringVar()
Entry(root, textvariable=mins, width=2, font='arial 12').place(x=225, y=155)
mins.set('00')

hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font='arial 12').place(x=200, y=155)
hrs.set('00')

# Biến để theo dõi trạng thái của đồng hồ đếm ngược
counting = False


def countdown():
    global counting
    counting = True
    total_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    
    while total_time >= 0 and counting:
        hour = total_time // 3600
        minute = (total_time % 3600) // 60
        second = total_time % 60
        
        hrs.set(f"{hour:02d}")  # Định dạng hai chữ số
        mins.set(f"{minute:02d}")  # Định dạng hai chữ số
        sec.set(f"{second:02d}")  # Định dạng hai chữ số
        
        root.update()
        time.sleep(1)
        total_time -= 1  # Giảm thời gian sau mỗi giây

    if counting:
        # Phát âm thanh khi đếm ngược kết thúc
        playsound('Loud_Alarm_Clock_Buzze.mp3')
        sec.set('00')
        mins.set('00')
        hrs.set('00')


def stop_countdown():
    global counting
    counting = False  # Đặt biến counting thành False để dừng đếm ngược


Label(root, font='arial 15 bold', text='Đặt thời gian:', bg='papaya whip').place(x=40, y=150)
Button(root, text='BẮT ĐẦU', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)
Button(root, text='DỪNG', bd='5', command=stop_countdown, bg='antique white', font='arial 10 bold').place(x=150, y=250)

root.mainloop()
