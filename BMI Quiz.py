import tkinter
from tkinter import *

window= Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)
window.config(padx=20,pady=20)

#label
my_label=Label(text="Enter Your Weight (kg)")
my_label.config(fg="black")
my_label.config(padx=10,pady=10)
my_label.pack()

#entry
my_entry=Entry(width=20)
#my_entry.focus()
my_entry.pack()

#2. label
my_label_2=Label(text="Enter Your Height (cm)")
my_label_2.config(fg="black")
my_label_2.config(padx=10,pady=10)
my_label_2.pack()

#2. entry
my_entry_2=Entry(width=20)
#my_entry.focus()
my_entry_2.pack()

def get_Weight():
    global kilo
    kilo = int(my_entry.get())

def get_Height():
    global boy
    boy = int(my_entry_2.get())

# 3. Label
my_label_3 = Label(text="",fg="black")
my_label_3.config(padx=10, pady=10)

# 4. Label
my_label_4 = Label(text="",fg="black")
my_label_4.config(padx=10, pady=10)

# 5. Label
my_label_5 = Label(text="",fg="black")
my_label_5.config(padx=10, pady=10)

# 6. Label
my_label_6 = Label(text="",fg="black")
my_label_6.config(padx=10, pady=10)


def click_button():
    global bmi
    kilo = my_entry.get()
    boy = my_entry_2.get()
    if not kilo or not boy:
        my_label_3.pack_forget()
        my_label_4.pack_forget()
        my_label_5.config(text="Please enter both weight and height!")
        my_label_5.pack()
        return
    my_label_5.pack_forget()
    try:
        kilo = float(my_entry.get())
        boy = float(my_entry_2.get())
    except ValueError:
        my_label_3.pack_forget()
        my_label_4.pack_forget()
        my_label_6.config(text="Enter a valid number!", fg="black")
        my_label_6.pack_forget()
        my_label_6.pack()
        return
    my_label_3.pack_forget()
    my_label_4.pack_forget()
    my_label_6.pack_forget()
    bmi = kilo / (boy * boy / 10000)
    my_label_3.config(text=f"Your BMI is: {bmi:.2f}")
    my_label_3.pack()
    if bmi < 18.5:
        kategori = "Under Weight"
    elif 18.5 <= bmi < 24.9:
        kategori = "Normal"
    elif 25 <= bmi < 29.9:
        kategori = "Over Weight"
    elif 30 <= bmi < 34.9:
        kategori = "Obesity class I"
    elif 35 <= bmi < 39.9:
        kategori = "Obesity class II"
    else:
        kategori = "Extreme Obesity"

    my_label_4.config(text=f"You are: {kategori}")
    my_label_4.pack()

#button
my_button=tkinter.Button(text="Calculate" , command=click_button)
my_button.update()
my_button.pack()



window.mainloop()