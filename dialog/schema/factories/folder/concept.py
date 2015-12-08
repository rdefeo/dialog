from dialog.schema.elements import Concept, Grammar
from dialog.schema.factories.folder.cdh import CDHFolder
from dialog.schema.factories.folder.genre import GenreFolder
from dialog.schema.factories.folder.style import StyleFolder
from dialog.schema.factories.grammar import GenericGrammar


class ConceptFolder:
    @staticmethod
    def create():
        return {
            "@label": "Concepts",
            (0, "folder"): [
                StyleFolder.create(),
                GenreFolder.create(),
                CDHFolder.create()
            ],
            (1, "concept"): [
                Concept(grammar=GenericGrammar.create_hello()),
                Concept(grammar=GenericGrammar.create_yes_goodbye()),
                Concept(grammar=GenericGrammar.create_ok_thanks()),
                Concept(grammar=GenericGrammar.create_yes_full()),
                Concept(grammar=GenericGrammar.create_no()),
                Concept(grammar=GenericGrammar.create_haha()),
                Concept(grammar=GenericGrammar.create_sorry()),
                Concept(grammar=GenericGrammar.create_you()),
                {
                    "grammar": {
                        "item": [
                            "movie",
                            "movies",
                            "film",
                            "films",
                            "flick",
                            "flicks"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "theater",
                            "theaters",
                            "theatre",
                            "theatres",
                            "cinema",
                            "cinemas"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "showtime",
                            "showtimes",
                            "show time",
                            "show times",
                            "movie time",
                            "movie times"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
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
                    },
                    "@id": "concept_place_to_eat"
                },
                {
                    "grammar": {
                        "item": [
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
                    },
                    "@id": "concept_weather"
                },
                {
                    "grammar": {
                        "item": [
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
                    },
                    "@id": "concept_2456118"
                },
                {
                    "grammar": {
                        "item": [
                            "what is",
                            "what's"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "Review",
                            "Reviews",
                            "Critique",
                            "Critiques",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "Ratings",
                            "Rating",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "it",
                            "that"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
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
                    },
                    "@id": "concept_family_friendly"
                },
                {
                    "grammar": {
                        "item": [
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
                    }
                },
                {
                    "grammar": {
                        "item": [
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
                    },
                    "@id": "concept_porn"
                }
            ]
        }
