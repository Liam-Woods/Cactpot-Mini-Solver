# -*- coding: utf-8 -*-

"""A simple GUI for calculating the reward from the Cactpot mini-game."""
import sys
import os
import itertools
from tkinter import Tk, Label, Button, Entry, Frame


def resource_path(relative_path):
    """Relative resource path func to allow pyinstaller to covert to exe."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def list_diff(list1, list2):
    """Difference between two lists."""
    set_difference = set(list1) - set(list2)
    list_difference = list(set_difference)
    return list_difference


class MyApp:
    """Class used to create GUI in tkinter."""

    def __init__(self, parent):
        """Initialise the GUI."""
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.entry = []
        self.mainlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.mainliststring = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.prizes = {6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252,
                       12: 108, 13: 72, 14: 54, 15: 180, 16: 72, 17: 180,
                       18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800,
                       24: 3600}
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.labels = []
        self.resultLab = []

        for indx, let in enumerate(self.letters):
            self.labels.append(Label(self.myContainer1, text=let, width=6))
            self.resultLab.append(Label(self.myContainer1, text=let, width=6))
            self.resultLab[indx].grid(row=indx+7, column=0, padx=4, pady=4)
            if indx > 4:
                self.labels[indx].grid(row=indx-4, column=0, padx=4, pady=4)
            else:
                self.labels[indx].grid(row=0, column=indx, padx=4, pady=4)

        self.labelmin = Label(self.myContainer1, text="min", width=6)
        self.labelmin.grid(row=6, column=1, padx=4, pady=4)
        self.labelavg = Label(self.myContainer1, text="mean", width=6)
        self.labelavg.grid(row=6, column=2, padx=4, pady=4)
        self.labelmax = Label(self.myContainer1, text="max", width=6)
        self.labelmax.grid(row=6, column=3, padx=4, pady=4)

        for i in range(1, 4):
            for j in range(1, 4):
                self.temp = Entry(self.myContainer1, width=6)
                self.temp.grid(row=i, column=j, padx=4, pady=4)
                self.entry.append(self.temp)

        self.textStatus = Label(self.myContainer1,
                                text="Submission Status:", width=16)
        self.textStatus.grid(row=4, column=0, columnspan=2, padx=4, pady=4)

        self.button1 = Button(self.myContainer1, text="Submit",
                              width=6, command=self.submit)
        self.button1.grid(row=2, column=4, padx=4, pady=4)

        self.button2 = Button(self.myContainer1, text="Clear",
                              width=6, command=self.clear)
        self.button2.grid(row=2, column=5, padx=4, pady=4)

        self.labelStatus = Label(self.myContainer1)
        self.labelStatus.grid(row=4, column=2, columnspan=3, sticky="w")

    def submit(self):
        """Take each line from the grid and find min, max and mean for each."""
        self.submitlist = []
        self.cellgroup = []
        self.possibleResult = []
        self.result = []
        self.minlist = []
        self.meanlist = []
        self.maxlist = []
        self.minentry = []
        self.meanentry = []
        self.maxentry = []
        self.cells = [0]*9

        for i in range(len(self.entry)):
            self.cell = self.entry[i].get()
            if self.cell != "":
                if self.cell not in self.mainliststring:
                    self.labelStatus["text"] = "Please enter integers 1-9"
                    return
                self.submitlist.append(int(self.cell))
                self.cells[i] = int(self.cell)

        if len(self.submitlist) == len(set(self.submitlist)):
            self.labelStatus["text"] = "Success"
        else:
            self.labelStatus["text"] = "Duplicate entries"
            return

        self.notlist = list_diff(self.mainlist, self.submitlist)

        self.cellgroup.append([self.cells[0], self.cells[4], self.cells[8]])
        self.cellgroup.append([self.cells[0], self.cells[3], self.cells[6]])
        self.cellgroup.append([self.cells[1], self.cells[4], self.cells[7]])
        self.cellgroup.append([self.cells[2], self.cells[5], self.cells[8]])
        self.cellgroup.append([self.cells[2], self.cells[4], self.cells[6]])
        self.cellgroup.append([self.cells[0], self.cells[1], self.cells[2]])
        self.cellgroup.append([self.cells[3], self.cells[4], self.cells[5]])
        self.cellgroup.append([self.cells[6], self.cells[7], self.cells[8]])

        for i in range(len(self.cellgroup)):
            self.suma = sum(self.cellgroup[i])
            self.li = list(itertools.combinations(self.notlist,
                                                  self.cellgroup[i].count(0)))
            self.sumb = [sum(tup) for tup in self.li]
            self.possibleResult.append([x + self.suma for x in self.sumb])
            self.temp2 = []
            for j in range(len(self.possibleResult[i])):
                self.temp2.append(self.prizes[self.possibleResult[i][j]])
            self.result.append(self.temp2)
            self.minlist.append(min(self.result[i]))
            self.meanlist.append(round(sum(self.result[i])
                                 / len(self.result[i]), 2))
            self.maxlist.append(max(self.result[i]))

        for i in range(len(self.minlist)):
            self.temp3 = Label(self.myContainer1,
                               text=str(self.minlist[i]), width=6)
            self.temp3.grid(row=7+i, column=1, padx=4, pady=4)
            self.minentry.append(self.temp3)

            self.temp3 = Label(self.myContainer1,
                               text=str(self.meanlist[i]), width=6)
            self.temp3.grid(row=7+i, column=2, padx=4, pady=4)
            self.meanentry.append(self.temp3)

            self.temp3 = Label(self.myContainer1,
                               text=str(self.maxlist[i]), width=6)
            self.temp3.grid(row=7+i, column=3, padx=4, pady=4)
            self.maxentry.append(self.temp3)

    def clear(self):
        """Button function to remove text from entry boxes and labels."""
        self.labelStatus["text"] = ""
        for i in range(len(self.entry)):
            self.entry[i].delete(0, "end")
            self.entry[i].insert(0, "")
        for i in range(len(self.minentry)):
            self.minentry[i]["text"] = ""
            self.meanentry[i]["text"] = ""
            self.maxentry[i]["text"] = ""


if __name__ == "__main__":
    root = Tk()
    root.title("Cactpot Mini Solver")
    root.iconbitmap(resource_path('cactuar.ico'))
    root.lift()
    myapp = MyApp(root)
    root.mainloop()
