__all__ = []

class Matrix:
    """
    Implementation of matrices.
    """
    def __init__(self):
        super().__init__()
        self.matrix = [[1, 2, 3], [4, 5, 6]]
        self.used = []
        self.shape = self.get_shape()
        self.__all__ = []
        self.__all__.extend("Matrix")
    
    def get_shape(self):
        # TODO(aaronhma): Stabilize this:
        self.__all__.extend("MatrixShape")
        shape = set()
        shape.add(len(self.matrix))
        shape.add(len(self.matrix[0]))
        return shape
    
matrix = Matrix()
__all__.extend(matrix.__all__)