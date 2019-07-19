from math import asinh, acosh, cosh, pow, sqrt, tanh


class Ship:

    def __init__(self, name, a):
        """Create new ship object with name 'name' and accel 'a' (where 'a' is
        some number multiplied by 'g')
        """
        self.name = name
        self.accel = a

    def ship_time_from_terra(self, tt):
        """Calculate Ship Time (i.e., time experienced aboard ship) using
        the time experienced from a stationary observer (Terra Time)
        """
        self.stime = (1/(self.accel)) * asinh(((self.accel)*tt))

    def ship_time_from_d(self, d):
        """Calculate Ship Time (i.e., time experienced aboard ship) using
        the distance travelled
        """
        self.stime = (1/(self.accel)) * acosh(((self.accel)*d)/pow(1, 2) + 1)

    def gamma_self(self):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship
        """
        self.gamma = cosh(((self.accel)*self.stime))

    def gamma_d(self, d):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship, using the
        distance travelled
        """
        self.gamma = ((self.accel)*d)/pow(1, 2) + 1

    def gamma_tt(self, tt):
        """Calculate gamma (a.k.a., the Lorentz factor) - the factor by which
        time, length, and relativistic mass change for the ship, using
        Terra Time
        """
        self.gamma = sqrt(1 + pow(((self.accel)*tt), 2))

    def velocity_self(self):
        """Calculate velocity as a percent of the speed of light
        """
        self.velocity = tanh(((self.accel)*self.stime))

    def setvar(self, var, val):
        """Set variable
        >>> myShip.accel
        1
        >>> myShip.setvar("accel", 21)
        >>> myShip.accel
        21
        """
        setattr(self, str(var), val)
