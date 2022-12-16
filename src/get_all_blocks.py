import os
def getAllBlocks():
    return [name[:-3] for name in os.listdir('src//converters') if name[-3:] == '.py']