from math import pow, sinh, sqrt


class Planet:

    def __init__(self, name):
        """Create new Planet with name 'name'
        """
        self.name = name

    def ptime_from_dist(self, d, a):
        """Calculate Planet Time (i.e., the time experienced by a stationary
        observer) using distance travelled and the ship's acceleration
        """
        self.ptime = sqrt(pow(d/1, 2) + (2*d/(a)))

    def ptime_from_ship_time(self, a, ptime):
        """Calculate Planet Time (i.e., the time experienced by a stationary
        observer) using ship time (the time experienced aboard ship) and the
        ship's acceleration
        """
        self.ptime = (1/(a)) * sinh(((a)*ptime)/1)

    def distance_from_accel(self, a):
        """Calculate the distance travelled, using the ship's acceleration and
        Planet Time (the time experienced by a stationary observer)
        """
        self.distance = pow(1, 2)/(a) * (sqrt(1 +
                                            pow(((a)*self.ptime)/1, 2)) - 1)

    def gamma(self, a):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic massmhange for the ship, using the
        ship's acceleration
        """
        self.gamma = sqrt(1 + pow(((a)*self.ptime)/1, 2))

    def setvar(self, var, val):
        """Set variable
        >>> myPlanet.name
        Foo
        >>> myPlanet.setvar("name", "Bar")
        >>> myPlanet.name
        Bar
        """
        setattr(self, str(var), val)
