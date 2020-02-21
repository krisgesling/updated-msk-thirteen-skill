from mycroft import MycroftSkill, intent_file_handler


class UpdatedMskThirteen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('thirteen.msk.updated.intent')
    def handle_thirteen_msk_updated(self, message):
        self.speak_dialog('thirteen.msk.updated')


def create_skill():
    return UpdatedMskThirteen()

