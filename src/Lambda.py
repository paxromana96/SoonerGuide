"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function

from external_building_synonyms import buildings
from name_lookup_utils import get_location_matching_name
from room_directions import union_rooms

# --------------- Helpers that build all of the responses ----------------------
ROOM_DIRECTIONS_INTENT_NAME = "WhereIsMyRoom"
BUILDING_DIRECTIONS_INTENT_NAME = "WhereIsMyBuilding"
ROOM_NAME_SLOT_KEY = 'RoomName'
BUILDING_NAME_SLOT_KEY = 'BuildingName'


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Sooner Guide test. " \
                    "Please ask me for directions by asking me something like, " \
                    "Where is KXOU?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please ask me for directions by saying something like, " \
                    "Where is Crossroads?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Sooner Guide. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_directions_for_intent(intent, session):
    """Creates an appropriate response, given intent and session information directly from Alexa"""

    matching_room = get_location_matching_name(intent['slots'][ROOM_NAME_SLOT_KEY]['value'], union_rooms)

    if matching_room is False or matching_room not in union_rooms:
        # meaning we can't find what room they're talking about
        # TODO: generalize this to search through all locations
        # TODO: reprompt them for the room name they meant to say
        return build_response(session_attributes={},
                              speechlet_response=build_speechlet_response(
                                  title="Directions to \"" + intent['slots'][ROOM_NAME_SLOT_KEY]['value'] + "\"",
                                  output=("I don't know where the room called " + intent['slots'][ROOM_NAME_SLOT_KEY][
                                      'value'] + " is."),
                                  reprompt_text=None,
                                  should_end_session=True))
    else:  # if we COULD get a canonical room_name
        return build_directions_response_from_directions_source(destination=matching_room, locations=union_rooms)


# TODO: Check to see if the intent works properly
def get_directions_for_blding_intent(intent, session):
    matching_building = get_location_matching_name(intent['slots'][BUILDING_NAME_SLOT_KEY]['value'], buildings)

    if matching_building is False or matching_building not in buildings:
        # TODO: reprompt them for the building they meant to say
        return build_response(session_attributes={},
                              speechlet_response=build_speechlet_response(
                                  title="Directions to \"" + intent['slots'][BUILDING_NAME_SLOT_KEY]['value'] + "\"",
                                  output=(
                                          "I don't know where the building called " +
                                          intent['slots'][BUILDING_NAME_SLOT_KEY][
                                              'value'] + " is."),
                                  reprompt_text=None,
                                  should_end_session=True))
    else:  # if we COULD get a canonical building_name
        return build_directions_response_from_directions_source(destination=matching_building,
                                                                locations=buildings)


def build_directions_response_from_directions_source(destination, locations):
    speech_output = destination.get_directions()
    card_title = "Directions to " + destination.get_names().get_canonical().replace('_', ' ')
    reprompt_text = None
    should_end_session = True

    session_attributes = {}
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # print("on_intent intentInfo=" + json.dumps(intent_request['intent']))

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == ROOM_DIRECTIONS_INTENT_NAME:
        return get_directions_for_intent(intent, session)
    elif intent_name == BUILDING_DIRECTIONS_INTENT_NAME:
        return get_directions_for_blding_intent(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    # print('onHandle event_request=' + json.dumps(event['request']))

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
