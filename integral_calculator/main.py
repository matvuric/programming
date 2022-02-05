import tkinter as tk
from tkinter import *
from tkinter import messagebox

import lr1, lr2, lr3, lr4, lr61, lr62


def btnClickCalc1():
    if cbVariableLev.get() and cbVariablePost.get():
        show_message(lr1.permanent_integral(1, float(tInput1.get())))
    if cbVariablePrav.get() and cbVariablePost.get():
        show_message(lr1.permanent_integral(2, float(tInput1.get())))
    if cbVariableTrap.get() and cbVariablePost.get():
        show_message(lr1.permanent_integral(3, float(tInput1.get())))
    if cbVariablePar.get() and cbVariablePost.get():
        show_message(lr1.permanent_integral(4, float(tInput1.get())))
    if cbVariablePer.get():
        show_message(lr1.variable_integral(float(tInput1.get())))


def btnClickCalc2():
    show_message(lr2.multiple_integral(float(tInput2.get()), float(tInput3.get())))


def btnClickCalc3():
    show_message(lr3.sum(float(tInput4.get())))


def btnClickCalc4():
    show_message(lr4.sum(float(tInput5.get())))


def btnClickCalc5():
    show_message(lr61.sum())


def show_message(txt):
    messagebox.showinfo("Ответ", txt)


root = Tk()


cbVariableLev = tk.IntVar()
cbVariablePrav = tk.IntVar()
cbVariableTrap = tk.IntVar()
cbVariablePar = tk.IntVar()
cbVariablePost = tk.IntVar()
cbVariablePer = tk.IntVar()


root.geometry('1000x450')
root.configure(background='#F0F8FF')
root.title('Вычислительная математика')


Label(root, text='Численное интегрирование', bg='#F0F8FF', font=('arial', 14, 'normal')).place(x=10, y=14)
Label(root, text='Алгоритм', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=10, y=208)
Label(root, text='Кол-во разбиений', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=10, y=328)

Label(root, text='Кратные интегралы', bg='#F0F8FF', font=('arial', 14, 'normal')).place(x=350, y=14)
Label(root, text='Разбиение x', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=350, y=48)
Label(root, text='Разбиение y', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=350, y=128)

Label(root, text='Элементарные функции', bg='#F0F8FF', font=('arial', 14, 'normal')).place(x=700, y=14)
Label(root, text='x', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=700, y=48)

Label(root, text='Нелинейные уравнения', bg='#F0F8FF', font=('arial', 14, 'normal')).place(x=350, y=288)
Label(root, text='y', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=350, y=328)

Label(root, text='Дифференциальные уравнения', bg='#F0F8FF', font=('arial', 14, 'normal')).place(x=700, y=288)


CheckBoxLev = Checkbutton(root, text='Прямоугольники левых частей', variable=cbVariableLev, bg='#F0F8FF',
                          font=('arial', 12, 'normal'))
CheckBoxPrav = Checkbutton(root, text='Прямоугольники правых частей', variable=cbVariablePrav, bg='#F0F8FF',
                           font=('arial', 12, 'normal'))
CheckBoxTrap = Checkbutton(root, text='Трапеции', variable=cbVariableTrap, bg='#F0F8FF', font=('arial', 12, 'normal'))
CheckBoxPar = Checkbutton(root, text='Параболы', variable=cbVariablePar, bg='#F0F8FF', font=('arial', 12, 'normal'))
CheckBoxPost = Checkbutton(root, text='Постоянный шаг', variable=cbVariablePost, bg='#F0F8FF',
                           font=('arial', 12, 'normal'))
CheckBoxPer = Checkbutton(root, text='Переменный шаг', variable=cbVariablePer, bg='#F0F8FF',
                          font=('arial', 12, 'normal'))

CheckBoxLev.place(x=10, y=48)
CheckBoxPrav.place(x=10, y=88)
CheckBoxTrap.place(x=10, y=128)
CheckBoxPar.place(x=10, y=168)
CheckBoxPost.place(x=10, y=248)
CheckBoxPer.place(x=10, y=288)

tInput1 = StringVar()
tInput2 = StringVar()
tInput3 = StringVar()
tInput4 = StringVar()
tInput5 = StringVar()

tInput1_entry = Entry(textvariable=tInput1)
tInput1_entry.place(x=10, y=368)
tInput2_entry = Entry(textvariable=tInput2)
tInput2_entry.place(x=350, y=88)
tInput3_entry = Entry(textvariable=tInput3)
tInput3_entry.place(x=350, y=168)
tInput4_entry = Entry(textvariable=tInput4)
tInput4_entry.place(x=700, y=88)
tInput5_entry = Entry(textvariable=tInput5)
tInput5_entry.place(x=350, y=368)

Button(root, text='Вычислить', bg='#FFB6C1', font=('arial', 12, 'normal'), command=btnClickCalc1).place(x=10, y=408)
Button(root, text='Вычислить', bg='#FFB6C1', font=('arial', 12, 'normal'), command=btnClickCalc2).place(x=350, y=208)
Button(root, text='Вычислить', bg='#FFB6C1', font=('arial', 12, 'normal'), command=btnClickCalc3).place(x=700, y=128)
Button(root, text='Вычислить', bg='#FFB6C1', font=('arial', 12, 'normal'), command=btnClickCalc4).place(x=350, y=408)
Button(root, text='Вычислить', bg='#FFB6C1', font=('arial', 12, 'normal'), command=btnClickCalc5).place(x=700, y=328)

root.mainloop()
