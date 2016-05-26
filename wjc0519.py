#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self, text='这是个内容')
        # self.helloLabel.pack()
        # self.quitButton = Button(self, text='Quit', command=self.quit)
        # self.quitButton.pack()
        self.nameInpur = Entry(self)
        self.nameInpur.pack()
        self.alertButton = Button(self, text='Hell', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInpur.get() or 'world'
        messagebox.showinfo('Message', 'Hello %s' % name)



app = Application()

app.master.title('这个是标题')

app.mainloop()