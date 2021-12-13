from tkinter import *
import pyautogui
from PIL import ImageTk, Image

pyautogui.screenshot('s.png')

root = Tk()
root.attributes('-fullscreen', True)
img = ImageTk.PhotoImage(Image.open("s.png"))
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.config(cursor="none")

root.mainloop()