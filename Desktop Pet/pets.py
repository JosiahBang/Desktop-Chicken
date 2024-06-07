from random import randint, random
from math import floor
from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk

idle = Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0001.png")
walk = [
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0001.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0002.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0003.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0004.png")
]
fall = [
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0005.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0006.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0007.png"),
]
sleep = [
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0007.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0008.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0009.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0010.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0011.png")
]
wake = [
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0007.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0006.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0005.png")
]
peck = [
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0001.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0012.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0013.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0012.png"),
    Image.open("C:\\Users\\josia\\OneDrive\\Documents\\Python\\Desktop Pet\\sprites\\duck_0001.png")
]

class Duck():
    def __init__(self, x_pos, y_pos, state, frame_time) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = 1
        self.state = state
        self.wait = 50
        self.target_x = x_pos
        self.frame = 0
        self.pecks = 0
        self.time_asleep = 0
        self.current_time = datetime.now().hour
        self.time_awake = 0
        self.frame_time = frame_time

        self.window = Tk()
        img = ImageTk.PhotoImage(idle)
        self.duck = Label(self.window, image = img)
        self.duck.pack()
        self.window.geometry("120x120" + "+" + str(x_pos) + "+" + str(y_pos))
        self.window.wm_attributes("-topmost", True)
        self.window.wm_attributes("-disabled", True)
        self.window.wm_attributes("-transparentcolor", "black")
        self.window.overrideredirect(True)
        self.window.after(self.frame_time, self.update())
        self.window.mainloop()
    
    def update(self):
        self.window.after(self.frame_time, self.update)
        self.current_time = datetime.now().hour
        match self.state:
            case "walk":
                self.pecks = 0
                if abs(self.target_x - self.x_pos) < 10:
                    if randint(0, 2) == 0:
                        self.frame = 0
                        self.state = "peck"
                    else:
                        self.state = "idle"
                    self.wait = randint(200, 350)
                else:
                    self.direction = (self.target_x - self.x_pos) / abs(self.target_x - self.x_pos)
                    self.x_pos += self.direction * 0.8
            case "idle":
                
                self.frame = 0
                if self.wait > 0:
                    self.wait -= 1
                else:
                    if self.time_awake > 15000 and randint(0, 5) == 0:
                        self.frame = 0
                        self.state = "fall"
                    else:
                        if randint(0, 2) == 0:
                            self.frame = 0
                            self.state = "peck"
                        else:
                            self.frame = 0
                            self.state = "walk"
                            self.target_x = randint(20, 1400)
            case "peck":
                pass
                
            case "fall":
                pass
            case "sleep":
                
                if self.time_asleep > 15000:
                    self.frame = 0
                    self.state = "wake"
            case "wake":
                pass
        
        if self.state != "sleep":
            self.time_asleep = 0
            self.time_awake += 1
        else:
            self.time_asleep += 1
            self.time_awake = 0
               
        match self.state:
            case "idle":
        
                if self.direction < 0:
                    img = ImageTk.PhotoImage(idle.transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(idle) 
                self.duck.config(image = img)
                self.duck.image = img
            case "walk":

                if self.direction < 0:
                    img = ImageTk.PhotoImage(walk[int(self.frame / 10) % len(walk)].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(walk[int(self.frame / 10) % len(walk)])
                self.frame += 1
            
            case "peck":
                if self.direction < 0:
                    img = ImageTk.PhotoImage(peck[int(self.frame / 8) % len(peck)].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(peck[int(self.frame / 8) % len(peck)])

                
                if int(self.frame / 8) % len(peck) == len(peck) - 1:
                    if randint(0, 3) == 0 and self.pecks < 2:
                        self.frame = 0
                        self.pecks += 1
                    else:
                        self.frame = 0
                        self.state = "idle"
                        self.wait = randint(80, 150)
                        self.target_x = randint(20, 1400)

                self.frame += 1
            
            case "fall":
                if self.direction < 0:
                    img = ImageTk.PhotoImage(peck[int(self.frame / 20) % len(peck)].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(peck[int(self.frame / 20) % len(peck)])

                if int(self.frame / 20) % len(peck) == len(peck) - 1:
                    self.frame = 0
                    self.state = "sleep"

                self.frame += 1
            
            case "sleep":
                if self.direction < 0:
                    img = ImageTk.PhotoImage(sleep[int(self.frame / 20) % len(sleep)].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(sleep[int(self.frame / 20) % len(sleep)])
                self.frame += 1

            case "wake":
                if self.direction < 0:
                    img = ImageTk.PhotoImage(wake[int(self.frame / 20) % len(wake)].transpose(Image.FLIP_LEFT_RIGHT))
                else:
                    img = ImageTk.PhotoImage(wake[int(self.frame / 20) % len(wake)])

                if int(self.frame / 20) % len(wake) == len(wake) - 1:
                    self.frame = 0
                    self.state = "idle"
                    self.wait = randint(80, 150)

                self.frame += 1

        self.duck.config(image = img)
        self.duck.image = img

        self.x_pos = min(self.x_pos, 1400)
        self.x_pos = max(self.x_pos, 20)

        self.window.geometry('+{}+{}'.format(int(self.x_pos), int(self.y_pos)))
        