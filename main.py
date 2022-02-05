from concurrent.futures import thread
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import imutils
import time


stream = cv2.VideoCapture("C:\\Users\\jaymi\\Desktop\\Python Projects\\Third Umpire Decision Review System\\clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")
 
    frame1 =stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)  
    if flag:
        canvas.create_text(132,26, fill="green", font="Times 20 bold", text="Decision Pending")
    flag = not flag

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("C:\\Users\\jaymi\\Desktop\\Python Projects\\Third Umpire Decision Review System\\decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(2.5)

    if decision == 'out':
        decisionImg ="C:\\Users\\jaymi\\Desktop\\Python Projects\\Third Umpire Decision Review System\\out.png"
    else:
        decisionImg="C:\\Users\\jaymi\\Desktop\\Python Projects\\Third Umpire Decision Review System\\not out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    


def out():
    thread= threading.Thread(target=pending, args=("out",))
    thread.daemon =1
    thread.start()
    print("Player is Out!")

def not_out():
    thread= threading.Thread(target=pending, args=("not out",))
    thread.daemon =1
    thread.start()
    print("Player is Not Out!")



SET_WIDTH = 650
SET_HEIGHT = 370

window = tkinter.Tk()
window.title("Third Umpire Decision Review System")
cv_img = cv2.cvtColor(cv2.imread("C:\\Users\\jaymi\\Desktop\\Python Projects\\Third Umpire Decision Review System\\welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image = photo)
canvas.pack()



btn = tkinter.Button(window, text = "<< Previous (fast)", width=50, command= partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text = "<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text = "Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text = "Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text = "Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text = "Give Not Out", width=50, command=not_out)
btn.pack()


window.mainloop()
