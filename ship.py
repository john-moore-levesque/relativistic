from math import asinh, acosh, cosh, pow, sqrt, tanh
from simulator import c, g


class Ship:

    def __init__(self, name, a):
        """Create new ship object with name 'name' and accel 'a*g' (where g is
        1 standard gravity
        """
        self.name = name
        self.accel = a*g

    def proper_time_from_terra(self, tt):
        """Calculate proper time (i.e., time experienced aboard ship) using
        the time experienced from a stationary observer (Terra Time)
        """
        self.ptime = (c/(self.accel)) * asinh(((self.accel)*tt)/c)

    def proper_time_from_d(self, d):
        """Calculate proper time (i.e., time experienced aboard ship) using
        the distance travelled
        """
        self.ptime = (c/(self.accel)) * acosh(((self.accel)*d)/pow(c, 2) + 1)

    def gamma(self):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship
        """
        self.gamma = cosh(((self.accel)*self.ptime)/c)

    def gamma_d(self, d):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship, using the
        distance travelled
        """
        self.gamma = ((self.accel)*d)/pow(c, 2) + 1

    def gamma_tt(self, tt):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship, using
        Terra Time
        """
        self.gamma = sqrt(1 + pow(((self.accel)*tt)/c, 2))

    def velocity(self):
        """Calculate velocity as a percent of the speed of light
        """
        self.velocity = c * tanh(((self.accel)*self.ptime)/c)

    def setvar(self, var, val):
        """Set variable
        >>> myShip.accel
        1
        >>> myShip.setvar("accel", 21)
        >>> myShip.accel
        21
        """
        setattr(self, str(var), val)

    def delvar(self, var):
        """Delete variable
        >>> myShip.accel
        1
        >>> myShip.delvar("accel")
        >>> myShip.accel
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AttributeError: 'Ship' object has no attribute 'accel'
        >>> myShip.delvar("something-that-doesn't-exist")
        My Ship does not have an attribute called something-that-doesn't-exist
        """
        try:
            delattr(self, str(var))
        except AttributeError:
            print("%s does not have an attribute called %s" % (self.name,
                    str(var)))
