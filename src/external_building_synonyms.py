from data_types import *

buildings = [
    Building(
        names=AliasedName("adams_center", aliases=["adams tower"]),
        directions=Directions(
            "Adams Center is the X-shaped dorm on the west side of the Walker-Adams mall, just south of Lindsey street. \
            It's between Cate Center and Couch Cafeteria.")
    ),
    Building(
        names=AliasedName("adams_hall", aliases=["adams"]),
        directions=Directions('Adams Hall is attached to the Price College of Business, to the east of the library.',
                              )
    ),
    Building(
        names=AliasedName("administration_building", aliases=["admin", "administration", "admin building"]),
        directions=Directions(
            "The Administration / O. C. C. E. building is south of the dorms, on Asp Avenue. \
            It's right next to the three-pointed forum building.",
        )
    ),
    Building(
        names=AliasedName("andrew_m_coats_hall", aliases=["coats hall", "coats"]),
        directions=Directions(
            "The Law building, Andrew Coats Hall, is on the south side of campus, \
            next to the Sam Noble Oklahoma Museum of Natural History. \
            It's on Timberdell Road across the street from the parking lot for the forum building.",

        )
    ),
    Building(
        names=AliasedName("anne_and_henry_zarrow_hall", aliases=["zarrow hall", "zarrow"]),
        directions=Directions(
            'Zarrow Hall is just south of Goddard on Elm Street, to the west of Nielsen and Farzaneh halls.',

        )
    ),
    Building(
        names=AliasedName("armory", aliases=["army r. o. t. c.", "navy r. o. t. c.", "r. o. t. c.", "rotissery",
                                             "r. o. t. c. building"]),
        directions=Directions(
            'The Army and Navy R. O. T. C. Armory is north of the stadium parking lot, \
            and directly across from Price Hall.',

        )
    ),
    Building(
        names=AliasedName("asp_avenue_parking_facility",
                          aliases=["asp parking garage", "union parking garage", "old parking garage"]),
        directions=Directions(
            'The parking facility on Asp Avenue is attached to the stadium on Asp Avenue. \
            You can reach it by turning north onto Asp Avenue from Lindsey, and then turning right.',

        )
    ),
    Building(
        names=AliasedName("bizzell_memorial_library", aliases=["bizzell", "library"]),
        directions=Directions(
            'Bizzell Memorial Library is located in the center of campus, between the North and South ovals. \
            You can enter it from the south oval or from the west clock tower near the Physical Science Center.',

        )
    ),
    Building(
        names=AliasedName("boomer_outreach_building", aliases=["outreach building"]),
        directions=Directions(
            'The Boomer Outreach Building is located just next to the Forum Building, \
            south of the dorms on Asp Avenue.',

        )
    ),
    Building(
        names=AliasedName("boyd_house", aliases=["presidents house", "boren house"]),
        directions=Directions(
            'Walk past the food court and out the western exit. \
             Make your way to the north oval and walk directly due north until you hit Boyd street. \
             On the left side, across the street, is the Boyd House.',

        )
    ),
    Building(
        names=AliasedName("brooks_street_transfer_station",
                          aliases=["cart station", "cart", "public transportation", "bus station", "duck pond",
                                   "duck pond parking lot"]),
        directions=Directions(
            'The Brooks Street transfer station is the bus stop to the east of the stadium on Brooks Street, \
            attached to the parking lot next to the Duck Pond.',

        )
    ),
    Building(
        names=AliasedName("buchanan_hall", aliases=["buchanan", "bursar", "bursar's office"]),
        directions=Directions("Buchanan Hall is the building south of the union, right outside of Crossroads.",
                              )
    ),
    Building(
        names=AliasedName("burton_hall", aliases=["burton"]),
        directions=Directions('Burton Hall is between Goddard Health Center and the parking garage on Elm Street.',
                              )
    ),
    Building(
        names=AliasedName("campus_depot", aliases=["depot"]),
        directions=Directions('The Campus Depot is the bus stop on Asp Avenue right next to the stadium.',
                              )
    ),
    Building(
        names=AliasedName("carnegie_building", aliases=["carnegie hall", "carnegie"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Turn right and walk directly due west until you turn right and walk towards the north oval. \
            Carnegie will be the first building on your right.',
        )
    ),
    Building(
        names=AliasedName("carpenter_hall", aliases=["carpenter"]),
        directions=Directions(
            "Carpenter Hall is north of the union parking garage, across Asp Avenue from Felgar Hall. \
            It's near Jacobson Hall, the visitor center.",

        )
    ),
    Building(
        names=AliasedName("carson_engineering_center", aliases=["carson", "engineering quad"]),
        directions=Directions(
            "Carson Energy Center is on the northwest corner of the engineering quad, \
            at the intersection of Asp Avenue and Boyd Street.",

        )
    ),
    Building(
        names=AliasedName("cate_center",
                          aliases=["cate", "cate 1", "cate 2", "cate 3", "cate 4", "cate 5", "cate cafeteria",
                                   "cate food court", "cate lounge"]),
        directions=Directions(  # TODO: make this special directions from the union
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south, even past Lindsey street. \
            The Cate Center should be between the first set of buildings you hit after crossing Lindsey, \
            and between the street you cross to get to the three dorm towers.',

        )
    ),
    Building(
        names=AliasedName("catlett_music_center", aliases=["catlett", "music building", "orchestra"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Turn right and walk directly due west until you hit Elm avenue. \
            Cross the street, turn right and walk directly due north. \
            The Catlett Music Center will be the last building before you hit Boyd street.',

        )
    ),
    Building(
        names=AliasedName("chemistry_building", aliases=["old chemistry building"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Turn right and walk directly due west until you turn right and walk towards the north oval. \
            The Chemistry building should be the second building on your left.',
        )
    ),
    Building(
        names=AliasedName("collings_hall", aliases=["collings"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south. \
            Collings Hall will be the fourth building on your right.',

        )
    ),
    Building(
        names=AliasedName("collums_commissary", aliases=["collums building"]),
        directions=Directions(
            "Collums Commissary is the skinny building in the athletic practice complex east of the football stadium. \
            It\'s between the large indoor practice facility and the smaller buildings on Lindsey Street.",

        )
    ),
    Building(
        names=AliasedName("copeland_hall", aliases=["journalism building", "journalism"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south. \
            Copeland Hall will be the fifth building on your right.',

        )
    ),
    Building(
        names=AliasedName("couch_cafeteria", aliases=["caf", "calf", "couch restaurants"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south, even past Lindsey street. \
            Past the three dorms, you\'ll run into a circular shaped building. That will be the Couch Cafeteria.',

        )
    ),
    Building(
        names=AliasedName("couch_center", aliases=["couch tower"]),
        directions=Directions(
            'Couch Center is the southern-most dorm building south of Lindsey Street, next to The Caf.',

        )
    ),
    Building(
        names=AliasedName("cross_center", aliases=[]),
        directions=Directions(
            'Cross Center is to the southeast of the dorms, \
             near the school of continuing education and the old forum building.',

        )
    ),
    Building(
        names=AliasedName("dale_hall", aliases=["dale"]),
        directions=Directions(
            'Dale Hall is the southernmost building on the South Oval, on the west side. \
            It\'s across the street from Cate Center Two, next to the OU Daily, \
            and across the South Oval from Gaylord, the Journalism building.',

        )
    ),
    Building(
        names=AliasedName("dale_hall_tower", aliases=["dale tower"]),
        directions=Directions(
            'Dale Hall Tower is the very tall building on the South Oval, just to the west of Dale Hall. \
            It\'s on the corner of Elm and Lindsey.',

        )
    ),
    Building(
        names=AliasedName("devon_energy_hall",
                          aliases=["devon", "devon hall", "engineering", "computer science building",
                                   "school of computer science"]),

        directions=Directions(
            "Devon Energy Hall is the 4-story glass building on the northeast corner of the engineering quad. \
            It's at the intersection of Boyd and Jenkins, just across from Sarkeys tower.",
        )
    ),
    Building(
        names=AliasedName("dunham_residential_college", aliases=["dunham", "dunham college"]),
        directions=Directions(
            'Dunham Residential College is next to Headington Residential College on Lindsey Street, \
            south of the stadium.',

        )
    ),
    Building(
        names=AliasedName("ellison_hall", aliases=["ellison", "math building"]),
        directions=Directions('Ellison Hall is between the library and Goddard Health Center, next to the rose garden.',

                              )
    ),
    Building(
        names=AliasedName("elm_ave_parking_facility", aliases=["elm parking garage"]),
        directions=Directions(
            'The Elm Avenues Parking Facility is on the north side of campus, on Elm Avenue. \
            It\'s next to Catlett school of music, and across from the Physical Science Center.',

        )
    ),
    Building(
        names=AliasedName("elm_avenue", aliases=["elm", "elm avenue"]),
        directions=Directions(
            'Elm Avenue runs along the west side of campus, \
            past the Physical Science Center, Dale Hall, and the dorms.',

        )
    ),
    Building(
        names=AliasedName("engineering_laboratory", aliases=["engineer lab", "engineering lab"]),
        directions=Directions("The Engineering Laboratory is across Asp Avenue from the union.",
                              )
    ),
    Building(
        names=AliasedName("evans_hall", aliases=["evans"]),
        directions=Directions('Evans Hall is on the north oval, directly north of the library.',
                              )
    ),
    Building(
        names=AliasedName("exxon_mobile_lawrence_g_rawl_practice_facility",
                          aliases=["rawl building", "engineering practice facility", "practice facility"]),
        directions=Directions(
            'The Rawl Engineering Practice Facility, or R. E. P. L., \
            is on the engineering quad, just south of Devon Energy Center.',

        )
    ),
    Building(
        names=AliasedName("facilities_management_complex", aliases=[]),
        directions=Directions('The Facilities Management Complex is on Felgar Street near the union.',
                              )
    ),
    Building(
        names=AliasedName("farzaneh_hall", aliases=["farzaneh"]),
        directions=Directions(
            'Farzaneh Hall houses the College of International Studies, \
            and is located just to the west of Nielsen Hall, on Elm Avenue.',

        )
    ),
    Building(
        names=AliasedName("fears_structural_engineering_lab", aliases=["fears lab", "fears"]),
        directions=Directions('Fears Lab is on south campus, to the east of Lloyd Noble Center.',
                              )
    ),
    Building(
        names=AliasedName("felgar_hall", aliases=["felgar"]),
        directions=Directions(
            'Felgar Hall is in the engineering quad across from the union, on the corner of Asp and Felgar. \
            It has a large concrete pyramid in front of its west entrance, and houses the Engineering Library.',

        )
    ),
    Building(
        names=AliasedName("fine_arts_center", aliases=["drama building"]),
        directions=Directions(
            'The Fine Arts Center is between the Physical Science Center and Fred Jones Museum of Art on Elm Avenue.',

        )
    ),
    Building(
        names=AliasedName("five_partners_place", aliases=["five partner place"]),
        directions=Directions('5 Partners Place is on south campus, near the weather center.',

                              )
    ),
    Building(
        names=AliasedName("forum_building", aliases=["forum"]),
        directions=Directions(
            'The Forum building is south of the dorms on Asp Avenue. \
            It\'s shaped like 3 identical prongs, with several other buildings and parking lots around it.',

        )
    ),
    Building(
        names=AliasedName("four_partners_place", aliases=["four partner place"]),
        directions=Directions('4 Partners Place is on south campus, near the weather center.',

                              )
    ),
    Building(
        names=AliasedName("fred_jones_junior_memorial_art_center", aliases=["art museum", "fred jones"]),
        directions=Directions(
            'The Fred Jones Museum of Art is on the corner of Elm and Boyd, on the northwest corner of campus. \
            It\'s across the street from Cattlet School of Music, and north of the Physical Science Center. You can enter it from the west entrance on Elm Avenue, next to the valkyrie statue.',

        )
    ),
    Building(
        names=AliasedName("gaylord_hall", aliases=["broadcasting building", "gaylord", "t. v. studio"]),
        directions=Directions(
            "Gaylord Hall houses the School of Journalism on the southeast side of the south oval. \
            It's the large building with a glass dome and electric news banner.",

        )
    ),
    Building(
        names=AliasedName("gaylord_family_oklahoma_memorial_stadium",
                          aliases=["oklahoma memorial stadium", "gaylord stadium", "football stadium", "stadium",
                                   "o. u. stadium"]),
        directions=Directions(
            'The stadium is between Asp and Jenkins Avenues, and between Brooks and Lindsey Streets. \
            It\'s on the east side of campus, between the new residential colleges and the Price College of Business.',

        )
    ),
    Building(
        names=AliasedName("george_lynn_cross_hall", aliases=["george lynn cross", "cross hall"]),
        directions=Directions(  # TODO: make this special directions from the union
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south until you can make a left on the second building down.',

        )
    ),
    Building(
        names=AliasedName("goddard_health_center", aliases=["health center", "goddard"]),
        directions=Directions(
            'Goddard Health Center is on the west side of campus, on a slight hill just across Elm. \
            It\'s just to the north of the parking lot across from Nielsen Hall.',

        )
    ),
    Building(
        names=AliasedName("gould_hall", aliases=["gould", "gold", "ghoul"]),
        directions=Directions(
            'Gould Hall is the Architecture building on the south oval, on the east side between Gaylord and Cross.',

        )
    ),
    Building(
        names=AliasedName("headington_hall", aliases=["headington"]),
        directions=Directions(
            'Headington Hall is the athletic dorm on the southeast corner of Lindsey and Jenkins. \
            You can enter it on the west side, between Einsteins Bagels and Qdoba.',

        )
    ),
    Building(
        names=AliasedName("headington_residential_college", aliases=["headington college"]),
        directions=Directions(
            'Headington Residential College is across the street from Headington Hall, \
            and is on the southwest corner of Jenkins and Lindsey. It\'s across the street from the south entrance to the stadium.',

        )
    ),
    Building(
        names=AliasedName("housing_offices", aliases=["housing office"]),
        directions=Directions('The Housing Offices are in Walker Tower, in the dorms.',

                              )
    ),
    Building(
        names=AliasedName("human_resources", aliases=["resources"]),
        directions=Directions(
            'I\'m sorry, I don\'t know where the offices for Human Resources are located. \
            Please see https://ou.edu for more information.',

        )
    ),
    Building(
        names=AliasedName("jacobs_field", aliases=["track and field", "outdoor track"]),
        directions=Directions(
            'Jacobs Field is the large track in by the practice facilities to the east of the football stadium.',

        )
    ),
    Building(
        names=AliasedName("jacobson_hall", aliases=["jacobson", "visitor center"]),
        directions=Directions(
            'Jacobson Hall is the Visitor Center on the northeast corner of the North Oval. \
            It\'s near the union and the parking garage.',

        )
    ),
    Building(
        names=AliasedName("jenkins_avenue_parking_facility", aliases=["jenkins parking garage", "new parking garage"]),
        directions=Directions(
            'The Jenkins Avenue parking facility is the parking garage south of Headington Residential College.',

        )
    ),
    Building(
        names=AliasedName("jimmie_austin_o_u_golf_course", aliases=["o. u. golf course", "golf course"]),
        directions=Directions(
            'The O. U. golf course is on Constitution street, to the east of Llyod Noble Center and Reeves Park.',

        )
    ),
    Building(
        names=AliasedName("jim_thorpe_multi_cultural_center",
                          aliases=["jim thorpe", "multi cultural center", "jim thorpe building",
                                   "multi cultural building"]),
        directions=Directions(
            'Walk past Crossroads and out the southern exit. \
            Make your way to the south oval and keep walking directly due south, even past Lindsey street. \
            Past the three dorms, you\'ll eventually run into a 3 pointed star shaped building. \
            The Jim Thorpe Multi-Cultural Center, also known as the Commons Restaurant, \
            will be located on the north west side of the block.',

        )
    ),
    Building(
        names=AliasedName("kaufman_hall", aliases=["kaufman", "cough men"]),
        directions=Directions(
            'Kaufman Hall is on the west side of the south oval, \
            between Nielsen Hall and the Rainbolt College of Education.',

        )
    ),
    Building(
        names=AliasedName("kraetteli_apartments", aliases=[]),
        directions=Directions('Kraetteli Apartments are across from Traditions East on the south side of Asp Avenue.',

                              )
    ),
    Building(
        names=AliasedName("lissa_and_cy_wagner_student_academic_services_center",
                          aliases=["wagner student center", "wagner center", "student academic services",
                                   "academic services"]),
        directions=Directions('Academic Services are located in Buchanan Hall, directly south of the union.',

                              )
    ),
    Building(
        names=AliasedName("lloyd_noble_center", aliases=["lloyd noble", "graduation", "free parking", "parking lot"]),
        directions=Directions(
            'Lloyd Noble Center is in the middle of the free parking at the southern end of Asp Avenue, \
            south of the dorms. You can get to it by bus from the campus depot.',

        )
    ),
    Building(
        names=AliasedName("l_dale_mitchell_baseball_park",
                          aliases=["baseball park", "baseball stadium", "baseball field", "baseball diamond",
                                   "baseball"]),
        directions=Directions(
            'The Mitchell Baseball Park is between Lloyd Noble Center and Traditions East on Asp Avenue.',

        )
    ),
    Building(
        names=AliasedName("mccarter_hall", aliases=["mccarter"]),
        directions=Directions(
            'McCarter Hall is in the northwest corner of the forum building\'s complex, just south of the dorms.',

        )
    ),
    Building(
        names=AliasedName("michael_f_price_college_of_business",
                          aliases=["price college of business", "college of business", "business college", "price"]),
        directions=Directions(
            'Price College of Business is in the middle of campus, \
            to the east of Bizzell library and just south of the union.',

        )
    ),
    Building(
        names=AliasedName("monnet_hall", aliases=["monnet"]),
        directions=Directions(
            'Monnet Hall is in the northwest corner of the north oval, amidst the fine art buildings.',
        )
    ),
    Building(
        names=AliasedName("mosier_indoor_athletic_facility", aliases=["indoor athletic facility", "indoor track"]),
        directions=Directions(
            'Mosier Indoor Athletic Facility is in southwest corner of the athletics practice complex \
             between the duck pond and the stadium. \
             It\'s the closest building to the duck pond in that area.',

        )
    ),
    Building(
        names=AliasedName("national_weather_center", aliases=["weather center", "weather building"]),
        directions=Directions(
            'The Weather Center is on the southeast corner of campus, at the intersection of Jenkins and Highway 9.',

        )
    ),
    Building(
        names=AliasedName("newman_hall", aliases=["newman"]),
        directions=Directions(
            'Newman Hall is far to the east of campus on Boyd Street, just to the north of Logan Apartments. \
            It\'s two blocks west of Catlett Hall.',

        )
    ),
    Building(
        names=AliasedName("nielsen_hall", aliases=["physics building", "nielsen", "kneel sun"]),
        directions=Directions(
            'Nielsen Hall is the physics building with the huge staircase on the northwest of the south oval.',

        )
    ),
    Building(
        names=AliasedName("norman_fire_department_number_3", aliases=["fire department number three"]),
        directions=Directions(
            'Norman Fire Department 3 is on Constitution Street on south campus, near Fears Lab, Llyod Noble Center, \
            and the O. U. Golf Course.',

        )
    ),
    Building(
        names=AliasedName("nuclear_engineering_laboratory", aliases=["nuclear lab", "nuclear laboratory"]),
        directions=Directions('The Nuclear Engineering Laboratory is across Asp Avenue from the union.',

                              )
    ),
    Building(
        names=AliasedName("observatory", aliases=["telescope", "old observatory"]),
        directions=Directions('The old observatory is across Asp Avenue from Cate Center, near the dorms and the gym.',

                              )
    ),
    Building(
        names=AliasedName("oklahoma_memorial_union", aliases=["union", "student union"]),
        directions=Directions('The Union is in the center of campus, east of the library, on Asp Avenue.',

                              )
    ),
    # Building(
    #     names=AliasedName("old_faculty_club", aliases=["old faculty building"]),
    #     directions=Directions(
    #     )
    # ),
    Building(
        names=AliasedName("one_partners_place", aliases=["south campus", "one partner place"]),
        directions=Directions('1 Partners Place is on south campus, near the Weather Center and Lloyd Noble Center.',

                              )
    ),
    Building(
        names=AliasedName("o_u_police_department", aliases=["o. u. p. d.", "police department"]),
        directions=Directions(
            'The O. U. P. D. office is in Cate Center, south of the Cate Food Courts. \
            In an emergency, you can request a police officer \
            by pressing the button on any blue safety pole around campus.',

        )
    ),
    Building(
        names=AliasedName("o_u_traditions_square_east", aliases=["traditions east", "traditions"]),
        directions=Directions(
            'O. U. Traditions East is south of the dorms on Asp Avenue, near the Sam Noble Museum of Natural History.',

        )
    ),
    Building(
        names=AliasedName("o_u_traditions_square_west", aliases=["traditions west"]),
        directions=Directions(
            'O. U. Traditions West is south of the Sam Noble Museum of Natural History\
             and west of Lloyd Noble Center, on Elm Avenue. \
             You can reach it by bus from the campus depot.',

        )
    ),
    Building(
        names=AliasedName("parking_services", aliases=["parking passes"]),
        directions=Directions('Parking Services are in Robertson Hall, southwest of Nielsen and Farzaneh Halls',

                              )
    ),
    Building(
        names=AliasedName("physical_sciences_center", aliases=["physical science building", "blender"]),
        directions=Directions(
            'The Physical Science Center is the tall, grey building north of the library. \
            It\'s on Elm Avenue, to the west of the north oval.',

        )
    ),
    Building(
        names=AliasedName("reynolds_performing_arts_center", aliases=["performing arts center"]),
        directions=Directions(
            'The Performing Arts Center is building with the big wooden doors \
            to the north of the Physical Science Center on the north oval.',

        )
    ),
    Building(
        names=AliasedName("richards_hall", aliases=["richards", "zoology", "zoology building"]),
        directions=Directions(
            'Richards Hall is at the northeast corner of the south oval, \
             between Price College of Business and George Lynn Cross Hall.',

        )
    ),
    Building(
        names=AliasedName("robertson_hall", aliases=["robertson"]),
        directions=Directions(
            'Robertson Hall, which houses the Graduate Office and Parking Services, \
            is to the southwest of Nielsen and Farzaneh Halls.',

        )
    ),
    Building(
        names=AliasedName("rupel_j_jones_theatre",
                          aliases=["drama theatre", "rupel jones", "jones", "theatre", "theater"]),
        directions=Directions(
            'The Rupel J. Jones Theatre is between the Fred Jones Museum of Art and Physical Science Center. \
            It\'s across Elm Avenue from Cattlet School of Music and the parking garage.',

        )
    ),
    Building(
        names=AliasedName("sam_noble_oklahoma_museum_of_natural_history",
                          aliases=["sam noble museum", "sam noble", "museum of natural history"]),
        directions=Directions(
            'The Sam Noble Oklahoma Museum of Natural History is south of the Law Building, \
            between Traditions East and West. \
            You can reach it from Asp Avenue or Elm Street.',

        )
    ),
    Building(
        names=AliasedName("sarkeys_energy_center", aliases=["sarkeys", "energy center"]),
        directions=Directions(
            'Sarkeys Energy Center is the massive red tower on the northeast corner of campus, \
            at the intersection of Jenkins and Boyd.',

        )
    ),
    Building(
        names=AliasedName("sarkeys_physical_fitness_center",
                          aliases=["huffman", "gym", "physical fitness center", "o. u. gym", "huff man"]),
        directions=Directions(
            'The Sarkeys Physical Science Center, also called the huff, is just across Asp Avenue from the dorms.',

        )
    ),
    Building(
        names=AliasedName("science_hall", aliases=["science building", "old science building"]),
        directions=Directions(
            'The Old Science Hall is on the southwest corner of the north oval, \
            by Bizzell Library and the Physical Science Center.',

        )
    ),
    Building(
        names=AliasedName("sells_swim_complex", aliases=["sells complex", "swim complex", "o. u. pool", "pool"]),
        directions=Directions(
            'The Sells Swim Complex is across Asp Avenue from the Forum Building, south of the dorms.',

        )
    ),
    Building(
        names=AliasedName("sooner_cottage_suites", aliases=["sooner suites", "cottage suites", "sooner cottages"]),
        directions=Directions(
            'Sooner Cottage Suites are just to the south of the dorms, between Couch Restaurants and the Law Building.',

        )
    ),
    Building(
        names=AliasedName("stephenson_life_sciences_research_center",
                          aliases=["life sciences", "life sciences research center"]),
        directions=Directions('Stepheson Life Science Research Center is on south campus, near Lloyd Noble Center.',

                              )
    ),
    Building(
        names=AliasedName("stephenson_research_and_technology_center",
                          aliases=["research and technology center", "stephenson", "stepheson hall", "stepheson center",
                                   "technology center"]),
        directions=Directions('Stepheson Research and Technology Center is on south campus, near the weather center.',

                              )
    ),
    Building(
        names=AliasedName("sutton_hall", aliases=["sutton"]),
        directions=Directions('Sutton Hall is directly south of the Physical Science Center.',

                              )
    ),
    # Building(
    #     names=AliasedName("t_howard_mccasland_field_house", aliases=["mccasland house", "field house"]),
    #     directions=Directions(
    #     )
    # ),
    # Building(
    #     names=AliasedName("theta_m_dempsey_transportation_operations_center",
    #                       aliases= ["dempsey center", "transporation operations center","transportation center",
    #                                "transportation building"]),
    #     directions=Directions(
    #     )

    # ),
    Building(
        names=AliasedName("three_partners_place", aliases=["innovation hub", "three partner place"]),
        directions=Directions('3 Partners Place is on south campus, near the weather center.',

                              )
    ),
    Building(
        names=AliasedName("two_partners_place", aliases=["two partner place"]),
        directions=Directions('2 Partners Place is on south campus, near the weather center.',

                              )
    ),
    Building(
        names=AliasedName("university_book_exchange", aliases=["book store", "text book store", "book exchange"]),
        directions=Directions('The university book store is near the stadium, under the asp avenue parking facility.',

                              )
    ),
    Building(
        names=AliasedName("university_of_oklahoma_foundation", aliases=["oklahoma foundation"]),
        directions=Directions(
            'The University of Oklahoma foundation is between Traditions East and the Forum Building on Asp Avenue.',

        )
    ),
    # Building(
    #     names=AliasedName("viersen_gymnastics_center",
    #                       aliases= ["gymnastics center", "viersen center", "viersen building",
    #                                "gymnastics building", "gymnastics"]),
    #     directions=Directions(
    #     )
    # ),
    Building(
        names=AliasedName("walker_tower",
                          aliases=["walker", "walker dorms", "walker tower", "walker adams mall", "dorms",
                                   "dorm towers"]),
        directions=Directions(
            'Walker Tower is the northeast dorm tower, south of Lindsey Street and Cate Center. \
            You can find the convenience store XCetera inside.',

        )
    ),
    Building(
        names=AliasedName("whitehand_hall", aliases=["whitehand", "white hand", "white hand hall"]),
        directions=Directions('Whitehand Hall is across the street from the north oval, on Boyd Street.')
    )
]
