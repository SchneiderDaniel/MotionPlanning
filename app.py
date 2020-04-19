import tkinter 
from tkinter import ttk, RIGHT
from workspace import Workspace 
from configspace import Configspace
from controller import  Controller
from PIL import ImageTk, Image
import os


def demo():
    root = tkinter.Tk()
    root.title("Motion Planning")
    universal_height = 1000

    nb = ttk.Notebook(root)
    

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb, width= 1080,height = universal_height)
    # second page
    page2 = ttk.Frame(nb,width = 1080,height = universal_height)

    nb.add(page1, text='Workspace')
    nb.add(page2, text='Configspace')
    nb.grid(column=2)

   
    workspace = Workspace("./resources/robot_BW_small.bmp", "./resources/Room_BW_small.bmp", page1)
    configspace = Configspace()
    controller = Controller(workspace,configspace)
    

    workspace.drawAll(workspace.currentPos[0],workspace.currentPos[1])
    def callback(event):
        print ("clicked at", event.x, event.y)
        controller.draw(event.x, event.y)
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
