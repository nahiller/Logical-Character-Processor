#!/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'src')))

sys.path.append(os.path.dirname(__file__)) 

@task
def setup():
    sh('python -m pip install -U coverage')
    sh('python -m pip install -U pytest')
    sh('python -m pip install -U radon==4.3.2')  
    pass


@task
def test():
    sh('python -m coverage run --source src --omit src/letter_blocker_processor.py -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')
    pass


@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
    for pycfile in glob.glob("radon.report"): os.remove(pycfile)    
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass
    pass

@task
def radon():
    sh('radon cc src -a -nb')
    sh('radon cc src -a -nb > radon.report')
    if os.stat("radon.report").st_size != 0:
        raise Exception('radon found complex code')

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
    pass


@task
def run():
    from src import get_all_blocks, block_processor, get_converters
    import importlib
    
    option = input('Would you like to use a file to create your block:\nyes\nno\n')

    if option == 'yes':
        filename = input('Enter your filename. The file must be in the current working directory\n')
        file = open(filename, 'r')
        chosen_block_names = file.read().split()
    else:
        blockNames = get_all_blocks.getAllBlocks()

        print("Type the numbers - separated by commas - of the blocks you want to use\nList of blocks:")

        count = 1
        for block in blockNames:
            print(count, block)
            count += 1
    
        chosen_block_names = [blockNames[num - 1] for num in [int(index) for index in input().split(' ')]]

    text = input('Please enter a sample text\n')

    converters = get_converters.get_converters(chosen_block_names)

    print('Processed block:\n', block_processor.blockProcessor(text, *converters), sep='')