class AliasedName:
    """
    Defines a standard way to interact with groups of names that refer to the same thing
    """

    def __init__(self, canonical_name, aliases):
        self.canonical_name = canonical_name

        # insist that we have a copy of the given collection,
        # so we don't a) have a single object when we don't expect,
        # or b) have a handle to a collection that someone else might modify
        self.aliases = [alias for alias in aliases]

    def get_canonical_name(self):
        return self.canonical_name

    def get_aliases(self):
        """
        Returns all aliases (excluding the canonical name) that refer to this object
        :return:
        """
        return self.aliases

    def get_all_names(self):
        """
        Returns all names (including all aliases) that refer to this object
        :return:
        """
        return self.aliases + [self.canonical_name]

    def matches(self, name):
        """
        Determines whether the given name refers to one of this name's aliases
        :param name: a name to test, to see if it refers to this object
        :return: true if the given name matches one of this object's names
        """
        return name in self.get_all_names()

    def __str__(self):
        return self.get_canonical_name()


class Location:
    def __init__(self, name, directions):
        self.name = name
        self.directions = directions

    def get_name(self):
        return self.name

    def get_directions(self, from_location_name):
        return self.directions.get_directions(from_location_name=from_location_name)


class Room(Location):
    def __init__(self, name, directions):
        super(Room, self).__init__(name, directions)


class Building(Location):
    def __init__(self, name, directions, rooms):
        super(Building, self).__init__(name, directions)
        self.rooms = [room for room in rooms]

    def get_rooms(self):
        return self.rooms

    def get_room_named(self, room_name):
        for room in self.rooms:
            if room.get_name().matches(room_name):
                return room
        return None


class Directions:
    """
    Defines a way to look up directions to a location, optionally specifying
    special directions when coming from particular places
    """

    def __init__(self, standard_directions, special_directions):
        self.standard_directions = standard_directions
        self.special_directions = special_directions

    def get_simple_directions(self):
        return self.standard_directions

    def get_directions_from(self, other_location_name):
        if other_location_name in self.special_directions.keys():
            return self.special_directions.get(other_location_name)
        return self.get_simple_directions()

    def get_directions(self, from_location_name=None):
        return self.get_directions_from(from_location_name)
