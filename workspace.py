import numpy as np
from PIL import Image, ImageTk, ImageColor
from io import BytesIO
from tkinter import ttk, Canvas, NW


class Workspace:
    def __init__(self, robotImagePath, envImagePath, root):
        
        # http://zetcode.com/tkinter/drawing/

        self.root = root
        self.envImage = Image.open(envImagePath)
        self.envArray = np.array(self.envImage)
        self.envPhoto = ImageTk.PhotoImage(self.envImage)


        self.robotImage = Image.open(robotImagePath)
        self.robotArray = np.array(self.robotImage)
        self.robotPhoto = ImageTk.PhotoImage(self.robotImage)


        self.imageToDraw = self.envImage.copy()
        self.imageToDraw.paste(self.robotImage,(0,0))
        self.photoToDraw = ImageTk.PhotoImage(self.imageToDraw)

        self.label = ttk.Label(root, image = self.photoToDraw)
        self.label.image=self.photoToDraw
        self.label.pack(side = "bottom", fill = "both", expand = "yes")


    def drawRobot (self,x,y):
        self.imageToDraw = self.envImage.copy()
        self.imageToDraw.paste(self.robotImage.copy(),(x,y))
        self.photoToDraw = ImageTk.PhotoImage(self.imageToDraw)

        self.label.destroy()
        self.label = ttk.Label(self.root, image = self.photoToDraw)
        self.label.image=self.photoToDraw
        self.label.pack(side = "bottom", fill = "both", expand = "yes")