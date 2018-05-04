from math import pow, sinh, sqrt
from simulator import c


class Terra:

    def __init__(self, name):
        """Create new Terra with name 'name'
        """
        self.name = name

    def ttime_from_dist(self, d, a):
        """Calculate Terra Time (i.e., the time experienced by a stationary
        observer) using distance travelled and the ship's acceleration
        """
        self.ttime = sqrt(pow(d/c, 2) + (2*d/(a)))

    def ttime_from_proper_time(self, a, ptime):
        """Calculate Terra Time (i.e., the time experienced by a stationary
        observer) using proper time (the time experienced aboard ship) and the
        ship's acceleration
        """
        self.ttime = (c/(a)) * sinh(((a)*ptime)/c)

    def distance_from_accel(self, a):
        """Calculate the distance travelled, using the ship's acceleration and
        Terra Time (the time experienced by a stationary observer)
        """
        self.distance = pow(c, 2)/(a) * (sqrt(1 + pow(((a)*self.ttime)/c, 2)) - 1)

    def gamma(self, a):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship, using the
        ship's acceleration
        """
        self.gamma = sqrt(1 + pow(((a)*self.ttime)/c, 2))

    def setvar(self, var, val):
        """Set variable
        >>> myTerra.name
        Foo
        >>> myTerra.setvar("name", "Bar")
        >>> myTerra.name
        Bar
        """
        setattr(self, str(var), val)

    def delvar(self, var):
        """Delete variable
        >>> myTerra.name
        Foo
        >>> myTerra.delvar("name")
        >>> myTerra.name
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: 'Terra' object has no attribute 'name'
        >>> myOtherTerra.delvar("something-that-doesn't-exist")
        My Other Terra does not have an attribute called
            something-that-doesn't-exist
        """
        try:
            delattr(self, str(var))
        except AttributeError:
            print("%s does not have an attribute called %s" % (self.name, str(var)))
