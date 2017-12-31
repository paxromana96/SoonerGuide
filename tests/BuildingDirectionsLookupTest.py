import unittest

from src.Lambda import on_intent, BUILDING_NAME_SLOT_KEY, BUILDING_DIRECTIONS_INTENT_NAME
from src.external_building_synonyms import buildings


def create_intent_for_looking_up_building_by_name(user_provided_building_name):
    return {'intent': {'name': BUILDING_DIRECTIONS_INTENT_NAME,
                       'slots': {BUILDING_NAME_SLOT_KEY: {'value': user_provided_building_name}}},
            'requestId': ""}


class BuildingDirectionsTestCase(unittest.TestCase):
    def test_allBuildingsWithSynonymsHaveDirections(self):
        for building in buildings:
            self.assertIsNotNone(building.get_directions(),
                                 "Building {building!s} is missing directions".format(building=building))

    def test_firingIntentForBuildingReturnsExpectedDirections(self):
        for building in buildings:
            response = on_intent(
                create_intent_for_looking_up_building_by_name(building.get_names().get_canonical().replace('_', ' ')),
                {"sessionId": ""})
            self.assertEqual(building.get_directions(),
                             response['response']['outputSpeech']['text'],
                             "Building {building!s} gave wrong/unexpected directions".format(building=building))

    def test_firingIntentForBuildingSynonymsReturnsExpectedDirections(self):
        for building in buildings:
            for room_synonym in building.get_names():
                response = on_intent(create_intent_for_looking_up_building_by_name(room_synonym), {"sessionId": ""})
                self.assertEqual(building.get_directions(),
                                 response['response']['outputSpeech']['text'],
                                 "Building {building!s} gave wrong/unexpected directions using the synonym {synonym}"
                                 .format(building=building, synonym=room_synonym))

    def test_firingIntentForLookingUpMissingBuildingReturnsSomeText(self):
        response = on_intent(create_intent_for_looking_up_building_by_name("missing building"), {"sessionId": ""})
        self.assertIsNotNone(response['response']['outputSpeech']['text'],
                             "No text given to indicate we could not find the \"missing building\"")


if __name__ == '__main__':
    unittest.main()
