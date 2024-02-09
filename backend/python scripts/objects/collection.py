from objects.exerciseObjects import Exercise
from objects.exerciseObjects import NotePattern
from objects.exerciseObjects import RhythmPattern
from notePatternGenerator import stepwiseScaleNotePatterns
from rhythmPatternGenerator import quarterNoteRhythms
from objects.practiceSet import PracticeSet
from objects.player import Player

class Collection:
    def __init__(self, name, notePatterns=None, rhythmPatterns=None, key="g", mode="major"):
        self.__name = name
<<<<<<< HEAD
        self.__key = key
        self.__mode = mode
        if rhythmPatterns is None:
            rhythmPatterns = []
        else :
            self.__rhythmPatterns = rhythmPatterns
        if notePatterns is None:
            notePatterns = []
        else:
            self.__notePatterns = notePatterns
=======
        self.__notePatterns = []
>>>>>>> parent of 64bea5c3 (great flow)

    def __str__(self):
        return self.__name

    def __iter__(self):
        return iter(self.__notePatterns)

<<<<<<< HEAD
    @property
    def getTitle(self):
        return self.title
=======
    def serialize(self):
        notePatterns = self.serializeNotePatterns()
        return {"name": self.__name, "notePatterns": notePatterns}

    # def serializeNotePatterns(self):
    #     serializedNotePatterns = []
    #     for p in self.__notePatterns:
    #         serializedNotePatterns.append(p.serialize())
    #     return serializedNotePatterns
>>>>>>> parent of 64bea5c3 (great flow)

    @property
    def getNotePatterns(self):
        return self.__notePatterns

    def addNotePattern(self, pattern):
        self.__notePatterns.append(pattern)

    @property
    def getRhythmPatterns(self):
        return self.__notePatterns

    def addRhythmPattern(self, pattern):
        self.__notePatterns.append(pattern)

    def getSampleExercises(self, player):
        pass

