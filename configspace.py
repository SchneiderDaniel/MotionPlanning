from tkinter import ttk, Canvas, BOTH, CENTER, RAISED

class Configspace:
    def __init__(self,root):
        self.initConfig = -1, -1
        self.goalConfig = -1, -1
        self.solutionPath = []
        self.isInitialize = False
        self.root = root
        self.xExt = 0
        self.yExt = 0
        self.canvas = Canvas(self.root)
        self.theOffset = 20
        
        # canvas_width = 80
        # canvas_height = 40
        # w = Canvas(root, width=canvas_width,height=canvas_height)


    def setDimensions(self,x,y):
      print ('Set dimensions to: ' + str(x) + '/'+ str(y))
      
      self.xExt=x
      self.yExt=y
      off = self.theOffset
      self.canvas.config(bd=0, height=y+2*off, width=x+2*off, offset='10,10')
      
      self.canvas.create_line(off, 0+off, 0+off, y+off)
      self.canvas.create_line(off, 0+off, x+off, 0+off)
      self.canvas.create_line(x+off, y+off, x+off, 0+off)
      self.canvas.create_line(x+off, y+off, 0+off, y+off)

      self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
      #       # self.canvas.pack(fill=BOTH, expand=1)


    def setIntialSolutionPath(self):
        resolution = max(abs(
            self.initConfig[0]-self.goalConfig[0]), abs(self.goalConfig[1]-self.goalConfig[1]))
        print(' Initial config: ' +
              str(self.initConfig[0]) + '/' + str(self.initConfig[1]))
        print(' Goal config: ' +
              str(self.goalConfig[0]) + '/' + str(self.goalConfig[1]))
        print('resolution: ' + str(resolution))

        self.solutionPath.append(self.initConfig)
        for i in range(1,resolution):
            deltaX = round(i*float(self.goalConfig[0]-self.initConfig[0])/float(resolution))
            deltaY = round(i*float(self.goalConfig[1]-self.initConfig[1])/float(resolution))
            newX = self.initConfig[0] + deltaX
            newY = self.initConfig[1] + deltaY
            self.solutionPath.append((newX, newY))
        self.solutionPath.append(self.goalConfig)

        # for s in self.solutionPath:
        #     print(s)

