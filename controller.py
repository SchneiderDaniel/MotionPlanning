

class Controller:
    def __init__(self, workspace, configspace):
        self.workspace = workspace
        self.configspace= configspace

    def setCurrentPosAsInit(self):
        self.configspace.initConfig=(self.workspace.currentPos[0],self.workspace.currentPos[1])
        print('Initial Config set to: '+ str(self.configspace.initConfig))

    def setCurrentPosAsGoal(self):
        self.configspace.goalConfig=(self.workspace.currentPos[0],self.workspace.currentPos[1])
        print('Goal Config set to: '+ str(self.configspace.goalConfig))

    def draw(self,x,y):
        self.workspace.drawAll(x-round(0.5*self.workspace.robotImage.width),y-round(0.5*self.workspace.robotImage.width),
        self.configspace.initConfig[0],self.configspace.initConfig[1], 
        self.configspace.goalConfig[0],self.configspace.goalConfig[1])