from PIL import ImageTk, Image, ImageDraw
import PIL,os
import random
from tkinter import *
from sample import *
width = 150
height = 150
black = (0, 0, 0)

font9 = "-family {Segoe UI Semibold} -size 14 -weight bold "  \
            "-slant italic -underline 0 -overstrike 0"
font10 = "-family {Sitka Text} -size 20 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 17 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"			
font8 = "-family Arial -size 24 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"
def save():
	filename = "image.png"
	image1.resize((84,84))
	image1.save(filename)
	myapp.destroy()

def paint(event):
	x1, y1 = (event.x - 1), (event.y - 1)
	x2, y2 = (event.x + 1), (event.y + 1)
	cv.create_line(x1, y1, x2, y2, fill="white",width=15,capstyle=ROUND, smooth=TRUE, splinesteps=36)
	draw.line([x1, y1, x2, y2],fill="white",width=15)
	
myapp = Tk()
myapp.resizable(0,0)
myapp.title("Created By Chaitany Krishna VB")
Label(text="Digit recognition from 0 to 9",font=font10,background="#3cc3d8",foreground="#ffffff").place(relx=0.11, rely=0.0, height=41, width=374)
Label(text="Not to expect 100 % accuracy",background="#3cc3d8",font=font12,foreground="#ffffff").place(relx=0.15, rely=0.87, height=31, width=324)
image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)
myapp.geometry("453x300+465+298")
myapp.configure(background="#3cc3d8")
cv = Canvas(myapp, width=width, height=height, bg='black')
cv.place(relx=0.33, rely=0.17,relheight=0.5, relwidth=0.33)
cv.bind("<B1-Motion>", paint)
button=Button(text="Predict",command=save,font=font9,foreground="#e02f0b",relief=GROOVE).place(relx=0.33, rely=0.7, height=40, width=150)

myapp.mainloop()


myapp2=Tk()

result=predict2("image.png")
myapp2.configure(background="#7fd80b")
myapp2.title("Prediction")
myapp2.geometry("600x135+430+182")
Label(text="The Number Predicted Is : "+str(result[0]),background="#7fd80b",foreground="#ffffff",font=font8).place(relx=0.1, rely=0.22, height=61, width=514)

myapp2.mainloop()

os.remove("image.png")