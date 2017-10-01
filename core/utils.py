class Enum:
    '''
    Implements enum: contains choices with naming enumeration. Get element by id or vice versa
    '''

    choices = []
    map = {}

    def __init__(self):
        pass

    # def __init__(self, enum_names):
    #     if type(enum_names) != list:
    #         raise TypeError()
    #     else:
    #         self.choices = enum_names
    #         self.map = {self.choices[i]: i for i in range(len(self.choices))}

    def get_name(self, id):
        if id >= len(self.choices):
            raise IndexError
        else:
            return self.choices[id]

    def get_id(self, name):
        if len(self.map) < len(self.choices):
            self.map = {self.choices[i]: i for i in range(len(self.choices))}
        return self.map.get(name)
