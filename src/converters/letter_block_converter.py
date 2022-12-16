def letter_block_converter(letter):
    if len(letter) > 1:
        raise Exception('must be a single letter')
    return lambda text: text.replace(letter, '')