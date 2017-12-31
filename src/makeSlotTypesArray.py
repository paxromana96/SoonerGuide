import json

from Lambda import ROOM_NAME_SLOT_KEY, BUILDING_NAME_SLOT_KEY
from external_building_synonyms import buildings
from room_directions import union_rooms
from slot_utils import make_slots_for_names_of_locations


def make_alexa_interaction_model_slot_types_array(map_of_slot_name_to_synonyms):
    return [
        {
            "name": slot_name,
            "values": map_of_slot_name_to_synonyms[slot_name]
        }
        for slot_name in map_of_slot_name_to_synonyms
    ]


if __name__ == '__main__':
    print(json.dumps(make_alexa_interaction_model_slot_types_array(
        {
            ROOM_NAME_SLOT_KEY: make_slots_for_names_of_locations(union_rooms),
            BUILDING_NAME_SLOT_KEY: make_slots_for_names_of_locations(buildings)
        }
    )))
