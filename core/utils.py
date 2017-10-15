import os
import uuid


def image_save_path(instance, filename):
    if instance.id:
        type_str = str(instance.__class__)
        type_str = type_str[(type_str.find("'") + 1):type_str.rfind("'")].split('.')[-1]
        save_path = "user/%i/%s/%i/%s" % (instance.author.id,
                                          type_str,
                                          instance.id,
                                          filename)
    else:
        save_path = "user/%i/temp/%s" % (instance.author.id,
                                         str(uuid.uuid4()) + os.path.splitext(filename)[1])
    return save_path


def post_title_image_save_path(instance, filename):
    return image_save_path(instance, 'title_image' + os.path.splitext(filename)[1])


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
