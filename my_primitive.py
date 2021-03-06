import numpy as np
import star2D, star3D, rhombicuboctahedron
from fury import window, utils
from fury.io import save_polydata, load_polydata
from fury.utils import vtk


def primStar(dim):
    if(dim == 2):
        vert = np.array([[-2.0, -3.0, 0.0],
                     [0.0, -2.0, 0.0],
                     [3.0, -3.0, 0.0],
                     [2.0, -1.0, 0.0],
                     [3.0, 1.0, 0.0],
                     [1.0, 1.0, 0.0],
                     [0.0, 3.0, 0.0],
                     [-1.0, 1.0, 0.0],
                     [-3.0, 1.0, 0.0],
                     [-2.0, -1.0, 0.0]])

        triangles = np.array([[1, 9, 0],
                          [1, 2, 3],
                          [3, 4, 5],
                          [5, 6, 7],
                          [7, 8, 9],
                          [1, 9, 3],
                          [3, 7, 9],
                          [3, 5, 7]], dtype='i8')

    if(dim == 3):
        vert = np.array([[-2.0, -3.0, 0.0],
                         [0.0, -2, 0.0],
                         [3.0, -3.0, 0.0],
                         [2.0, -1.0, 0.0],
                         [3.0, 0.5, 0.0],  # 4
                         [1.0, 0.5, 0.0],
                         [0, 3.0, 0.0],
                         [-1.0, 0.5, 0.0],  # 7
                         [-3.0, 0.5, 0.0],
                         [-2.0, -1.0, 0.0],
                         [2.0, 1.5, 0.5],
                         [2.0, 1.5, -0.5]])
        triangles = np.array([[1, 9, 0],
                              [1, 2, 3],
                              [3, 4, 5],
                              [5, 6, 7],
                              [7, 8, 9],
                              [1, 9, 3],
                              [3, 7, 9],
                              [3, 5, 7],
                              [1, 0, 10],  # start of 3D section, front, change all 10's to 11 for back of star3D
                              [0, 9, 10],
                              [10, 9, 8],
                              [7, 8, 10],
                              [6, 7, 10],
                              [5, 6, 10],
                              [5, 10, 4],
                              [10, 3, 4],
                              [3, 10, 2],
                              [10, 1, 2],
                              [1, 0, 11],  # back
                              [0, 9, 11],
                              [11, 9, 8],
                              [7, 8, 10],
                              [6, 7, 11],
                              [5, 6, 11],
                              [5, 10, 4],
                              [11, 3, 4],
                              [3, 11, 2],
                              [11, 1, 2]], dtype='i8')  # end of front
    return vert, triangles

def primrhombicuboctohedron():
    vert  = np.array([[2.0, 8.0, 6.0],
                       [0.0, 6.0, 6.0],
                       [0.0, 2.0, 6.0],
                       [2.0, 0.0, 6.0],
                       [6.0, 0.0, 6.0],
                       [8.0, 2.0, 6.0],
                       [8.0, 6.0, 6.0],
                       [6.0, 8.0, 6.0],
                       [2.0, 6.0, 8.0],
                       [2.0, 2.0, 8.0],
                       [6.0, 6.0, 8.0],#10
                       [6.0, 2.0, 8.0],#11
                       [2.0, 8.0, 2.0],#0 -start of 2nd face
                       [0.0, 6.0, 2.0],#1
                       [0.0, 2.0, 2.0],#2
                       [2.0, 0.0, 2.0],#3
                       [6.0, 0.0, 2.0],#4
                       [8.0, 2.0, 2.0],#5
                       [8.0, 6.0, 2.0],#6
                       [6.0, 8.0, 2.0],#7
                       [2.0, 6.0, 0.0],#8
                       [2.0, 2.0, 0.0],#9
                       [6.0, 6.0, 0.0],#10
                       [6.0, 2.0, 0.0]])#11
    triangles = np.array([[0, 1, 8], #1
                         [1, 2, 9], #2
                         [1, 8, 9], #3
                         [2, 3, 9], #4
                         [3, 9, 11], #5
                         [3, 4, 11], #6
                         [4, 11, 5], #7
                         [5, 11, 10], #8
                         [5, 10, 6], #9
                         [6, 7, 10], #10
                         [7, 8, 10], #11
                         [7, 8, 0], #12
                         [8, 9, 10], #13
                         [9, 10, 11], #14 end of front face, works up to here
                         [12, 13, 20], #1
                         [13, 14, 21], #2
                         [13, 20, 21], #3
                         [14, 15, 21], #4
                         [15, 21, 23], #5
                         [15, 16, 23], #6
                         [16, 23, 17], #7
                         [17, 22, 23], #8
                         [17, 22, 18], #9
                         [18, 19, 22], #10
                         [19, 20, 22], #11
                         [19, 20, 12], #12
                         [20, 21, 22], #13
                         [21, 22, 23], #14
                         [7, 18, 19], #end of back face, start of right side
                         [6, 7, 18],
                         [6, 17, 18],
                         [5, 6, 17],
                         [4, 5, 16],
                         [5, 16, 17], #end of right side, start of left side
                         [0, 1, 12],
                         [1, 12, 13],
                         [1, 2, 13],
                         [2, 13, 14],
                         [2, 3, 14],
                         [3, 14, 15], #end of left side, start of top
                         [0, 7, 12],
                         [7, 12, 19], #end of top, start of bottom
                         [3, 15, 16],
                         [3, 4, 16], #end of shape
                         ], dtype='i8')
    return vert, triangles

def main():
    print(primStar(2))


if __name__ == "__main__":
    main()
