import cython
from libc.stdlib cimport malloc
cpdef juliaSet(int mouseX,int mouseY,int width,int height, int maxiterations):
    #cdef int arrayLength = width * height
    #TODO: Dynamically sized array as width * height, set to 500000 for convenience currently.
    cdef int iterationArray[160000], x, y, iterations
    cdef float complexX, complexY, cx, cy, temporaryValue
    #iterationArray = <float *> malloc(arrayLength * sizeof(float))
    for x in range(width):
        for y in range(height):

            complexX = (x-width/2)/(width/3)
            complexY = (y)/(height/1.5)

            cx = (mouseX-width/2)/(width/3)
            cy = (mouseY-height)/(height/1.5)

            iterations = 0
            while complexX * complexX + complexY * complexY < 2 and iterations < maxiterations:
                temporaryValue = complexX * complexX - complexY * complexY
                complexY = 2 * complexX * complexY + cy
                complexX = temporaryValue + cx
                
                iterations += 1
            iterationArray[x + y * 400] = iterations
    return iterationArray