import importlib

def letter_blocker_processor(block):
    return eval("importlib.import_module('src.converters.%s').%s" % (block, block))(input('Enter letter you want to block\n'))