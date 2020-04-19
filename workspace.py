import numpy as np
from PIL import Image, ImageTk, ImageColor
from io import BytesIO
from tkinter import ttk, Canvas, NW
import os
from configspace import Configspace


class Workspace:
    def __init__(self, robotImagePath, envImagePath, root):
        
        self.root = root
        self.envImage = Image.open(envImagePath)
        self.envArray = np.array(self.envImage)
        self.envPhoto = ImageTk.PhotoImage(self.envImage)

        self.robotImage = Image.open(robotImagePath)

        #https://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent
        # white_to_transparency(self.robotImage)

        self.robotArray = np.array(self.robotImage)
        self.robotPhoto = ImageTk.PhotoImage(self.robotImage)

        self.label = ttk.Label(root, image = self.envPhoto)

        self.currentPos = (0,0)

    def drawRobot (self,x,y):
        self.currentPos=x,y
        self.imageToDraw = self.envImage.copy()
        self.imageToDraw.paste(self.robotImage.copy(),(self.currentPos[0],self.currentPos[1]))
        self.photoToDraw = ImageTk.PhotoImage(self.imageToDraw)

        self.label.configure(image=self.photoToDraw)
        self.label.image = self.photoToDraw

        self.label.pack(side = "bottom", fill = "both", expand = "yes")

    

    
    
