class Point:

    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
