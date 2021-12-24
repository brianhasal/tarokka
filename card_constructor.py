import random

class Card:
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description
        self.str_value = self.name[:self.name.find(" ")]
        self.suit = self.name[self.name.rfind(" ") + 1:]



    def __repr__(self):
        return self.name


    def description_add(self, content):
        if len(self.description) > 0:
            self.description += " " + content
        else:
            self.description += content





class Low_Card(Card):
    def __init__(self, name, description = "", namealt = ""):
        super().__init__(name, description = "")
        self.namealt = namealt

    def __repr__(self):
        return self.name







class High_Card(Card):
    def __init__(self, name, description = ""):
        super().__init__(name, description = "")
        self.edesca = ""
        self.edescb = ""
        self.location = ""

    def __repr__(self):
        return self.name




