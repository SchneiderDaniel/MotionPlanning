

class Configspace:
    def __init__(self):
        self.initConfig = -1, -1
        self.goalConfig = -1, -1
        self.solutionPath = []
        self.isInitialize = False

    def setIntialSolutionPath(self):
        resolution = max(abs(
            self.initConfig[0]-self.goalConfig[0]), abs(self.goalConfig[1]-self.goalConfig[1]))
        # print(' Initial config: ' +
        #       str(self.initConfig[0]) + '/' + str(self.initConfig[1]))
        # print(' Goal config: ' +
        #       str(self.goalConfig[0]) + '/' + str(self.goalConfig[1]))
        # print('resolution: ' + str(resolution))

        self.solutionPath.append(self.initConfig)
        for i in range(1,resolution):
            deltaX = round((self.goalConfig[0]-self.initConfig[0])/resolution)
            deltaY = round((self.goalConfig[1]-self.initConfig[1])/resolution)
            newX = self.initConfig[0] + i*deltaX
            newY = self.initConfig[1] + i*deltaY
            self.solutionPath.append((newX, newY))
        self.solutionPath.append(self.goalConfig)

        # for s in self.solutionPath:
        #     print(s)

