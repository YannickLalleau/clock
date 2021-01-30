#Import
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import time as t


def fixedfont(size):
    return font.Font(family='Source Code Pro Light', size=size, weight='normal')


def fixedfontbold(size):
    return font.Font(family='Source Code Pro Light', size=size, weight='bold')


class App:
    def __init__(self):

        self.mode = "HOUR"
        self.offColor = "#3e3e3e"
        self.onColor = "white"

        # ROOT WINDOW
        self.root = Tk()
        self.root.configure(background='black')
        self.root.title("Clock")
        # make it cover the entire screen
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.focus_set()
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_state("zoomed")
        self.root.protocol("WM_DELETE_WINDOW", self.destroy)

        self.lettres = [
            ["I", "L", "N", "E", "S", "T", "O", "D", "E", "U", "X"],
            ["Q", "U", "A", "T", "R", "E", "T", "R", "O", "I", "S"],
            ["N", "E", "U", "F", "U", "N", "E", "S", "E", "P", "T"],
            ["H", "U", "I", "T", "S", "I", "X", "C", "I", "N", "Q"],
            ["M", "I", "D", "I", "X", "M", "I", "N", "U", "I", "T"],
            ["O", "N", "Z", "E", "R", "H", "E", "U", "R", "E", "S"],
            ["M", "O", "I", "N", "S", "O", "L", "E", "D", "I", "X"],
            ["E", "T", "R", "Q", "U", "A", "R", "T", "P", "M", "D"],
            ["V", "I", "N", "G", "T", "-", "C", "I", "N", "Q", "U"],
            ["E", "T", "S", "D", "E", "M", "I", "E", "P", "A", "M"]
        ]
        self.labellettres = [
            ["I", "L", "N", "E", "S", "T", "O", "D", "E", "U", "X"],
            ["Q", "U", "A", "T", "R", "E", "T", "R", "O", "I", "S"],
            ["N", "E", "U", "F", "U", "N", "E", "S", "E", "P", "T"],
            ["H", "U", "I", "T", "S", "I", "X", "C", "I", "N", "Q"],
            ["M", "I", "D", "I", "X", "M", "I", "N", "U", "I", "T"],
            ["O", "N", "Z", "E", "R", "H", "E", "U", "R", "E", "S"],
            ["M", "O", "I", "N", "S", "O", "L", "E", "D", "I", "X"],
            ["E", "T", "R", "Q", "U", "A", "R", "T", "P", "M", "D"],
            ["V", "I", "N", "G", "T", "-", "C", "I", "N", "Q", "U"],
            ["E", "T", "S", "D", "E", "M", "I", "E", "P", "A", "M"]
        ]
        self.counter = [1, 2, 3, 4]

        self.main = Frame(self.root, height=2, bd=0, padx=0.5)
        self.main.place(relx=0.5, rely=0.48, anchor=CENTER)
        for i in range(10):
            for j in range(11):
                self.labellettres[i][j] = Label(self.main, text=self.lettres[i][j], font=fixedfont(24), fg="#3e3e3e",
                                                bg="black")
                self.labellettres[i][j].grid(row=i + 1, column=j + 1, padx=50, pady=25)

        self.counter1 = Frame(self.root)
        self.counter1.place(relx=0.03, rely=0.02, anchor=NW)
        self.counter[0] = Label(self.counter1, text="●", font=fixedfont(30), fg="#3e3e3e", bg="black")
        self.counter[0].grid(row=1, column=1)

        self.counter2 = Frame(self.root)
        self.counter2.place(relx=0.96, rely=0.02, anchor=NW)
        self.counter[1] = Label(self.counter2, text="●", font=fixedfont(30), fg="#3e3e3e", bg="black")
        self.counter[1].grid(row=1, column=1)

        self.counter3 = Frame(self.root)
        self.counter3.place(relx=0.96, rely=0.90, anchor=NW)
        self.counter[2] = Label(self.counter3, text="●", font=fixedfont(30), fg="#3e3e3e", bg="black")
        self.counter[2].grid(row=1, column=1)

        self.counter4 = Frame(self.root)
        self.counter4.place(relx=0.03, rely=0.90, anchor=NW)
        self.counter[3] = Label(self.counter4, text="●", font=fixedfont(30), fg="#3e3e3e", bg="black")
        self.counter[3].grid(row=1, column=1)

        self.main.configure(bg="#000000", borderwidth=10)

        # ttk styles
        self.style = ttk.Style()

        self.update()

    def destroy(self):
        self.root.destroy()

    def displayletter(self, i, j, hour, minute):
        if self.mode == "HOUR":
            if (i == 0 and j == 0) \
                    or (i == 0 and j == 1) \
                    or (i == 0 and j == 3) \
                    or (i == 0 and j == 4) \
                    or (i == 0 and j == 5) \
                    or (i == 0 and j == 7 and (
                    ((hour == 1 or hour == 13) and minute > 30) or ((hour == 2 or hour == 14) and minute < 35))) \
                    or (i == 0 and j == 8 and (
                    ((hour == 1 or hour == 13) and minute > 30) or ((hour == 2 or hour == 14) and minute < 35))) \
                    or (i == 0 and j == 9 and (
                    ((hour == 1 or hour == 13) and minute > 30) or ((hour == 2 or hour == 14) and minute < 35))) \
                    or (i == 0 and j == 10 and (
                    ((hour == 1 or hour == 13) and minute > 30) or ((hour == 2 or hour == 14) and minute < 35))) \
                    or (i == 1 and j == 0 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 1 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 2 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 3 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 4 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 5 and (
                    ((hour == 3 or hour == 15) and minute > 30) or ((hour == 4 or hour == 16) and minute < 35))) \
                    or (i == 1 and j == 6 and (
                    ((hour == 2 or hour == 14) and minute > 30) or ((hour == 3 or hour == 15) and minute < 35))) \
                    or (i == 1 and j == 7 and (
                    ((hour == 2 or hour == 14) and minute > 30) or ((hour == 3 or hour == 15) and minute < 35))) \
                    or (i == 1 and j == 8 and (
                    ((hour == 2 or hour == 14) and minute > 30) or ((hour == 3 or hour == 15) and minute < 35))) \
                    or (i == 1 and j == 9 and (
                    ((hour == 2 or hour == 14) and minute > 30) or ((hour == 3 or hour == 15) and minute < 35))) \
                    or (i == 1 and j == 10 and (
                    ((hour == 2 or hour == 14) and minute > 30) or ((hour == 3 or hour == 15) and minute < 35))) \
                    or (i == 2 and j == 0 and (
                    ((hour == 8 or hour == 20) and minute > 30) or ((hour == 9 or hour == 21) and minute < 35))) \
                    or (i == 2 and j == 1 and (
                    ((hour == 8 or hour == 20) and minute > 30) or ((hour == 9 or hour == 21) and minute < 35))) \
                    or (i == 2 and j == 2 and (
                    ((hour == 8 or hour == 20) and minute > 30) or ((hour == 9 or hour == 21) and minute < 35))) \
                    or (i == 2 and j == 3 and (
                    ((hour == 8 or hour == 20) and minute > 30) or ((hour == 9 or hour == 21) and minute < 35))) \
                    or (i == 2 and j == 4 and (
                    ((hour == 12) and minute > 30) or ((hour == 1 or hour == 13) and minute < 35))) \
                    or (i == 2 and j == 5 and (
                    ((hour == 12) and minute > 30) or ((hour == 1 or hour == 13) and minute < 35))) \
                    or (i == 2 and j == 6 and (
                    ((hour == 12) and minute > 30) or ((hour == 1 or hour == 13) and minute < 35))) \
                    or (i == 2 and j == 7 and (
                    ((hour == 6 or hour == 18) and minute > 30) or ((hour == 7 or hour == 19) and minute < 35))) \
                    or (i == 2 and j == 8 and (
                    ((hour == 6 or hour == 18) and minute > 30) or ((hour == 7 or hour == 19) and minute < 35))) \
                    or (i == 2 and j == 9 and (
                    ((hour == 6 or hour == 18) and minute > 30) or ((hour == 7 or hour == 19) and minute < 35))) \
                    or (i == 2 and j == 10 and (
                    ((hour == 6 or hour == 18) and minute > 30) or ((hour == 7 or hour == 19) and minute < 35))) \
                    or (i == 3 and j == 0 and (
                    ((hour == 7 or hour == 19) and minute > 30) or ((hour == 8 or hour == 20) and minute < 35))) \
                    or (i == 3 and j == 1 and (
                    ((hour == 7 or hour == 19) and minute > 30) or ((hour == 8 or hour == 20) and minute < 35))) \
                    or (i == 3 and j == 2 and (
                    ((hour == 7 or hour == 19) and minute > 30) or ((hour == 8 or hour == 20) and minute < 35))) \
                    or (i == 3 and j == 3 and (
                    ((hour == 7 or hour == 19) and minute > 30) or ((hour == 8 or hour == 20) and minute < 35))) \
                    or (i == 3 and j == 4 and (
                    ((hour == 5 or hour == 17) and minute > 30) or ((hour == 6 or hour == 18) and minute < 35))) \
                    or (i == 3 and j == 5 and (
                    ((hour == 5 or hour == 17) and minute > 30) or ((hour == 6 or hour == 18) and minute < 35))) \
                    or (i == 3 and j == 6 and (
                    ((hour == 5 or hour == 17) and minute > 30) or ((hour == 6 or hour == 18) and minute < 35))) \
                    or (i == 3 and j == 7 and (
                    ((hour == 4 or hour == 16) and minute > 30) or ((hour == 5 or hour == 17) and minute < 35))) \
                    or (i == 3 and j == 8 and (
                    ((hour == 4 or hour == 16) and minute > 30) or ((hour == 5 or hour == 17) and minute < 35))) \
                    or (i == 3 and j == 9 and (
                    ((hour == 4 or hour == 16) and minute > 30) or ((hour == 5 or hour == 17) and minute < 35))) \
                    or (i == 3 and j == 10 and (
                    ((hour == 4 or hour == 16) and minute > 30) or ((hour == 5 or hour == 17) and minute < 35))) \
                    or (i == 4 and j == 0 and (
                    ((hour == 11) and minute > 30) or ((hour == 12) and minute < 35))) \
                    or (i == 4 and j == 1 and (
                    ((hour == 11) and minute > 30) or ((hour == 12) and minute < 35))) \
                    or (i == 4 and j == 2 and (
                    ((hour == 11) and minute > 30) or ((hour == 12) and minute < 35))) \
                    or (i == 4 and j == 2 and (
                    ((hour == 9 or hour == 21) and minute > 30) or ((hour == 10 or hour == 22) and minute < 35))) \
                    or (i == 4 and j == 3 and (
                    ((hour == 11) and minute > 30) or ((hour == 12) and minute < 35))) \
                    or (i == 4 and j == 2 and (
                    ((hour == 9 or hour == 21) and minute > 30) or ((hour == 10 or hour == 22) and minute < 35))) \
                    or (i == 4 and j == 2 and (
                    ((hour == 9 or hour == 21) and minute > 30) or ((hour == 10 or hour == 22) and minute < 35))) \
                    or (i == 4 and j == 5 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 4 and j == 6 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 4 and j == 7 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 4 and j == 8 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 4 and j == 9 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 4 and j == 10 and (
                    ((hour == 23) and minute > 30) or ((hour == 00) and minute < 35))) \
                    or (i == 5 and j == 0 and (
                    ((hour == 10 or hour == 22) and minute > 30) or ((hour == 11 or hour == 23) and minute < 35))) \
                    or (i == 5 and j == 1 and (
                    ((hour == 10 or hour == 22) and minute > 30) or ((hour == 11 or hour == 23) and minute < 35))) \
                    or (i == 5 and j == 2 and (
                    ((hour == 10 or hour == 22) and minute > 30) or ((hour == 11 or hour == 23) and minute < 35))) \
                    or (i == 5 and j == 3 and (
                    ((hour == 10 or hour == 22) and minute > 30) or ((hour == 11 or hour == 23) and minute < 35))) \
                    or (i == 5 and j == 5) \
                    or (i == 5 and j == 6) \
                    or (i == 5 and j == 7) \
                    or (i == 5 and j == 8) \
                    or (i == 5 and j == 9) \
                    or (i == 6 and j == 0 and (minute >= 35)) \
                    or (i == 6 and j == 1 and (minute >= 35)) \
                    or (i == 6 and j == 2 and (minute >= 35)) \
                    or (i == 6 and j == 3 and (minute >= 35)) \
                    or (i == 6 and j == 4 and (minute >= 35)) \
                    or (i == 6 and j == 6 and (minute >= 45) and (minute <= 49)) \
                    or (i == 6 and j == 7 and (minute >= 45) and (minute <= 49)) \
                    or (i == 6 and j == 8 and (minute >= 50) and (minute <= 54)) \
                    or (i == 6 and j == 9 and (minute >= 50) and (minute <= 54)) \
                    or (i == 6 and j == 10 and (minute >= 50) and (minute <= 54)) \
                    or (i == 7 and j == 3 and (minute >= 45) and (minute <= 49)) \
                    or (i == 7 and j == 4 and (minute >= 45) and (minute <= 49)) \
                    or (i == 7 and j == 5 and (minute >= 45) and (minute <= 49)) \
                    or (i == 7 and j == 6 and (minute >= 45) and (minute <= 49)) \
                    or (i == 7 and j == 7 and (minute >= 45) and (minute <= 49)) \
                    or (i == 8 and j == 0 and (minute >= 40) and (minute <= 44)) \
                    or (i == 8 and j == 1 and (minute >= 40) and (minute <= 44)) \
                    or (i == 8 and j == 2 and (minute >= 40) and (minute <= 44)) \
                    or (i == 8 and j == 3 and (minute >= 40) and (minute <= 44)) \
                    or (i == 8 and j == 4 and (minute >= 40) and (minute <= 44)) \
                    or (i == 8 and j == 0 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 1 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 2 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 3 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 4 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 5 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 6 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 7 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 8 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 9 and (minute >= 35) and (minute <= 39)) \
                    or (i == 8 and j == 6 and (minute >= 55) and (minute <= 59)) \
                    or (i == 8 and j == 7 and (minute >= 55) and (minute <= 59)) \
                    or (i == 8 and j == 8 and (minute >= 55) and (minute <= 59)) \
                    or (i == 8 and j == 9 and (minute >= 55) and (minute <= 59)) \
                    or (i == 9 and j == 0 and (minute >= 30) and (minute <= 34)) \
                    or (i == 9 and j == 1 and (minute >= 30) and (minute <= 34)) \
                    or (i == 9 and j == 3 and (minute >= 30) and (minute <= 34)) \
                    or (i == 9 and j == 4 and (minute >= 30) and (minute <= 34)) \
                    or (i == 9 and j == 5 and (minute >= 30) and (minute <= 34)) \
                    or (i == 9 and j == 6 and (minute >= 30) and (minute <= 34)) \
                    or (i == 6 and j == 6 and (minute >= 15) and (minute <= 19)) \
                    or (i == 6 and j == 7 and (minute >= 15) and (minute <= 19)) \
                    or (i == 6 and j == 8 and (minute >= 10) and (minute <= 14)) \
                    or (i == 6 and j == 9 and (minute >= 10) and (minute <= 14)) \
                    or (i == 6 and j == 10 and (minute >= 10) and (minute <= 14)) \
                    or (i == 7 and j == 3 and (minute >= 15) and (minute <= 19)) \
                    or (i == 7 and j == 4 and (minute >= 15) and (minute <= 19)) \
                    or (i == 7 and j == 5 and (minute >= 15) and (minute <= 19)) \
                    or (i == 7 and j == 6 and (minute >= 15) and (minute <= 19)) \
                    or (i == 7 and j == 7 and (minute >= 15) and (minute <= 19)) \
                    or (i == 8 and j == 0 and (minute >= 20) and (minute <= 24)) \
                    or (i == 8 and j == 1 and (minute >= 20) and (minute <= 24)) \
                    or (i == 8 and j == 2 and (minute >= 20) and (minute <= 24)) \
                    or (i == 8 and j == 3 and (minute >= 20) and (minute <= 24)) \
                    or (i == 8 and j == 4 and (minute >= 20) and (minute <= 24)) \
                    or (i == 8 and j == 0 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 1 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 2 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 3 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 4 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 5 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 6 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 7 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 8 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 9 and (minute >= 25) and (minute <= 29)) \
                    or (i == 8 and j == 6 and (minute >= 5) and (minute <= 9)) \
                    or (i == 8 and j == 7 and (minute >= 5) and (minute <= 9)) \
                    or (i == 8 and j == 8 and (minute >= 5) and (minute <= 9)) \
                    or (i == 8 and j == 9 and (minute >= 5) and (minute <= 9)):
                    self.labellettres[i][j].configure(fg=self.onColor, font=fixedfontbold(24))
            else:
                self.labellettres[i][j].configure(fg=self.offColor, font=fixedfont(24))

    def displaycounter(self, i, hour, minute):
        if self.mode == "HOUR":
            if i == 0 and minute % 5 >= 1:
                self.counter[0].configure(fg=self.onColor, font=fixedfontbold(30))
            elif i == 0:
                self.counter[0].configure(fg=self.offColor, font=fixedfontbold(30))
            if i == 1 and minute % 5 >= 2:
                self.counter[1].configure(fg=self.onColor, font=fixedfontbold(30))
            elif i == 1:
                self.counter[1].configure(fg=self.offColor, font=fixedfontbold(30))
            if i == 2 and minute % 5 >= 3:
                self.counter[2].configure(fg=self.onColor, font=fixedfontbold(30))
            elif i == 2:
                self.counter[2].configure(fg=self.offColor, font=fixedfontbold(30))
            if i == 3 and minute % 5 >= 4:
                self.counter[3].configure(fg=self.onColor, font=fixedfontbold(30))
            elif i == 3:
                self.counter[3].configure(fg=self.offColor, font=fixedfontbold(30))

    def update(self):
        hour = int(t.strftime("%H", t.localtime()))
        minute = int(t.strftime("%M", t.localtime()))
        sec = int(t.strftime("%S", t.localtime()))
        for i in range(10):
            for j in range(11):
                self.displayletter(i, j, hour, minute)
        for i in range(3):
            self.displaycounter(i, hour, minute)

        self.root.after(100, self.update)


def main():
    app = App()
    app.root.mainloop()


if __name__ == '__main__':
    main()
