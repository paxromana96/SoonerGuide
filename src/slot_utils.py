from name_lookup_utils import get_pronounceable_names


def make_slots_for_names_of_locations(locations):
    return [{'id': location.get_names().get_canonical(),
             'name': {'value': location.get_names().get_canonical().replace('_', ' '),
                      'synonyms': get_pronounceable_names(location.get_names())}}
            for location in locations]
