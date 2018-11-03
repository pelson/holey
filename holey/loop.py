"""



"""


import numba

from .point import Point


@numba.jit(nopython=True)
def is_left(P0, P1, P2):
    """
    // isLeft(): tests if a point is Left|On|Right of an infinite line.
    //    Input:  three points P0, P1, and P2
    //    Return: >0 for P2 left of the line through P0 and P1
    //            =0 for P2  on the line
    //            <0 for P2  right of the line
    //    See: Algorithm 1 "Area of Triangles and Polygons"

    Credit:
        Original C implementation by Dan Sunday http://geomalgorithms.com/
        C implementation license:

            Copyright 2000 softSurfer, 2012 Dan Sunday
            This code may be freely used and modified for any purpose
            providing that this copyright notice is included with it.

    """
    return ((P1.x - P0.x) * (P2.y - P0.y)
            - (P2.x -  P0.x) * (P1.y - P0.y))


@numba.jit(nopython=True)
def crossing_number(loop, point):
    """
    // cn_PnPoly(): crossing number test for a point in a loop
    //      Input:   P = a point,
    //               V[] = vertex points of a loop V[n+1] with V[n]!=V[0]
    //      Return:  0 = outside, 1 = inside
    // This code is patterned after [Franklin, 2000]


    Credit:
        Original C implementation by Dan Sunday http://geomalgorithms.com/
        C implementation license:

            Copyright 2000 softSurfer, 2012 Dan Sunday
            This code may be freely used and modified for any purpose
            providing that this copyright notice is included with it.


    """
    n = len(loop)
    cn = 0  #    // the  crossing number counter

    # loop through all edges of the loop
    for i in range(-1, n-1):  # edge from V[i]  to V[i+1]
       if (((loop[i, 1] <= point.y) and (loop[i+1, 1] > point.y))     # an upward crossing
            or
           ((loop[i, 1] > point.y) and (loop[i+1, 1] <= point.y))):   # a downward crossing
            # compute  the actual edge-ray intersect x-coordinate
            vt = (point.y  - loop[i, 1]) / (loop[i+1, 1] - loop[i, 1])
            if (point.x <  loop[i, 0] + vt * (loop[i+1, 0] - loop[i, 0])): # point.x < intersect
                 cn += 1  # a valid crossing of y=P.y right of P.x
    return cn #bool(cn % 2)  # 0 if even (out), and 1 if  odd (in)


# @numba.jit
# def winding_number(point, loop):
#     pass


@numba.jit(nopython=True)
def winding_number(loop, point):
    """
    // wn_PnPoly(): winding number test for a point in a loop
    //      Input:   P = a point,
    //               V[] = vertex points of a loop V[n+1] with V[n]!=V[0]
    //      Return:  wn = the winding number (=0 only when P is outside)


    Credit:
        Original C implementation by Dan Sunday http://geomalgorithms.com/
        C implementation license:

            Copyright 2000 softSurfer, 2012 Dan Sunday
            This code may be freely used and modified for any purpose
            providing that this copyright notice is included with it.

    """
    n = len(loop)
    wn = 0  #;    // the  winding number counter

    # loop through all edges of the loop
    for i in range(-1, n-1):  # edge from V[i]  to V[i+1]
        if (loop[i, 1] <= point.y):  #          // start y <= P.y
            if (loop[i+1, 1] > point.y): #     // an upward crossing
                 if (is_left(Point(loop[i, 0], loop[i, 1]),
                             Point(loop[i+1, 0], loop[i+1, 1]), point) > 0):  # // P left of  edge
                     wn += 1  #       // have  a valid up intersect
        else:  #                     // start y > P.y (no test needed)
            if (loop[i+1, 1] <= point.y):  #     // a downward crossing
                 if (is_left(Point(loop[i, 0], loop[i, 1]),
                             Point(loop[i+1, 0], loop[i+1, 1]), point) < 0):  # // P right of  edge
                     wn -= 1
    return wn
