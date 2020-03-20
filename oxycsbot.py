#!/usr/bin/env python3
"""A simple chatbot that utilizes Cognitive Behavioral Therapy to help first-generation students
with distressing thoughts of their first year of college."""

from chatbot import ChatBot


class OxyCSBot(ChatBot):
    """An amazingggggggg chatbot that directs students to office hours of CS professors."""

    "CD = Cognitive Distortion"

    STATES = [
        'waiting',
        'specific_emotion',
        'unknown_emotion',
        'unknown_CD',
        'specific_CD',
        'challenge_emotion',
    ]

    TAGS = {
        # intent
        'help': 'help',
        'feel': 'help',
        '': 'hello',
        'hello':'hello',
        'hi':'hello',

        # emotions
        'anxiety': 'anxious',
        'anxious': 'anxiety',
        'homesick': 'homesick',
        'isolated': 'isolation',
        'isolation': 'isolated',
        'worthless': 'worthless',
        'worried': 'worry',
        'worry': 'worried',
        'sad': 'sad',
        'depressed': 'depressed',
        'scared': 'scared',
        'tired': 'tired',
        'annoyed': 'annoyed',
        'angry': 'angry',
        'unprepared': 'unprepared',
        'emptiness': 'empty',
        'empty': 'emptiness',
        'lost': 'lost',

        #cogntive distortions
        'filtering': 'filtering',
        'polarized thinking': 'polarized thinking',
        'control fallacies': 'control fallacies',
        'fallacy of fallacies': 'fallacy of fallacies',
        'overgeneralization': 'overgeneralization',
        'emotional reasoning': 'emotional reasoning',
        'fallacy of change': 'fallacy of change',
        'shoulds': 'shoulds',
        'catastrophizing': 'catastrophizing',
        'heavens reward fallacy': 'heavens reward fallacy',
        'always being right': 'always being right',
        'personalization': 'personalization',
        'jump to conclusions': 'jump to conclusions',
        'blaming': 'blaming',
        'global labeling': 'global labeling',

        # generic
        'thanks': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'yes': 'yes',
        'yep': 'yes',
        'no': 'no',
        'nope': 'no',

        #scenarios
        'roommate': 'roommate',
        'homesick': 'homesick',
        'home': 'home',
        'lost': 'lost',
        'academic': 'academic',
        'hard': 'hard',
        'alone': 'alone',
    }

    EMOTIONS = [
        'anxiety',
        'homesick',
        'isolated',
        'worthless',
        'worried',
        'sad',
        'scared',
        'tired',
        'annoyed',
        'angry',
        'unprepared',
        'empty',
        'lost'
    ]

    SCENARIOS = [
        'roommate',
        'homesick',
        'home',
        'lost',
        'academic',
        'hard',
        'alone',
    ]

    def __init__(self):
        """Initialize the OxyCSBot.

        The `emotion` member variable stores whether the target emotion has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.emotion = None

    def get_emotion(self, emotion):
        """Find the office hours of a professor.

        Arguments:
            professor (str): The professor of interest.

        Returns:
            str: The office hours of that professor.
        """
        responses = {
            'bad': ' ',
            'hsing-hau': 'MW 3:30-4:30pm; F 11:45am-12:45pm',
            'jeff': 'W 4-5pm; Th 12:50-1:50pm; F 4-5pm and partyoclock',
            'justin': 'T 3-4pm; W 2-3pm; F 4-5pm',
            'kathryn': 'MF 4-5:30pm',
            'umit': 'M 3-5pm; W 10am-noon, 3-5pm',
            'jasmine': 'party oclock',
        }
        return responses[emotion]




    def get_office(self, professor):
        """Find the office of a professor.

        Arguments:
            professor (str): The professor of interest.

        Returns:
            str: The office of that professor.
        """
        office = {
            'celia': 'Swan 232',
            'hsing-hau': 'Swan 302',
            'jeff': 'Fowler 321',
            'justin': 'Swan B102',
            'kathryn': 'Swan B101',
            'umit': 'Swan 226',
        }
        return office[professor]

    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.emotion = None
        self.greet = None
        if 'hello' in tags:
            return self.greet('hello')
        if 'help' in tags:
            for emotion in self.EMOTIONS:
                if emotion in tags:
                    self.emotion = emotion
                    return self.go_to_state('specific_emotion')
            return self.go_to_state('unknown_emotion')
        elif 'thanks' in tags:
            return self.finish('thanks')
        else:
            return self.finish('confused')

    # "specific_faculty" state functions

    def on_enter_specific_emotion(self):
        """Send a message when entering the "specific_faculty" state."""
        response = [
            f"I'm here to listen. Can you explain the time when you felt {self.emotion}?"
            # f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            # 'Do you know where their office is?',
        ]
        return response

    def respond_from_specific_emotion(self, message, tags):
        """Decide what state to go to from the "specific_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for scenario in self.SCENARIOS:
            if scenario in tags:
                self.scenario = scenario
                return self.go_to_state('specific_scenario')

        return self.finish_confused()


        # if '' in tags:
        #     return self.finish('success')
        # else:
        #     return self.finish('location')

    # "unknown_faculty" state functions

    def on_enter_specific_scenario(self):
        """Send a message when entering the "specific_faculty" state."""
        response = [
            f" What makes you believe that {self.scenario}?"
            # f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            # 'Do you know where their office is?',
        ]
        return response

    def on_enter_unknown_emotion(self):
        """Send a message when entering the "unknown_faculty" state."""
        return "Could you explain more of what you are feeling?"

    def respond_from_unknown_emotion(self, message, tags):
        """Decide what state to go to from the "unknown_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for emotion in self.EMOTION:
            if emotion in tags:
                self.emotion = emotion
                return self.go_to_state('specific_emotion')
        return self.go_to_state('unrecognized_emotion')

    # "unrecognized_faculty" state functions

    def on_enter_unrecognized_faculty(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "I'm not sure I understand - are you looking for",
            "Celia, Hsing-hau, Jeff, Justin, Kathryn, or Umit?",
        ])

    def respond_from_unrecognized_faculty(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for professor in self.PROFESSORS:
            if professor in tags:
                self.professor = professor
                return self.go_to_state('specific_faculty')
        return self.finish('fail')

    # "finish" functions

    def greet_hello(self):
        """Send a message and go to the default state."""
        return "Hello! I'm an O-team leader and I will be helping you through this rough patch." \
               "I'll be using Cognitive Behavioral Therapy to help navigate your feelings."

    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. You can ask me about office hours though!"


    def finish_location(self):
        """Send a message and go to the default state."""
        return f"{self.professor.capitalize()}'s office is in {self.get_office(self.professor)}"

    def finish_success(self):
        """Send a message and go to the default state."""
        return 'Great, let me know if you need anything else!'

    def finish_fail(self):
        """Send a message and go to the default state."""
        return "I've tried my best but I still don't understand. Maybe try asking other students?"

    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "You're welcome!"


if __name__ == '__main__':
    OxyCSBot().chat()
