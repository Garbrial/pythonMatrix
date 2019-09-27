import os
import time
import pandas as pandas

def printmatrix(matrix):
    """Prints a matrix row by row to the console"""
    for row in matrix:
        print(row)

def matrixmult(matrix1, matrix2):
    """Calculates the multiplication of two equal sized matrices -> Matrix"""
    out = [[0 for x in range(len(matrix2))]for y in range(len(matrix1[0]))]

    for y, row in enumerate(out):
        for x in range(len(row)):
            t = 0
            h = 0
            for elem1 in matrix1[y]:
                p = matrix2[h]
                t += elem1 * p[x]
                h += 1
                
            out[y][x] = t

    return out

def matrixmultodd(matrix1, matrix2):
    out = [[0 for x in range(len(matrix2[0]))]for y in range(len(matrix1))]
    return out

if __name__ == "__main__":
    dotProd3x3 = lambda a, b: [[((a[0][0] * b[0][0]) + (a[0][1] * b[1][0]) + (a[0][2] * b[2][0])), ((a[0][0] * b[0][1]) + (a[0][1] * b[1][1]) + (a[0][2] * b[2][1])), ((a[0][0] * b[0][2]) + (a[0][1] * b[1][2]) + (a[0][2] * b[2][2]))],
                               [((a[1][0] * b[0][0]) + (a[1][1] * b[1][0]) + (a[1][2] * b[2][0])), ((a[1][0] * b[0][1]) + (a[1][1] * b[1][1]) + (a[1][2] * b[2][1])), ((a[1][0] * b[0][2]) + (a[1][1] * b[1][2]) + (a[1][2] * b[2][2]))],
                               [((a[2][0] * b[0][0]) + (a[2][1] * b[1][0]) + (a[2][2] * b[2][0])), ((a[2][0] * b[0][1]) + (a[2][1] * b[1][1]) + (a[2][2] * b[2][1])), ((a[2][0] * b[0][2]) + (a[2][1] * b[1][2]) + (a[2][2] * b[2][2]))]]
    
    matrix1 = [[2,0,0],
               [0,2,0],
               [0,0,2,]]

    matrix2 = [[1,0,0],
               [0,1,0],
               [0,0,1]]

    matrix3 = [[2,0,0],
               [0,2,0],
               [0,0,2]]

    matrix4 = [[9],
               [9],
               [9]]
    start_time1 = time.perf_counter()
    printmatrix(dotProd3x3(matrix1,matrix2))
    print("---- %s seconds ----" % (time.perf_counter() - start_time1))
    start_time1 = time.perf_counter()
    printmatrix(matrixmult(matrix1, matrix2))
    print("---- %s seconds ----" % (time.perf_counter() - start_time1))
    start_time1 = time.perf_counter()
    printmatrix(matrixmultodd(matrix3, matrix4))
    print("---- %s seconds ----" % (time.perf_counter() - start_time1))
    
    # recurse()