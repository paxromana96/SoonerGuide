import unittest

from name_lookup_utils import remove_prefix, get_canonical_union_room_name, get_canonical_building_name, \
    get_canonical_name
from src.external_building_synonyms import buildings
from src.room_directions import union_rooms


class PrefixRemovalWorksTest(unittest.TestCase):
    def test_prefixRemovalRemovesFromFrontOfLiteral(self):
        self.assertEqual("room", remove_prefix("the room", "the "))

    def test_prefixRemovalDoesntAffectStringsWithoutPrefix(self):
        self.assertEqual("room", remove_prefix("room", "the "))

    def test_prefixRemovalCanRemoveOptionalTheAtFrontOfRoomName(self):
        for canonical_union_room_name in [room.get_names().get_canonical() for room in
                                          union_rooms]:  # just any random test strings
            self.assertEqual(canonical_union_room_name, remove_prefix("the " + canonical_union_room_name, "the "),
                             "prefix removal not working")
            self.assertEqual(canonical_union_room_name, remove_prefix(canonical_union_room_name, "the "),
                             "prefix removal affecting strings without prefix")


class RoomCanonicalNameLookupTestCase(unittest.TestCase):
    def test_allCanonicalRoomNamesReturnCanonicalRoomName(self):
        for canonical_room_name in [room.get_names().get_canonical() for room in union_rooms]:
            self.assertEqual(canonical_room_name, get_canonical_name(canonical_room_name, union_rooms),
                             "canonical union room name should return itself")  # idempotency
            self.assertEqual(canonical_room_name,
                             get_canonical_name(canonical_room_name.replace("_", " "), union_rooms),
                             "should be able to say canonical room name (with spaces) and get the canonical part back")  # fine if we do the key with space separations

    def test_allUnionRoomSynonymsReturnCorrectCanonicalRoomName(self):
        for room in union_rooms:
            for room_synonym in room.get_names():
                self.assertEqual(room.get_names().get_canonical(), get_canonical_name(room_synonym, union_rooms),
                                 "a room's synonym (" + room_synonym + ") didn't identify its key")

    def test_missingRoomReturnsFalse(self):
        self.assertFalse(get_canonical_name('missing room', union_rooms),
                         "Found room that shouldn't have been there!")
        for room in union_rooms:
            self.assertFalse(get_canonical_name(room.get_names().get_canonical() + " FAIL", union_rooms),
                             "Found room that shouldn't have been there!")

    def test_canAddTheToAnyRoomNameAndItStillMatches(self):
        prefix = "the "
        for room in union_rooms:
            self.assertEqual(room.get_names().get_canonical(),
                             get_canonical_name(prefix + room.get_names().get_canonical().replace("_", " "),
                                                union_rooms),
                             str.format("Can't add \"{prefix}\" to the front of canonical room name {name}",
                                        prefix=prefix, name=room.get_names().get_canonical()))
            for room_synonym in room.get_names():
                self.assertEqual(room.get_names().get_canonical(),
                                 get_canonical_name("the " + room_synonym, union_rooms),
                                 str.format("Can't find room {room!s} \
                                             after adding \"{prefix}\" to the front of alias {synonym}",
                                            room=room, prefix=prefix, synonym=room_synonym))


class UnionRoomCanonicalNameLookupTestCase(unittest.TestCase):
    def test_noEmptyStringSynonyms(self):
        for room in union_rooms:
            self.assertFalse("" in room.get_names(),
                             str.format("{room!s} has an empty string as a synonym", room=room))

    def test_allCanonicalRoomNamesReturnCanonicalRoomName(self):
        for canonical_union_room_name in [room.get_names().get_canonical() for room in union_rooms]:
            self.assertEqual(canonical_union_room_name, get_canonical_union_room_name(canonical_union_room_name),
                             "canonical union room name should return itself")  # idempotency
            self.assertEqual(canonical_union_room_name,
                             get_canonical_union_room_name(canonical_union_room_name.replace("_", " ")),
                             "should be able to say canonical room name (with spaces) and get the canonical part back")  # fine if we do the key with space separations

    def test_allUnionRoomSynonymsReturnCorrectCanonicalRoomName(self):
        for room in union_rooms:
            for room_synonym in room.get_names().get_aliases():
                self.assertEqual(room.get_names().get_canonical(), get_canonical_union_room_name(room_synonym),
                                 "a room's synonym (" + room_synonym + ") didn't identify its key")

    def test_missingRoomReturnsFalse(self):
        self.assertFalse(get_canonical_union_room_name('missing room'), "Found room that shouldn't have been there!")
        for room in union_rooms:
            self.assertFalse(get_canonical_union_room_name(room.get_names().get_canonical() + " FAIL"),
                             "Found room that shouldn't have been there!")

    def test_canAddTheToAnyRoomNameAndItStillMatches(self):
        for room in union_rooms:
            canonical_room_name = room.get_names().get_canonical()
            self.assertEqual(canonical_room_name,
                             get_canonical_union_room_name("the " + canonical_room_name.replace("_", " ")),
                             "Can't add \"the \" to the front of any canonical room name")
            for room_synonym in room.get_names().get_aliases():
                self.assertEqual(canonical_room_name, get_canonical_union_room_name("the " + room_synonym),
                                 "Can't add \"the \" to the front of any room name")

    def test_noCapitalLetters(self):
        """
        Makes sure none of the names listed have capital letters.
        This is important, because the Alexa device will not know how to capitalize user speech
        """
        for room in union_rooms:
            for room_synonym in room.get_names():
                self.assertTrue(room_synonym.islower(),
                                "{room!s} name synonym {syn!s} has a capital letter".format(room=room,
                                                                                            syn=room_synonym))


class BuildingCanonicalNameLookupTestCase(unittest.TestCase):
    def test_noEmptyStringSynonyms(self):
        for building in buildings:
            self.assertFalse("" in building.get_names(),
                             str.format("{building!s} has an empty string as a synonym", building=building))

    def test_allCanonicalBuildingNamesReturnCanonicalBuildingName(self):
        for canonical_building_name in [building.get_names().get_canonical() for building in buildings]:
            self.assertEqual(canonical_building_name, get_canonical_building_name(canonical_building_name),
                             "canonical building name should return itself")  # idempotency
            self.assertEqual(canonical_building_name,
                             get_canonical_building_name(canonical_building_name.replace("_", " ")),
                             # fine if we do the key with space separations
                             "should be able to say canonical building name (with spaces) \
                             and get the canonical part back, but couldn't for " + canonical_building_name)

    def test_allBuildingSynonymsReturnCorrectCanonicalBuildingName(self):
        for building in buildings:
            for building_synonym in building.get_names():
                self.assertEqual(building.get_names().get_canonical(), get_canonical_building_name(building_synonym),
                                 "a building's synonym (" + building_synonym + ") didn't identify its key")

    def test_missingBuildingReturnsFalse(self):
        self.assertFalse(get_canonical_building_name('missing building'),
                         "Found building that shouldn't have been there!")
        for building in buildings:
            self.assertFalse(get_canonical_building_name(building.get_names().get_canonical() + " FAIL"),
                             "Found building that shouldn't have been there!")

    def test_canAddTheToAnyBuildingNameAndItStillMatches(self):
        for building in buildings:
            canonical_building_name = building.get_names().get_canonical()
            self.assertEqual(canonical_building_name,
                             get_canonical_building_name("the " + canonical_building_name.replace("_", " ")),
                             "Can't add \"the \" to the front of canonical building name for " + canonical_building_name)
            for building_synonym in building.get_names():
                self.assertEqual(canonical_building_name, get_canonical_building_name("the " + building_synonym),
                                 "Can't add \"the \" to the front of building name synonym " + building_synonym)

    def test_noCapitalLetters(self):
        for building in buildings:
            self.assertTrue(building.get_names().get_canonical().islower(),
                            "canonical name " + building.get_names().get_canonical() + " has a capital letter")
            for building_synonym in building.get_names():
                self.assertTrue(building_synonym.islower(),
                                str.format("{building!s} synonym {synonym!s} has a capital letter",
                                           building=building, synonym=building_synonym))


if __name__ == '__main__':
    unittest.main()
