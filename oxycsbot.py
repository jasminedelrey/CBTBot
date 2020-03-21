#!/usr/bin/env python3
"""A simple chatbot that utilizes Cognitive Behavioral Therapy to help first-generation students
with distressing thoughts of their first year of college."""

from chatbot import ChatBot


class OxyCSBot(ChatBot):
    """A chatbot that uses CBT techniques to unravel discomforting thoughts."""

    "CD = Cognitive Distortion"

    STATES = [
        'waiting',
        'specific_emotion',
        'unknown_emotion',
        'specific_scenario',
        'unknown_scenario',
        'unknown_CD',
        'specific_CD',
        'challenge_emotion',
    ]

    TAGS = {
        # intent
        'help': 'help',
        'feel': 'help',
        '': 'help',
        'hello':'help',
        'hi':'help',

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
        'roommate': 'scenario',
        'homesick': 'scenario',
        'home': 'scenario',
        'lost': 'scenario',
        'academic': 'scenario',
        'hard': 'scenario',
        'alone': 'scenario',
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

    CORE_BELIEFS = {
        'not enough',
        'not prepared',

    }

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
            emotion (str): The emotion of interest.

        Returns:
            str: The office hours of that professor.
        """
        responses = {
            'anxiety': "I'm sorry that you feel this way. Do you feel anything physically when you feel that way?",
            'homesick': "What about school makes you feel this way?",
            'isolated': "What do you do when you feel this way?",
            'worthless': "What makes you feel this way?",
            'worried': "What are some things that make you worry?",
            'sad': "What do you think of when you feel this way?",
            'scared': "What are some core beliefs that make you feel this way?",
            'tired': "What is part of your schedule that makes you feel this way?",
            'annoyed': "What are some things that makes you feel this way?",
            'angry': "What makes you feel this way?",
            'unprepared': "What makes you feel this way?",
            'empty': "What makes you feel this way?",
            'lost': "What makes you feel this way?",
            'bad': "What makes you feel this way?",

        }
        return responses[emotion]


    # def get_cd(self, core_belief):
    #     responses = {
    #         'always': "Let's challenge that notion of 'always'. But it's normal to feel this way. Can you think of times "
    #         'reject':
    #         'hopeless':
    #         'not enough':
    #         'dumb':
    #         'never':
    #         'bad':
    #     }

        # return responses[core_belief]

    # def get_school_help(self, cd):
    #     responses = {
    #
    #     }
    #     return responses[]


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
        self.finish('hello')
        if 'help' in tags:
            for emotion in self.EMOTIONS:
                if emotion in tags:
                    self.emotion = emotion
                    return self.go_to_state('specific_emotion')
            return self.go_to_state('unknown_emotion')
        else:
            return self.finish('confused')

    # "specific_faculty" state functions

    def on_enter_specific_emotion(self):
        """Send a message when entering the "specific_faculty" state."""
        response = [
            f"{self.get_emotion(self.emotion)}"
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
        if 'scenario' in tags:
            for scenario in self.SCENARIOS:
                if scenario in tags:
                    self.scenario = scenario
                    return self.go_to_state('specific_scenario')

        return self.finish_confused()


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
        return self.go_to_state('unknown_emotion')

    # "unrecognized_faculty" state functions

    def on_enter_specific_scenario(self):
        """Send a message when entering the "specific_faculty" state."""
        response = '\n'.join([
            f"Ok. It is good to understand a specific time that you felt this way.",
            'Lets dive into what makes you feel this way. '
            'What core beliefs are instilled in these times in your life?'
            # f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            # 'Do you know where their office is?',
        ])
        return response

    def respond_from_specific_scenario(self, message, tags):
        for scenario in self.SCENARIOS:
            if scenario in tags:
                return self.go_to_state('specific_cb')
        return self.go_to_state('unknown_cb')


    def on_enter_specific_cb(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "I'm not sure I understand - are you looking for",
            "Celia, Hsing-hau, Jeff, Justin, Kathryn, or Umit?",
        ])

    def respond_from_specific_cb(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for emotion in self.EMOTIONS:
            if emotion in tags:
                self.emotion = emotion
                return self.go_to_state('specific_emotion')
        return self.finish('emotion')

    def on_enter_specific_cd(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "I'm not sure I understand - are you looking for",
            "Celia, Hsing-hau, Jeff, Justin, Kathryn, or Umit?",
        ])

    def respond_from_specific_cd(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for emotion in self.EMOTIONS:
            if emotion in tags:
                self.emotion = emotion
                return self.go_to_state('specific_emotion')
        return self.finish('emotion')

    # "finish" functions

    def finish_hello(self):
        """Send a message and go to the default state."""
        return "Hello! I'm an O-team leader and I will be helping you through this rough patch." \
               "I'll be using Cognitive Behavioral Therapy to help navigate your feelings."

    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. You can ask me about office hours though!"


    def finish_location(self):
        """Send a message and go to the default state."""
        return "I am finished."
        # return f"{self.professor.capitalize()}'s office is in {self.get_office(self.professor)}"

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
