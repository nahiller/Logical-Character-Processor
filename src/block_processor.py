from functools import reduce

def blockProcessor(text, *blocks):
    return reduce(lambda result, block: block(result), blocks, text)