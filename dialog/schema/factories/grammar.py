from dialog.schema.elements import Grammar

__author__ = 'robdefeo'


class GenericGrammar:
    @staticmethod
    def create_sorry():
        return Grammar(
            [
                "sorry",
                "apologize",
                "I am sorry",
                "I apologise",
                "I apologize",
                "apologies",
                "my apology",
                "my apologies",
                "so sorry",
                "very sorry",
                "extremely sorry",
                "extremely apologetic",
                "soz",
                "sozz",
                "so soz",
                "so sozz"
            ]
        )

    @staticmethod
    def create_hello():
        return Grammar(
            [
                "Hello",
                "Hi",
                "Hola",
                "Howdy",
                "Hiya",
                "Hey",
                "Heya",
                "yello",
                "aloha",
                "hi there",
                "hey there"
            ]
        )

    @staticmethod
    def create_ok():
        return Grammar(
            [

                "okay",
                "ok"
            ]
        )

    @staticmethod
    def create_ok_thanks():
        return Grammar(
            [

                "okay",
                "ok",
                "thanks",
                "thank you",
                "ok thanks",
                "ok thank you",
                "okay thanks",
                "okay thank you",
                "all right",
                "alright",
                "great",
                "cool",
                "aww",
                "awww",
                "oh",
                "oh okay",
                "oh ok",
                "ah",
                "ah okay",
                "ah ok",
                "got it",
                "gotcha"
            ]
        )

    @staticmethod
    def create_yes_goodbye():
        return Grammar(
            [
                "Goodbye",
                "bye bye",
                "bye now",
                "bye",
                "later",
                "laters",
                "see you later",
                "see you",
                "see ya later",
                "see ya",
                "cya",
                "au revoir",
                "good night",
                "good day"
            ]
        )

    @staticmethod
    def create_yes_full():
        return Grammar(
            [
                "yes",
                "yep",
                "yup",
                "yeah",
                "yeh",
                "y",
                "that's right",
                "sure",
                "yes thanks",
                "yes thank you",
                "yes please",
                "yah",
                "ya",
                "for sure",
                "fo shizzle",
                "fo shiz",
                "yeppers",
                "you betcha",
                "you bet",
                "you bet ya",
                "certainly"
            ]
        )

    @staticmethod
    def create_no_full():
        return Grammar(
            [
                "no",
                "n",
                "nope",
                "no way",
                "not really",
                "nah",
                "no thanks",
                "no thank you"
            ]
        )

    @staticmethod
    def create_yes():
        return Grammar(
            [
                "Yes",
                "Yes.",
                "$ yes"
            ]
        )

    @staticmethod
    def create_no():
        return Grammar(
            [
                "No"
            ]
        )

    @staticmethod
    def create_yes_okay():
        return Grammar(
            [
                "Yes",
                "Yes.",
                "Okay",
                "Ok",
                "$ yes"
            ]
        )


class ProfileGrammar:
    @staticmethod
    def create_my_name_is_dynamic_data():
        return Grammar(
            [
                "My name is",
                "$ my name is (DYNAMIC_DATA)={User_Name}",
                "$ I am (DYNAMIC_DATA)={User_Name}",
                "$ I'm (DYNAMIC_DATA)={User_Name}",
                "$ called (DYNAMIC_DATA)={User_Name}",
                "$ call me (DYNAMIC_DATA)={User_Name}",
                "$ known as (DYNAMIC_DATA)={User_Name}",
                "$ (DYNAMIC_DATA)={User_Name}"
            ]
        ).create()


class FeelingGrammar:
    @staticmethod
    def create_preliminaries():
        return Grammar(
            [
                "Preliminaries",
                "$ what do you know",
                "$ what can you do",
                "$ what can I do",
                "$ what can you tell",
                "$ what kind of",
                "$ what else do you know",
                "$ what do you have information",
                "$ do you know",
                "$ can you",
                "$ do you have information",
                "$ can I"
            ]
        ).create()

    @staticmethod
    def create_not_so_good():
        return Grammar(
            [
                "Not so good",
                "$ not * good",
                "$ not * well",
                "$ no * good",
                "$ not * nice"
            ]
        ).create()

    @staticmethod
    def create_feeling_great():
        return Grammar(
            [
                "Great",
                "$ great",
                "$ excellent",
                "$ outstanding",
                "$ fabulous",
                "$ terrific",
                "$ fantastic",
                "$ awesome"
            ]
        ).create()

    @staticmethod
    def create_feeling_fine():
        return Grammar(
            [
                "Fine",
                "$ good",
                "$ fine",
                "$ well",
                "$ all right",
                "$ nice"
            ]
        ).create()

    @staticmethod
    def create_feeling_bad():
        return Grammar(
            [
                "Bad",
                "$ terrible",
                "$ awful",
                "$ worst",
                "$ bored",
                "$ sad",
                "$ tired",
                "$ hungry",
                "$ thirsty",
                "$ bad",
                "$ badly",
                "$ poor",
                "$ poorly",
                "$ crap",
                "$ crappy"
            ]
        ).create()
