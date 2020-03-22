#!/usr/bin/env python3
"""A simple chatbot that utilizes Cognitive Behavioral Therapy to help first-generation students
with distressing thoughts of their first year of college."""


from chatbot import ChatBot


class CBTBot(ChatBot):
    """A chatbot that uses CBT techniques to unravel discomforting thoughts."""

    "CD = Cognitive Distortion"

    STATES = [
        'waiting',
        'specific_emotion',
        'unknown_emotion',
        'specific_scenario',
        'unknown_scenario',
        'unknown_cb',
        'specific_cb',
        'challenge_emotion',
    ]

    TAGS = {
        # intent
        'help': 'help',
        'feel': 'help',
        'am': 'help',
        '': 'help',
        'hello':'help',
        'hi':'help',

        'roommate': 'moment',
        'roommates': 'moment',
        'homesick': 'moment',
        'home': 'moment',
        'lost': 'moment',
        'academic': 'moment',
        'hard': 'moment',
        'alone': 'moment',

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
        'roommates': 'roommate',
        'room mate': 'roommate',
        'roommate': 'roommate',
        'living': 'roommate',
        'homesick': 'homesick',
        'home': 'home',
        'lost': 'lost',
        'academic': 'academic',
        'hard': 'hard',
        'alone': 'alone',
        'imposter': 'imposter',
        'not smart': 'imposter',
        'dumb': 'imposter',
        'deserve': 'imposter',

        # core beliefs
        'not enough': 'not enough',
        'not prepared': 'not prepared',
        'not enough': 'not enough',
        'not prepared':'not prepared',
        'not good enough':'not good enough',
        'undeserving':'undeserving',
        'unlovable':'unlovable',
        'abnormal': 'abnormal',
        'failure': 'failure',


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
        'class',
        'home',
        'lost',
        'academic',
        'hard',


    ]

    CORE_BELIEFS = {
        'not enough',
        'not prepared',
        'not good enough',
        'undeserving',
        'unlovable',
        'abnormal',
        'failure',

    }

    def __init__(self):
        """Initialize the OxyCSBot.

        The `emotion` member variable stores whether the target emotion has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.emotion = None
        self.scenario = None
        self.cb = None
        self.cd = None

    def get_emotion(self, emotion):
        """Find the office hours of a professor.

        Arguments:
            emotion (str): The emotion of interest.

        Returns:
            str: The office hours of that professor.
        """
        responses = {
            'anxiety': 'Im sorry that you feel this way. Can you give us an example of when you felt anxious?',
            'homesick': "Being away from your support system is challenging. What about campus life makes you miss home?",
            'isolated': "I hear your point; college is very different from what we're used to. What are times that you feel isolated?",
            'worthless': "I know that this isn't an easy topic. I appreciate you for sharing. What makes you feel this way? ",
            'worried': "This is a stressful time for many students. What makes you worry?",
            'sad': "Why?",
            'scared': "I want you to know that your feelings are valid. What makes you scared?",
            'tired': "There are many adjustments when transitioning to college that can make people feel worn down. Do you find yourself constantly tired or only after certain events?",
            'annoyed': "What are some things that makes you feel this way?",
            'angry': "It is understandable to have moments of anger, but remember that it is healthy to get rid of this anger. What makes you angered?",
            'unprepared': '\n'.join
                    ("Transitioning to college can be a big step up, so it is common to feel like you are not prepared. "
                    "Are there certain times that make you feel unprepared or do you always feel this way?"),
            'empty': "Remember that you are an incredible human being full of unique experiences that make you ‘you’. Have you felt this way before or did something happen that made you feel empty?",
            'lost': "You don’t need to have every aspect of your life planned out, remember that college is a time of exploration and discovery. What makes you feel lost?",
            'bad': "It is normal to feel bad sometimes, but remember to not let it define your day. Did a certain event happen that made you feel bad?",
        }
        return responses[emotion]

    def get_scenario(self, scenario):
        """Find the office hours of a professor.

                Arguments:
                    scenario (str): The emotion of interest.

                Returns:
                    str: The office hours of that professor.
                """
        responses = {
        'roommate': "I see. Have you talked with Resed abot what we can do?",
        'homesick': "Herrick is a great resource.",
        'lost': "duck.",
        'academic': "Professors are a great resource if you feel the academics are too challenging.",
        'hard': "College can be hard. ",
        'alone': "Try joining some clubs to meet new people.",
        }
        return responses[scenario]


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
        if 'help' in tags:
            for emotion in self.EMOTIONS:
                if emotion in tags:
                    self.emotion = emotion
                    return self.go_to_state('specific_emotion')
            return self.go_to_state('unknown_emotion')
        else:
            return self.finish('confused')

    # "specific_emotion" state functions

    def on_enter_specific_emotion(self):
        """Send a message when entering the "specific_emotion" state."""
        response = [
            f"{self.get_emotion(self.emotion)}"
        ]
        return response

    def respond_from_specific_emotion(self, message, tags):
        """Decide what state to go to from the "specific_emotion" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.scenario = None
        for scenario in self.SCENARIOS:
            if scenario in tags:
                self.scenario = scenario
                return self.go_to_state('specific_scenario')
            else:
                return self.go_to_state('unknown_scenario')

    def on_enter_unknown_scenario(self):
        return "It seems like this feeling is not cause by a specific scenario. Lets try to see if there are any underlying beliefs that make you feel this way. What negative core beliefs make you feel this way"
    def respond_from_unknown_scenario(self, message, tags):
        for cb in self.CORE_BELIEFS:
            if cb in tags:
                self.cb = cb
                return self.go_to_state('specific_cb')
        return self.go_to_state('unknown_cb')


    def on_enter_unknown_emotion(self):
        """Send a message when entering the "unknown_emotion" state."""
        return "I am not sure if I understand. Try to think of specific emotions that you are feeling. \nHave you recently, or are you currently, struggling with any of the following emotions?\n" \
               "anxiety \n" \
               "isolation \n" \
               "worthlessness \n" \
               "worry \n" \
               "unpreparedness \n" \
               "lost \n" \
               "depressed \n"

    def respond_from_unknown_emotion(self, message, tags):
        """Decide what state to go to from the "unknown_emotion" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        self.emotion = None
        for emotion in self.EMOTIONS:
            if emotion in tags:
                self.emotion = emotion
                return self.go_to_state('specific_emotion')
        return self.go_to_state('unknown_emotion')

    # "specific_scenario" state functions

    def on_enter_specific_scenario(self):
        """Send a message when entering the "specific_scenario" state."""
        response = '\n'.join([
            f"{self.get_scenario(self.scenario)}."
            "Ok. It is good to understand a specific time that you felt this way."
            'Lets dive into what makes you feel this way. '
            'What core beliefs are instilled in these times in your life?'
            # f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            # 'Do you know where their office is?',
        ])
        return response

    def respond_from_specific_scenario(self, message, tags):
        """ If there is a specific scenario, """
        for cb in self.CORE_BELIEFS:
            if cb in tags:
                self.cb = cb
                return self.go_to_state('specific_cb')
        return self.go_to_state('unknown_cb')


    def on_enter_specific_cd(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        response = '\n'.join([
            f"{self.get_cd(self.cd)}."
            "\n Das a cognitive distortion"
        ])
        return response

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
    def on_enter_unknown_cd(self):
        """Send a message when entering the "unknown_emotion" state."""
        return "... elaborate so that we can pinpoint a cognitive distortion"

    def respond_from_unknown_cd(self, message, tags):
        """Decide what state to go to from the "unknown_emotion" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        self.cd = None
        for cd in self.EMOTIONS:
            if cd in tags:
                self.emotion = cd
                return self.go_to_state('specific_cd')
        return self.go_to_state('unknown_cd')


    def on_enter_specific_cb(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "Feeling like you are", self.cb, "seems like a negative core belief. Lets challenge that. Think of a time when you felt the opposite of this negative feeling..."
        ])
    def respond_from_specific_cb(self, message, tags):
        self.go_to_state('unknown_cb')

    def on_enter_challenge_emotion(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "Think of a time of where you felt the opposite. You felt loved, confident, and you felt others saw you in this light. Describe any time where you felt smart, capable and loved. ",
            "Or describe a time where you felt loved and respected by others. Start with 'I am'.",
        ])

    def respond_from_challenge_emotion(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.
        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.
        Returns:
            str: The message to send to the user.
        """
        if "I am" in tags:
            return self.go_to_state('check_feeling')
        else:
            return self.finish('breathing')


    def on_enter_unknown_cb(self):
        """Send a message when entering the "" staunknown_cbte."""
        return "I am not sure if I understand. Core beliefs are what we believe about ourselves that influence how we interpret our experiences. \n" \
               "If our core beliefs are negative, they will negatively impact how we see others, the world, ourselves, and our future. \n" \
               "Here are some common negative beliefs. If you suffer from any of these cognitive beliefs, please type it. \n" \
               "not enough \n not prepared \n undeserving \n unlovable \n abnormal \n failure "

    def respond_from_unknown_cb(self, message, tags):
        self.cb = None
        for cb in self.CORE_BELIEFS:
            if cb in tags:
                self.cb = cb
                return self.go_to_state('specific_cb')
        return self.go_to_state('unknown_cb')


    # "finish" functions


    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm just a simple bot that can't understand much. Maybe try rephrasing so I can better understand."


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
    CBTBot().chat()
