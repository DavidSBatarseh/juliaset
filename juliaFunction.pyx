import cython
cpdef juliaSet(int mouseX,int mouseY,int width,int height):
    cdef int iterationArray[160000], x, y, iterations
    cdef float complexX, complexY, cx, cy, temporaryValue
    for x in range(width):
        for y in range(height):

            complexX = (x-width/2)/(width/3)
            complexY = (y-height/2)/(height/3)

            cx = (mouseX-width/2)/(width/3)
            cy = (mouseY-height/2)/(height/3)

            iterations = 0
            while complexX * complexX + complexY * complexY < 2 and iterations < 10:
                temporaryValue = complexX * complexX - complexY * complexY
                complexY = 2 * complexX * complexY + cy
                complexX = temporaryValue + cx
                
                iterations += 1
            iterationArray[x + y * 400] = iterations
    return iterationArray