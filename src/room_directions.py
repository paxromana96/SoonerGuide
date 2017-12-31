from data_types import *

union_rooms = [
    Room(
        names=AliasedName(canonical_name='kxou',
                          aliases=["the radio station", "radio station", "k. x. o. u.", "radio room",
                                   "radio station room"]),
        directions=Directions(
            'The K. X. O. U. radio room is the glass room in the center of the union, \
            across from the central staircase and the One U store.'),
    ),
    Room(
        names=AliasedName(canonical_name='post_office',
                          aliases=["post office", "the post office", "union post office", "the union post office"]),
        directions=Directions('It\'s on the right side of the hallway towards crossroads, across from the Starbucks. '),
    ),
    Room(
        names=AliasedName(canonical_name='sooner_card',
                          aliases=["sooner card office", "sooner card", "sun card", "sun card office"]),
        # some times it thinks "sooner" is pronounced "sun"
        directions=Directions(
            'It\'s on the left side of the hallway leading towards crossroads, to the left of the Starbucks.'),
    ),
    Room(
        names=AliasedName(canonical_name='ou_passport',
                          aliases=["o. u. passport"]),
        directions=Directions(
            'It\'s on the left side of the hallway leading towards crossroads, to the left of the Starbucks.'),
    ),
    Room(
        names=AliasedName(canonical_name='student_art_gallery',
                          aliases=["student art gallery", "art gallery", "art shop"]),
        directions=Directions(
            'It\'s on the left side of the hallway leading towards crossroads, to the left of the Starbucks.'),
    ),
    Room(
        names=AliasedName(canonical_name='starbucks',
                          aliases=["star bucks"]),
        directions=Directions('It\'s in the hallway between Crossroads and the center of the union.'),
    ),
    Room(
        names=AliasedName(canonical_name='credit_union',
                          aliases=["bank", "credit union", "o. u. f. c. u.", "o. u. bank"]),
        directions=Directions(
            'Go down the hall to your left towards Crossroads. It will be on your left at the bottom of the ramp.'),
    ),
    Room(
        names=AliasedName(canonical_name='crossroads',
                          aliases=["cross roads", "24 hour restaurant"]),
        directions=Directions(
            'From the center of the union, go down the hall to your left. It will be on your right after the ramp.'),
    ),
    Room(
        names=AliasedName(canonical_name='lgbtq_lounge',
                          aliases=["queer lounge", "l. g. b. t. q. lounge", "l. g. b. t. lounge", "gay lounge"]),
        directions=Directions(
            "From crossroads, the L. G. B. T. Q. lounge is down the hallway to the left of the counter, \
            past all of the chairs. It's behind the glass door to your right."),
    ),
    Room(
        names=AliasedName(canonical_name='sooner_room',
                          aliases=["sooner room", "sun room"]),
        # sometimes Alexa hears "Sooner" as "sun"
        directions=Directions(
            'From crossroads, the sooner room is to the left, past the microwave, \
            at the end of the hallway just past the bathrooms.'),
    ),
    Room(
        names=AliasedName(canonical_name='student_government_association',
                          aliases=["s. g. a.", "student government", "student government association",
                                   "student government office", "s. g. a. office"]),
        directions=Directions(
            "Go down the hall to your left. Turn right after going down the ramp. \
            It's at the end of the hallway on the right."),
    ),
    Room(
        names=AliasedName(canonical_name='one_university_store',
                          aliases=["one u. store", "o. u. store", "computer store", "one university store"]),
        directions=Directions(
            'The One U. Store is the glass room in the center of the union, across from the union market.'),
    ),
    Room(
        names=AliasedName(canonical_name='union_market',
                          aliases=["union market"]),
        directions=Directions(
            "The Union Market is the room with two cash registers across from the One U. Store, \
            between the food court and the center of the union."),
    ),
    Room(
        names=AliasedName(canonical_name='will_rogers_room',
                          aliases=["will rogers room", "will rogers"]),
        directions=Directions('The Will Rogers Room is across from the food court, on the north side of the union.'),
    ),
    Room(
        names=AliasedName(canonical_name='food_court',
                          aliases=["food court", "food", "chick fill a.", "chic fil a", "quizno's", "laughing tomato",
                                   "taco shop"]),
        directions=Directions('The food court is on the north side of union, past the One U. Store and on your right.'),
    ),
    Room(
        names=AliasedName(canonical_name='clarke_anderson_room',
                          aliases=["clarke anderson room", "clarke anderson"]),
        directions=Directions(
            "The Clarke-Anderson Room, also called the Schooner Room, is on the northwest part of the union. \
            It' past the Will Rogers Room with all the chairs."),
    ),
    Room(
        names=AliasedName(canonical_name='stuart_landing',
                          aliases=["stuart landing"]),
        directions=Directions(
            "The Stuart Landing is immediately in front of the central staircase, on the second floor. \
            It's next to the Beaird Lounge."),
    ),
    Room(
        names=AliasedName(canonical_name='alma_wilson_room',
                          aliases=["alma wilson room", "alma wilson"]),
        directions=Directions(
            "The Alma Wilson room is on the second floor, in the hallway between \
            Meacham Auditorium and the central staircase. \
            The Alma Wilson room is closest to the staircase, across from the elevator."),
    ),
    Room(
        names=AliasedName(canonical_name='pioneer_room',
                          aliases=["pioneer", "pioneer room"]),
        directions=Directions(
            "The Pioneer room is on the second floor, \
            in the hallway between Meacham Auditorium and the central staircase. \
            It's to the left of the elevator, across from the Alma Wilson Room."),
    ),
    Room(
        names=AliasedName(canonical_name='david_f_schrage_traditions_room',
                          aliases=["david f. schrage traditions room", "david schrage", "traditions room",
                                   "traditions"]),
        directions=Directions(
            "The Traditions Room is on the second floor, \
            in the hallway between Meacham Auditorium and the central staircase. \
            It's to the left of the elevator, across from the John and Louise Houchin Rooms."),
    ),
    Room(
        names=AliasedName(canonical_name='john_houchin_room',
                          aliases=["john houchin room"]),
        directions=Directions(
            "The Traditions Room is on the second floor, \
            in the hallway between Meacham Auditorium and the central staircase. \
            It's in the middle of the hallway, across from the Traditions Room."),
    ),
    Room(
        names=AliasedName(canonical_name='louise_houchin_room',
                          aliases=["louise houchin room"]),
        directions=Directions(
            "The Traditions Room is on the second floor, \
            in the hallway between Meacham Auditorium and the central staircase. \
            It's in the middle of the hallway, across from the Traditions Room."),
    ),
    Room(
        names=AliasedName(canonical_name='david_l_boren_lounge',
                          aliases=["david l. boren lounge", "boren lounge", "boren room"]),
        directions=Directions(
            "The Boren Lounge is just to the north of Meacham Auditorium. \
            It's the open room across from the Presidents Room, with all of the bookcases."),
    ),
    Room(
        names=AliasedName(canonical_name='presidents_room',
                          aliases=["president's room", "president room"]),
        directions=Directions(
            "The Presidents Room is on the second floor, \
            in the hallway between Meacham Auditorium and the central staircase. \
            It's across from the Boren Lounge, and has two entrances."),
    ),
    Room(
        names=AliasedName(canonical_name='meacham_auditorium',
                          aliases=["meacham auditorium", "meacham", "auditorium", "movie theatre", "movie theatre"]),
        directions=Directions(
            'The Meacham Auditorium is on the second floor, \
            in the lobby beside the gender equality center.'),
    ),
    Room(
        names=AliasedName(canonical_name='volunteer_office',
                          aliases=["volunteer office"]),
        directions=Directions(
            'The Volunteer Office is on the second floor, \
            in the hallway in front of the Student Affairs office and the staircase.'),
    ),
    Room(
        names=AliasedName(canonical_name='student_affairs',
                          aliases=["student affairs", "student affairs office", "student affairs room"]),
        directions=Directions(
            "Student Affairs is on the second floor. \
            It's at the end of the hallway by bathrooms and the staircase leading up from Crossroads. "),
    ),
    # TODO: fill out these descriptions below a bit more
    Room(
        names=AliasedName(canonical_name='conoco_student_leadership_wing',
                          aliases=["conoco student leadership wing", "conoco", "student leadership",
                                   "student leadership wing"]),
        directions=Directions('The Student Leadership Wing is on the second floor.'),
    ),
    Room(
        names=AliasedName(canonical_name='beaird_lounge',
                          aliases=["beaird lounge", "beard lounge"]),
        directions=Directions(
            'The Beaird Lounge is on the second floor, in the large room between the Frontier Room and Stuart Landing'),
    ),
    Room(
        names=AliasedName(canonical_name='flint_study_center_computer_lab',
                          aliases=["computer lab", "computers", "study center", "flint study center computer lab"]),
        directions=Directions(
            "The Flint Study Center Computer Lab is in the large room beside Stuart Landing. \
            It's in the hallway beside the Crimson Meeting Room."),
    ),
    Room(
        names=AliasedName(canonical_name='crimson_meeting_room',
                          aliases=["crimson room", "crimson meeting room"]),
        directions=Directions(
            "The Crimson Meeting Room is on the second floor. It is in the large room beside Stuart Landing. \
            It's in a hallway just beside the stairs."),
    ),
    Room(
        names=AliasedName(canonical_name='bartlet_study_room',
                          aliases=["bartlet study room", "bartlet room", "study room"]),
        directions=Directions(
            'The Bartlet Study Room is on the second floor. It is just inside the large room beside Stuart Landing.'),
    ),
    Room(
        names=AliasedName(canonical_name='frontier_room',
                          aliases=["frontier room"]),
        directions=Directions(
            "The Frontier Room is on the second floor. \
            It's between the large room by Stuart Landing and the Heritage room, just up the stairs."),
    ),
    Room(
        names=AliasedName(canonical_name='weitzenhoffer_dining_room',
                          aliases=["weitzenhoffer dining room", "dining room", "weitzenhoffer room",
                                   "white zen hoffer room", "white zen four", "white zen fer"]),
        directions=Directions(
            'The Weitzenhoffer Dining Room is on the second floor \
            between the Frontier Room and the Heritage room.'),
    ),
    Room(
        names=AliasedName(canonical_name='heritage_room',
                          aliases=["heritage room"]),
        directions=Directions(
            'The Heritage Room is on the second floor. \
            It is at the end of the hallway in front of the Jan Marie and Richard L. Crawford University Club.'),
    ),
    Room(
        names=AliasedName(canonical_name='crawford_university_club',
                          aliases=["crawford", "university club", "fancy restaurant"]),
        directions=Directions(
            'The Crawford University Club is the second floor. \
            It is up the stairs in the hallway just beyond the Beaird Lounge.'),
    ),
    Room(
        names=AliasedName(canonical_name='career_services',
                          aliases=["career services", "career service"]),
        directions=Directions(
            'Career Services is on the third floor. \
            It is up the central staircase on the opposite side of the Molly Shi Boren Ballroom'),
    ),
    Room(
        names=AliasedName(canonical_name='molly_shi_boren_ballroom',
                          aliases=["molly shi boren ballroom", "ballroom", "molly boren room", "molly shi boren room"]),
        directions=Directions(
            'The Molly Shi Boren Ballroom is on the third floor. \
            It is the large room beside the central staircase'),
    ),
    Room(
        names=AliasedName(canonical_name='governors_room',
                          aliases=["governors' room", "governor's room", "governor room"]),
        directions=Directions('The Governors Room is on the third floor just past the Molly Shi Boren Ballroom'),
    ),
    Room(
        names=AliasedName(canonical_name='regents_room',
                          aliases=["regents' room", "regent's room", "regent room"]),
        directions=Directions(
            'The Regents Room is on the third floor between the Governors Room and the Associates Room.'),
    ),
    Room(
        names=AliasedName(canonical_name='associates_room',
                          aliases=["associates' room", "associate's room", "associate room"]),
        directions=Directions(
            'The Associates Room is on the third floor. \
            It is past the Molly Shi Boren Ballroom at the very end of the hallway past the Governors Room'),
    ),
    Room(
        names=AliasedName(canonical_name='scholars_room',
                          aliases=["scholar's room", "scholar's room", "scholars room", "scholar room"]),
        directions=Directions(
            'The Scholars Room is on the third floor. \
            It is past the Molly Shi Boren Ballroom in the lobby just beyond the restrooms.'),
    ),
    Room(
        names=AliasedName(canonical_name='meacham_balcony',
                          aliases=["meacham balcony", "auditorium balcony", "movie theatre balcony",
                                   "movie theater balcony", "theatre balcony", "theater balcony"]),
        directions=Directions(
            'The Meacham Balcony is on the third floor. \
            It is up the stairs to the left of Meacham Auditorium.'),
    ),
    Room(
        names=AliasedName(canonical_name='student_life',
                          aliases=["student life", "student life office"]),
        directions=Directions(
            'Student Life is on the third floor. \
            It is up stairs leading from Crossroads, just past the bathrooms by the stairs.'),
    ),
    Room(
        names=AliasedName(canonical_name='union_administration_and_programming_board',
                          aliases=["u. p. b.", "u. p. b. office", "union administration and programming board"]),
        directions=Directions(
            'The Union Administration and Programming Board is on the third floor \
            on the opposite side of the Paul Massad Conference Room using the central staircase.'),
    ),
    Room(
        names=AliasedName(canonical_name='alumni_association',
                          aliases=["alumni association", "alumni office"]),
        directions=Directions(
            'The Alumni Association is on the fourth floor \
            on the opposite side the Paul Massad Conference Room using the central staircase.'),
    ),
    Room(
        names=AliasedName(canonical_name='paul_massad_conference_room',
                          aliases=["paul massad conference room", "conference room", "massad conference room"]),
        directions=Directions(
            'The Paul Massad Conference Room is on the fourth floor using the central staircase. \
            Facing the staircase, it is immedietly to the left.')
    )
]
