# This code by [ref](https://github.com/josephwilk/semanticpy) modify

class MatrixFormatter:
    def __init__(self, matrix):
        self.matrix = matrix

    def pretty_print(self):
        out = ""
        rows,cols = self.matrix.shape
        for row in xrange(0,rows):
            out += "["
            for col in xrange(0,cols):
                out += "%+0.2f "%self.matrix[row][col]
                out += "]\n"
        return out