import numpy as np
from PIL import Image, ImageTk, ImageColor
from io import BytesIO
from tkinter import ttk, Canvas, NW
import os


def white_to_transparency(img):
        x = np.asarray(img.convert('RGBA')).copy()

        x[:, :, 3] = (255 * (x[:, :, :3] != 255).any(axis=2)).astype(np.uint8)


        dosave= Image.fromarray(x)
        dosave.save("./resources/img3.png", "PNG")
        return Image.fromarray(x)

class Workspace:
    def __init__(self, robotImagePath, envImagePath, root):
        
        self.root = root
        self.envImage = Image.open(envImagePath)
        self.envArray = np.array(self.envImage)
        self.envPhoto = ImageTk.PhotoImage(self.envImage)

        self.robotImage = Image.open(robotImagePath)


        #https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
        white_to_transparency(self.robotImage)

        

        self.robotArray = np.array(self.robotImage)
        self.robotPhoto = ImageTk.PhotoImage(self.robotImage)

        self.label = ttk.Label(root, image = self.envPhoto)

        self.currentPos = (0,0)

    def drawRobot (self,x,y):
        self.currentPos=(x-round(0.5*self.robotImage.width),y-round(0.5*self.robotImage.width))
        self.imageToDraw = self.envImage.copy()
        self.imageToDraw.paste(self.robotImage.copy(),(self.currentPos[0],self.currentPos[1]))
        self.photoToDraw = ImageTk.PhotoImage(self.imageToDraw)

        self.label.configure(image=self.photoToDraw)
        self.label.image = self.photoToDraw

        self.label.pack(side = "bottom", fill = "both", expand = "yes")

    def setCurrentPosAsInit(self):
        pass

    def setCurrentPosAsGoal(self):
        pass

    
    
