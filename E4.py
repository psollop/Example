import random

class Die:
    def __init__(self, top_face=None, num_faces=6):
        self._top_face = top_face if top_face is not None else random.randint(1, num_faces)
        self._num_faces = num_faces

    @property
    def top_face(self):
        return self._top_face

    @top_face.setter
    def top_face(self, value):
        self._top_face = value

    @property
    def num_faces(self):
        return self._num_faces

    @num_faces.setter
    def num_faces(self, value):
        self._num_faces = value

    def roll(self):
        self._top_face = random.randint(1, self._num_faces)

    def __str__(self):
        return "Die with {} faces, top face is {}".format(self._num_faces, self._top_face)

# Programa de prueba
dice = [Die(), Die(3), Die(5, 10), Die(2)]

for i in range(5):
    print("Roll", i+1)
    for die in dice:
        die.roll()
        print(die)
