

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