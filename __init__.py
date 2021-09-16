from mycroft import MycroftSkill, intent_file_handler


class WookieAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.wookie.intent')
    def handle_assistant_wookie(self, message):
        self.speak_dialog('assistant.wookie')


def create_skill():
    return WookieAssistant()

