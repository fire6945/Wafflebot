import json

class Values:
    """
    This class handles bot/server information and setting, getting and deleting them
    Works with config.json
    """

    with open('config.json', 'r') as f:
        data = json.loads(f.read())

    @classmethod
    def save(cls):
        with open('config.json', 'w') as f:
            f.write(cls.data)

    # The four following methods deal with getting, setting and deleting badwords
    @classmethod
    def get_badwords(cls):
        return cls.data["badwords"]

    @classmethod
    def set_badword(cls, prev, new):
        try: cls.data[cls.data["badwords"].index(prev)] = new
        except: return False

    @classmethod
    def delete_badword(cls, word):
        try: del cls.data["badwords"][cls.data["badwords"].index(word)]
        except: return False

    @classmethod
    def delete_all_badwords(cls):
        try: cls.data["badwords"] = {}; cls.save()
        except: return False

    # The five following methods deal with getting, setting and deleting channel ids
    @classmethod
    def get_channels(cls):
        try: return cls.data["channels"]
        except: return False

    @classmethod
    def get_channel(cls, channel):
        try: return cls.data["channels"][channel]
        except: return False

    @classmethod
    def set_channel(cls, prev, new):
        try: cls.data["channels"][prev] = new
        except: return False

    @classmethod
    def delete_channel(cls, prev, new):
        try: del cls.data["channels"][prev]
        except: return False

    @classmethod
    def delete_all_channels(cls):
        try: cls.data["channels"] = {}; cls.save()
        except: return False
