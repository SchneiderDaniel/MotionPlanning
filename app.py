import tkinter 
from tkinter import ttk, RIGHT, Canvas,BOTH
from workspace import Workspace 
from configspace import Configspace
from controller import  Controller
from PIL import ImageTk, Image
import os
from utils import setBackgroundColor


def demo():
    root = tkinter.Tk()
    root.title("Motion Planning")
    universal_height = 1000

    nb = ttk.Notebook(root)
    page1 = ttk.Frame(nb, width= 1080,height = universal_height)
    page2 = ttk.Frame(nb,width = 1080,height = universal_height)

    nb.add(page1, text='Workspace')
    nb.add(page2, text='Configspace')
    nb.grid(column=0)

    # collisionCanvas= Canvas(page1, height = 50)
    # collisionCanvas. create_rectangle(0, 0, 50, 50,
    #         outline="#f50", fill="#f50")
    # collisionCanvas.pack(side=tkinter.RIGHT)

   
    workspace = Workspace("./resources/robot_BW_small.bmp", "./resources/Room_BW_small.bmp", page1)
    configspace = Configspace()
    controller = Controller(workspace,configspace)
    

    workspace.drawAll(workspace.currentPos[0],workspace.currentPos[1])
    def callback(event):
        print ("clicked at", event.x, event.y)
        controller.draw(event.x, event.y)
      
        if controller.isInCollision(): setBackgroundColor(page1,"red")
        else: setBackgroundColor(page1,"green")
        # style = ttk.Style()     # Create style
        # style.configure("Blue.TFrame", background="blue") # Set bg color
        # page1.config(style='Blue.TFrame')    # Apply style to widget

        print(workspace.currentPos)
    
    workspace.label.bind("<Button-1>", callback)

    def set_init():
        controller.setCurrentPosAsInit()
    setInitButton = ttk.Button(page1, text = 'Set Init',command = set_init)
    setInitButton.pack(side=tkinter.RIGHT)

    def set_goal():
        controller.setCurrentPosAsGoal()
    setGoalButton = ttk.Button(page1, text = 'Set Goal',command = set_goal)
    setGoalButton.pack(side=tkinter.RIGHT)


    root.mainloop()


if __name__ == "__main__":
    demo()
