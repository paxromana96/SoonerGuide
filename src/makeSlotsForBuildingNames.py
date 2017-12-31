import json

from external_building_synonyms import buildings
from slot_utils import make_slots_for_names_of_locations

if __name__ == '__main__':
    print(json.dumps(make_slots_for_names_of_locations(buildings)))
