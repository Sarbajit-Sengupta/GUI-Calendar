from tkinter import *
import calendar

from tkinter import messagebox


def showCalender():
    try:
        year = int(year_field.get())
        if not 1 <= year <= 9999:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid year", "Enter a whole year from 1 to 9999.")
        return
    gui = Toplevel(new)
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',
fg='Black',bg='Blue',command=showCalender)

    #putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Button(new, text="Exit", command=new.destroy).grid(row=6, column=1)
    new.mainloop()