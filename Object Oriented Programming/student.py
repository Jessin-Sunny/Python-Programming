class Student(object):
    def __init__(self, name, num):
        self._name = name
        self._scores = []
        for i in range(num):
            self._scores.append(0)

    def getName(self):
        return self._name

    def getScore(self, i):
        return self._scores[i]

    def setScore(self, i, score):
        self._scores[i] = score

    def getAvg(self):
        return sum(self._scores)/len(self._scores)

    def __str__(self):
        return "Name: " + self._name + "\nScores :" + " ".join(map(str, self._scores)) + "\n"
