class Sphere:
    # finish class Sphere here
    PI = 3.1415
    volume = 0

    def __init__(self, radius):
        Sphere.volume = (4 / 3) * Sphere.PI * (radius ** 3)
