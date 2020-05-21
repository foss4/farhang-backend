class Dictionary:

    def __init__(self, name=None, dic_id=None):
        self.id = dic_id
        self.name = name


class Word:
    def __init__(self, name=None, meaning=None, dictionary=None):
        self.name = name
        self.meaning = meaning
        self.dictionary = dictionary
