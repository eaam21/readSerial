# !/usr/bin/python3
import tkinter as tk
from tkinter import StringVar
from PIL import ImageTk, Image
import os
import time
import serial

#Serial port parameters
serial_speed = 9600
serial_port = '/dev/ttyUSB0'
try:
	ser = serial.Serial(
		serial_port,
		serial_speed,
		timeout = 1
		)
except OSError:
	print("Oops! Check your serial connector.")

class Application(tk.Frame):

	def read_serial(self):
		data = str(ser.readline(), 'utf-8')#Convert to string from byte
		if (data != ""):
			self.read.set(data)
			self.lbl_read.pack()

		self.after(1000, self.read_serial)#Wait 1 second between each measurement

	def create_widgets(self):
		image = ImageTk.PhotoImage(Image.open("pyserial.png"))
		self.lbl_image = tk.Label(self)
		self.lbl_image["image"] = image
		self.lbl_image.image = image #keep a reference!
		self.lbl_image.pack(side='top', fill='both', expand=True)

		self.lbl_title = tk.Label(self)
		self.lbl_title["text"] = "Python reading serial"
		self.lbl_title["font"] = ('Courier', 18)
		self.lbl_title.pack(side='top')

		self.lbl_read = tk.Label(self)
		self.lbl_read["textvariable"] = self.read
		self.lbl_read["font"] = ('Verdana', 12)
		self.lbl_read.pack(side='bottom')

	def __init__(self, master=None):
		super().__init__(master)
		self.read = StringVar()
		self.create_widgets()
		self.pack()
		self.read_serial()

root = tk.Tk()
app = Application(master=root)
app.master.title("Reading serial")
app.master.geometry('400x300')
app.mainloop()
