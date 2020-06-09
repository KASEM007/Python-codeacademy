from tkinter import *
import calendar


def show_cal():
    # Create a GUI
    new_gui = TK()

    # setting background color of GUI window
    new_gui.config(background="white")

    # setting the name of tkinter GUI window
    new_gui.title("Calender")

    # setting the config of GUI window
    new_gui.geometry("550x600")

    # get method returns current text as string
    fetch_year = int(year_field.get())

    # calendar method of calendar module return
    # the calendar of the given year.
    cal_content = calendar.calendar(fetch_year)

    # create a label for showing the content of the calendare
    cal_year = label(new_gui, text=cal_content, font="consolas 10 bold")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row=5, column=1, padx=20)

    # start the GUI
    new_gui.mainloop()


# # Drive code
# if __name__ == "__main__":
#     # creat a GUI window
#     gui = Tk()

#     # set the background color of GUI window
#     gui.config(background="white")

#     # set the name of tkinter GUI window
#     gui.title("Calender")

#     # set the configuration of GUI window
#     gui.geometry("250x140")

#     # Create a calendar: label with specified font and size
#     cal = label(gui, text="Calendar", bg="dark grey", font=("times", 28, "bold"))

#     # create a Enter year:label
#     year = label(gui, text="Enter Year", bg="light green")

#     # create a text entry box for filling or typing the information.
#     year_field = Entry(gui)

#     # create a show calendar Button and attached to showCal function
#     Show = Button(gui, text="Show Calendar", fg="Black", bg="Red", command=showCal)

#     # Create a Exit Button and attached to exit function
#     Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

#     # grid method is used for placing
#     # the widgest ar respective positions
#     # in table like structure.
#     cal.grid(row=1, column=1)

#     year.grid(row=2, column=1)

#     year_field.grid(row=3, column=1)

#     show.grid(row=4, column=1)

#     Exit.grid(row=6, column=1)

#     # start the GUI
#     gui.mainloop()
