from dialog.elements import Concept, Grammar, Folder
from dialog.schema.factories.concepts import StyleConcept, ColorConcept
from dialog.schema.factories.folder.cdh import CDHFolder
from dialog.schema.factories.grammar import GenericGrammar


class ConceptFolder:
    @staticmethod
    def create():
        return Folder(
            label="Concepts",
            children=[
                StyleConcept.create(),
                ColorConcept.create(),
                CDHFolder.create(),
                Concept(grammar=GenericGrammar.create_hello()),
                Concept(grammar=GenericGrammar.create_yes_goodbye()),
                Concept(grammar=GenericGrammar.create_ok_thanks()),
                Concept(grammar=GenericGrammar.create_yes_full()),
                Concept(grammar=GenericGrammar.no()),
                Concept(grammar=GenericGrammar.create_haha()),
                Concept(grammar=GenericGrammar.create_sorry()),
                Concept(grammar=GenericGrammar.create_you()),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "movie",
                            "movies",
                            "film",
                            "films",
                            "flick",
                            "flicks"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "theater",
                            "theaters",
                            "theatre",
                            "theatres",
                            "cinema",
                            "cinemas"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "showtime",
                            "showtimes",
                            "show time",
                            "show times",
                            "movie time",
                            "movie times"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "dining",
                            "restaurant",
                            "restaurants",
                            "place to eat",
                            "places to eat",
                            "diner",
                            "diners",
                            "cafe",
                            "cafes",
                            "cafeteria",
                            "cafeterias",
                            "Bar",
                            "Bars",
                            "Pub",
                            "Pubs",
                            "Tavern",
                            "Taverns",
                            "Brewery",
                            "Breweries",
                            "somewhere to eat",
                            "eatery",
                            "place to dine",
                            "somewhere nice to eat",
                            "eateries",
                            "places to dine",
                            "bistro",
                            "a bistro",
                            "bistros",
                            "coffee shop",
                            "coffee shops",
                            "coffee place",
                            "coffee places",
                            "eating house",
                            "eating houses",
                            "snack bar",
                            "snack bars",
                            "juice bar",
                            "juice bars",
                            "health food shop",
                            "fast food outlet",
                            "fast food shop",
                            "fast food outlets",
                            "fast food shops",
                            "food court",
                            "food courts",
                            "food mall",
                            "food malls"
                        ]
                    ),
                    _id="concept_place_to_eat"
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "weather",
                            "Rain",
                            "Raining",
                            "Snow",
                            "Snowing",
                            "Sunny",
                            "Cloudy",
                            "Sleet",
                            "Freezing Rain",
                            "Windy",
                            "Tornado",
                            "Hurricane"
                        ]
                    ),
                    _id="concept_weather"
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "traffic",
                            "Traffic conditions",
                            "Driving conditions",
                            "Road conditions",
                            "Streets",
                            "Roads",
                            "Freeways",
                            "Highways",
                            "Driving",
                            "Rush hour",
                            "Bus",
                            "Buses",
                            "Train",
                            "Trains",
                            "Car",
                            "Cars",
                            "Automobile",
                            "Automobiles",
                            "Bicycle",
                            "Bicycles",
                            "Bike",
                            "Bikes",
                            "Motorcycle",
                            "Motorcycles",
                            "Walking",
                            "Driving",
                            "Pedestrian"
                        ]
                    ),
                    _id="concept_2456118"
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "what is",
                            "what's"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Review",
                            "Reviews",
                            "Critique",
                            "Critiques",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Ratings",
                            "Rating",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "it",
                            "that",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "family-friendly",
                            "family",
                            "child",
                            "children",
                            "childrens",
                            "children's",
                            "kiddy",
                            "kids",
                            "kid's",
                            "kid",
                            "family friendly",
                            "family safe",
                            "kid friendly",
                            "child friendly",
                            "safe for kids",
                            "kid safe",
                            "suitable for children",
                            "suitable for kids",
                            "suitable for a child",
                            "suitable for a kid",
                            "child appropriate",
                            "appropriate for children",
                            "not adult",
                            "for families",
                            "for a family",
                            "no sex",
                            "no violence",
                            "clean"
                        ]
                    ),
                    _id="concept_family_friendly"
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "near me",
                            "by me",
                            "my area",
                            "close to me",
                            "close by",
                            "nearby",
                            "in the neighborhood",
                            "local",
                            "locally",
                            "fairly close",
                            "close to us",
                            "near to us",
                            "short drive",
                            "short walk",
                            "a short drive",
                            "a short walk",
                            "close",
                            "near",
                            "around the corner",
                            "just around the corner",
                            "short distance",
                            "a short distance",
                            "close at hand",
                            "short distance awat",
                            "a short distance away",
                            "walking distance",
                            "within walking distance",
                            "not a long distance",
                            "not far",
                            "not too far",
                            "not far away",
                            "not too far away",
                            "in my area",
                            "in the city",
                            "my zipcode",
                            "dowtown"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Adult",
                            "Adults Only",
                            "NC 17",
                            "NC-17",
                            "NC17",
                            "NC 17 rated",
                            "NC-17 rated",
                            "NC-17-rated",
                            "NC 17-rated",
                            "NC17 rated",
                            "NC17-rated",
                            "X",
                            "X-rated",
                            "X rated",
                            "XXX",
                            "XXX-rated",
                            "XXX rated",
                            "Triple X",
                            "Triple X-rated",
                            "Triple X rated",
                            "NC seventeen",
                            "NC-seventeen"
                        ]
                    ),
                    _id="concept_porn"
                )
            ]
        )
