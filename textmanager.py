import pickle

class TextManager:
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(TextManager, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.filename = "data.pk1"

    def loadFromFile(self):
        pk_file = open(self.filename, 'rb')
        data = pickle.load(pk_file)
        pk_file.close()
        return data

    def writeToFile(self, data):
        output = open(self.filename, 'wb')
        pickle.dump(data, output)
        output.close()
        
