import numpy as np


def generate_naca4(m, p, t, n=100):
    x = np.linspace(0, 1, n)

    yt = 5 * t * (
        0.2969 * np.sqrt(x)
        - 0.1260 * x
        - 0.3516 * x**2
        + 0.2843 * x**3
        - 0.1015 * x**4
    )

    yc = np.where(
        x < p,
        m / (p**2) * (2 * p * x - x**2),
        m / ((1 - p)**2) * ((1 - 2 * p) + 2 * p * x - x**2),
    )

    xu = x
    yu = yc + yt
    xl = x
    yl = yc - yt

    coords = np.vstack([
        np.column_stack([xu[::-1], yu[::-1]]),
        np.column_stack([xl[1:], yl[1:]])
    ])

    return coords


def save_dat(coords, filepath):
    with open(filepath, "w") as f:
        for x, y in coords:
            f.write(f"{x} {y}\n")
