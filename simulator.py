from ship import Ship
from planet import Planet

# g = 1 gravity = 1.03 light years/year^2
# c = speed of light = 1 (because everything is calculated as a percent of c)
g = 1.03
c = 1


def createShip(shipname=None, shipaccel=None):
    """Creates a new ship object
    >>> myShip = createShip()
    Enter a ship name: My Ship
    Enter an acceleration as a multiple of g; hit 'Enter' for 1g: 12
    >>> myShip
    < ship.shipObject at ... >
    >>> myShip.name
    'My Ship'
    >>> myShip.accel
    12
    >>> myOtherShip = createShip("My Other Ship", 3.2")
    >>> myOtherShip
    < ship.shipObject at ... >
    >>> myOtherShip.name
    'My Other Ship'
    >>> myOtherShip.accel
    3.2
    """
    if not shipname:
        name = input("Enter a ship name: ")
    else:
        name = shipname

    if shipaccel:
        accel = shipaccel*g
    else:
        accel = input("Enter an acceleration as a multiple of g; "
                "hit 'Enter' for 1g: ")
        if not accel:
            accel = 1.0*g

    try:
        accel = float(accel)
    except ValueError:
        print("Invalid value " + str(accel) +
            " for accel; setting accel to 1.0")
        accel = 1.0*g

    return Ship(name, accel)


def createPlanet(planetname=None):
    """Creates new planet object
    >>> myplanet = createplanet()
    Enter a planet name: My planet
    >>> myplanet
    < planet.planet object at ... >
    >>> myplanet.name
    My planet
    >>> myOtherplanet = createplanet("My Other planet")
    >>> myOtherplanet
    < planet.planet object at ... >
    >>> myOtherplanet.name
    My Other planet
    """
    if planetname:
        name = planetname
    else:
        name = input("Enter a planet name: ")
    return Planet(name)


def planMission(brachistrone, distance, myShip, myplanet):
    """Plan a mission using given parameters; see below for clarification on the
    brachistrone parameters
    """
    def brachistrone(bdist):
        """In a brachistrone mission, the ship flips end-for-end halfway through
        to decellerate; therefore the ship time (time experienced aboard
        ship) is calculated to the midway point (distance/2) and then doubled
        for the second half of the mission
        """
        myShip.ship_time_from_d(bdist)
        myShip.setvar("stime", 2*myShip.stime)
        myShip.velocity_self()
        myplanet.ptime_from_ship_time(myShip.accel, myShip.stime)
        myShip.gamma_self()

    def nobrachistrone(dist):
        """In a non-brachistrone mission, the ship accelerates the whole way
        through, without making any provision for stopping
        """
        myShip.ship_time_from_d(dist)
        myShip.velocity_self()
        myplanet.ptime_from_ship_time(myShip.accel, myShip.stime)
        myShip.gamma_self()

    if brachistrone:
        brachistrone(distance/2)
    else:
        nobrachistrone(distance)


def resetMission(myShip, myplanet):
    """Deletes all ship variables except for name and accel; deletes all planet
    variables except for name
    """
    for var in vars(myShip):
        if var != 'name' and var != 'accel':
            myShip.setvar(str(var), None)
    for var in vars(myplanet):
        if var != 'name':
            myplanet.setvar(str(var), None)


def testMission():
    """Does a test mission to Vega (27 light years away) at 1g acceleration
    This is a brachistrone mission (i.e., the ship flips over halfway through
    to start decelleration).
    If stime, velocity, gamma, and ptime all match the expected values, then
    isGreen is left at True and everything is good
    If one (or more) deviates, then isGreen is set to False and an error
    message is printed
    In either case, isGreen, the ship, and the planet are returned
    """
    enterprise = createShip("Enterprise", 1)
    earth = createPlanet("Earth")
    vega = 27
    stime_expected = 6.589741132778765
    velocity_expected = 0.9999974558674861
    gamma_expected = 443.31805000000037
    ptime_expected = 430.4047787768305
    isGreen = True
    planMission(True, vega, enterprise, earth)
    try:
        assert enterprise.stime == stime_expected
    except AssertionError:
        print("enterprise.stime: %f" % enterprise.stime)
        print("expected stime: %f" % stime_expected)
        isGreen = False
    try:
        assert enterprise.velocity == velocity_expected
    except AssertionError:
        print("enterprise.velocity: %f" % enterprise.velocity)
        print("expected velocity: %f" % velocity_expected)
        isGreen = False
    try:
        assert enterprise.gamma == gamma_expected
    except AssertionError:
        print("enterprise.gamma: %f" % enterprise.gamma)
        print("expected gamma: %f" % gamma_expected)
        isGreen = False
    try:
        assert earth.ptime == ptime_expected
    except AssertionError:
        print("earth.ptime: %f" % earth.ptime)
        print("expected ptime: %f" % ptime_expected)
        isGreen = False
    return isGreen, enterprise, earth
