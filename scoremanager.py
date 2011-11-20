from textmanager import *
import operator

class ScoreManager:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(ScoreManager, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.places = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.textm = TextManager()
        self.places = list()
        self.names = list()
        self.scores = list()
        print("AAA")
        self.loadTheData()

    def loadTheData(self):
        print("AAAAasdadsadwada")
        self.mainDict = self.textm.loadFromFile()
        self.places = self.mainDict['places']
        self.names = self.mainDict['names']
        self.scores = self.mainDict['scores']
        print("AAAAAAA", self.places, self.names, self.scores)

    def returnAllScores(self):
        self.loadTheData()
        return self.places, self.names, self.scores

    def sortNamesAndScores(self):
        foo = dict()
        for i in range(len(self.names)):
            foo[self.names[i]] = self.scores[i]
            print(foo[self.names[i]])

        print(foo)
        sorted_x = sorted(foo.items(), key=operator.itemgetter(1))
        sorted_x.reverse()
        name = list()
        score = list()
        for item in sorted_x:
            name.append(item[0])
            score.append(item[1])
        return name, score

    def addScore(self, name, result):
        self.loadTheData()
        if len(self.names) < 10 and len(self.scores) < 10:
            self.names.append(name)
            self.scores.append(result)
        else:
            self.names[len(self.names) - 1] = name
            self.scores[len(self.scores) - 1] = result

        self.names, self.scores = self.sortNamesAndScores()
        self.places = [x for x in range(1, len(self.names) + 1)]

        self.mainDict = {'places': self.places,
                         'names' : self.names,
                         'scores': self.scores}
        print("AAHAUSGDUAWG", self.mainDict)
        self.textm.writeToFile(self.mainDict)