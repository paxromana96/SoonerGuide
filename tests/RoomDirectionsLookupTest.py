import unittest

from src.Lambda import on_intent, ROOM_NAME_SLOT_KEY
from src.room_directions import union_rooms


def create_intent_for_looking_up_room(user_provided_room_name):
    return {'intent': {'name': 'WhereIsMyRoom', 'slots': {ROOM_NAME_SLOT_KEY: {'value': user_provided_room_name}}},
            'requestId': ""}


class RoomDirectionsTestCase(unittest.TestCase):
    def test_allUnionRoomsHaveDirections(self):
        for room in union_rooms:
            self.assertIsNotNone(room.get_directions(),
                                 "Room {room!s} is missing directions".format(room=room))

    def test_firingIntentForRoomReturnsExpectedDirections(self):
        for room in union_rooms:
            self.assertEqual(room.get_directions(),
                             on_intent(create_intent_for_looking_up_room(room.get_names()),
                                       {"sessionId": ""})['response']['outputSpeech']['text'],
                             "Room {room!s} gave unexpected/wrong directions".format(room=room))

    def test_firingIntentForRoomSynonymsReturnsExpectedDirections(self):
        for room in union_rooms:
            for room_synonym in room.get_names().get_aliases():
                self.assertEqual(room.get_directions(),
                                 on_intent(create_intent_for_looking_up_room(room_synonym),
                                           {"sessionId": ""})['response']['outputSpeech']['text'],
                                 "Room {room!s} gave unexpected/wrong directions using the synonym {synonym}"
                                 .format(room=room, synonym=room_synonym))

    def test_firingIntentForUnknownRoomReturnsSomeText(self):
        self.assertIsNotNone(on_intent(create_intent_for_looking_up_room("missing room"),
                                       {"sessionId": ""})['response']['outputSpeech']['text'],
                             "No text generated indicating we could not find the \"missing room\"")


if __name__ == '__main__':
    unittest.main()
