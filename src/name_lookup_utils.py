from external_building_synonyms import buildings
from room_directions import union_rooms


def get_pronounceable_names(names):
    names = [syn.replace('_', ' ') for syn in names]
    return ["the " + syn for syn in names] + names


def remove_prefix(string_with_prefix, prefix):
    if string_with_prefix.startswith(prefix):
        return string_with_prefix[len(prefix):]
    return string_with_prefix


def get_canonical_union_room_name(intent_value_for_union_room):
    return get_canonical_name(intent_value_for_union_room, union_rooms)


def get_canonical_building_name(intent_value_for_building):
    return get_canonical_name(intent_value_for_building, buildings)


def get_canonical_name(location_name_from_intent, locations_array):
    normalized_name = remove_prefix(location_name_from_intent, 'the ')
    matching_location = get_location_matching_name(normalized_name, locations_array)  # Note - could be False
    return matching_location and matching_location.get_names().get_canonical()  # akin to .? in Swift


def get_location_matching_name(name, locations):
    if not locations:  # that is, if empty array (no locations to search through)
        return False
    for location in locations:
        if location.get_names().matches(name):
            return location
    # otherwise, search through all interior locations within those given
    return get_location_matching_name(name,
                                      locations=list(sum([loc.get_interior_locations() for loc in locations], [])))
