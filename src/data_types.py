def make_own_copy_of(data):
    return [obj for obj in data]


class AliasedName:
    """
    Defines a standard way to interact with groups of names that refer to the same thing
    """

    def __init__(self, canonical_name, aliases=None):
        self.canonical_name = canonical_name

        if aliases is None:
            # Have to do this because mutable default argument is bad,
            # see http://docs.python-guide.org/en/latest/writing/gotchas/
            self.aliases = []
        else:
            # insist that we have a copy of the given collection,
            # so we don't a) have a single object when we don't expect,
            # or b) have a handle to a collection that someone else might modify
            self.aliases = make_own_copy_of(aliases)

    def get_canonical(self):
        return self.canonical_name

    def get_aliases(self):
        """
        Returns all aliases (excluding the canonical name) that refer to this object
        :return:
        """
        return self.aliases

    def get_all(self):
        """
        Returns all names (including all aliases) that refer to this object
        :return:
        """
        return [self.canonical_name] + self.aliases

    def matches(self, name):
        """
        Determines whether the given name refers to one of this name's aliases
        :param name: a name to test, to see if it refers to this object
        :return: true if the given name matches one of this object's names
        """
        return AliasedName.normalize_for_matching(name) \
               in [AliasedName.normalize_for_matching(name) for name in self.get_all()]

    @staticmethod
    def normalize_for_matching(obj):
        return str(obj).replace('_', ' ')

    def __eq__(self, other):
        return self.get_canonical() == str(other)

    def __str__(self):
        return self.get_canonical()

    def __iter__(self):
        """
        Returns an iterator over all of the names that refer to this object
        """
        return self.get_all().__iter__()


class Location:
    def __init__(self, names, directions, interior_locations=None):
        self.names = names
        self.directions = directions
        if interior_locations is None:
            # necessary because mutable default arguments are bad,
            # see http://docs.python-guide.org/en/latest/writing/gotchas/
            self.interior_locations = []
        else:
            self.interior_locations = make_own_copy_of(interior_locations)

    def get_names(self):
        return self.names

    def get_directions(self, from_location_name=None):
        return self.directions.get_directions(from_location_name=from_location_name)

    def get_interior_locations(self):
        return self.interior_locations

    def __str__(self):
        return self.get_names().__str__()


class Room(Location):
    def __init__(self, names, directions):
        super(Room, self).__init__(names, directions)


class Building(Location):
    def __init__(self, names, directions, rooms=None):
        super(Building, self).__init__(names, directions, rooms)

    def get_rooms(self):
        return self.get_interior_locations()

    def get_room_named(self, room_name):
        for room in self.get_rooms():
            if room.get_names().matches(room_name):
                return room
        return None


class Directions:
    """
    Defines a way to look up directions to a location, optionally specifying
    special directions when coming from particular places
    """

    def __init__(self, standard_directions, special_directions=None):
        self.standard_directions = standard_directions
        if special_directions is None:
            # Have to do this because mutable default argument is bad,
            # see http://docs.python-guide.org/en/latest/writing/gotchas/
            self.special_directions = {}
        else:
            self.special_directions = special_directions

    def get_simple_directions(self):
        return self.standard_directions

    def get_directions_from(self, other_location_name):
        if other_location_name in self.special_directions.keys():
            return self.special_directions.get(other_location_name)
        return self.get_simple_directions()

    def get_directions(self, from_location_name=None):
        return self.get_directions_from(from_location_name)

    def __str__(self):
        return self.get_simple_directions()
