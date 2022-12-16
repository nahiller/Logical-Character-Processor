import importlib
from letter_blocker_processor import *

def get_converters(block_names):
    return [eval("importlib.import_module('src.converters.%s').%s" % (block, block)) if block != 'letter_block_converter' else letter_blocker_processor(block) for block in block_names]