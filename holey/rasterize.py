import numba
import numpy as np

from .loop import winding_number
from .point import Point


@numba.jit(nopython=True)
def _rasterize(simplicies, points, target, target_x, target_y):
    nx = target_x.size
    ny = target_y.size
    n_geoms = len(simplicies)
    orig = target.copy()
    
    # NOTE: Order of operations is interchangable (and can have
    # a big impact on performance!)
    for j in range(ny):
        for i in range(nx):
            for simplex_i in range(n_geoms):
                loop = points[simplicies[simplex_i, :]]
                loop = loop[::-1, :]

                pt = Point(target_x[i], target_y[j])
                if winding_number(loop, pt) != 0:
                    target[j, i] = simplex_i
                    break
    return target


@numba.jit
def pixels(tri, shape, extent=None):
    # extent: (x0, x1, y0, y1)
    ny, nx = shape

    if extent is None:
        extent = [tri.points[:, 0].min(), tri.points[:, 0].max(),
                  tri.points[:, 1].min(), tri.points[:, 1].max()]
    
    target_x = np.linspace(extent[0], extent[1], nx)
    target_y = np.linspace(extent[3], extent[2], ny)
    target = np.zeros([ny, nx], dtype=np.uint64) - 1
    overflow = target[0, 0]
    
    target = _rasterize(tri.simplices, tri.points, target, target_x, target_y)
    target = np.ma.masked_equal(target, overflow)
    return extent, target

