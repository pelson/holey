from matplotlib.patches import Polygon as _MPLPoly


def loop(ax, loop, *, color='blue', alpha=0.4):
    p = _MPLPoly(
            [(p.x, p.y) for p in loop],
            closed=True, alpha=alpha, facecolor=color)
    ax.add_patch(p)
    return p


def point(ax, pt, *, marker='o', color='blue', size=6):
    [p] = ax.plot(
            pt.x, pt.y,
            marker=marker, color=color, markersize=size)
    return p


def splat(*geoms):
    """
    Throw multiple geometries at an axes, and show it.
    You have no control over the style - if you need such a thing,
    call the appropriate draw functions yourself.

    """
    import matplotlib.pyplot as plt

    from .point import Point

    fig, ax = plt.subplots()
    for geom in geoms:
        if isinstance(geom, Point):
            point(ax, geom)
        else:
            loop(ax, geom)
    plt.show()
