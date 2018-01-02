# -*- coding: utf-8 -*-
# Created by Andrei Kisel
import os
import re

# Task 1

def search_file():
    '''This function searches for files on disk D'''
    path_files = []
    for d, dirs, files in os.walk('D:\\'):
        for f in files:
            path = os.path.join(d, f)
            path_files.append(path)
    return path_files

# think about displaying the Russian ways


for res_path_file in search_file():
    print(res_path_file)


# Task 2

def censor(forbidden, substitution):   # decorator_maker_with_arguments
    '''The super sensor via regular'''
    def my_decorator(func):
        def wrapped():
            return re.sub(r'|'.join(forbidden), substitution, func())
        return wrapped
    return my_decorator


@censor(forbidden=("ipsum", "quis"), substitution="[CENSORED]")
def text_producer():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum."""


print(text_producer())


# Task 2.1  Write a decorator using a cycle

def censor(forbidden, substitution):   # decorator_maker_with_arguments
    '''The super sensor via cycle'''
    def my_decorator(func):
        def wrapped():
            for line in func():
                return line.replace(forbidden, substitution)
        return wrapped
    return my_decorator


@censor(forbidden=("ipsum", "quis"), substitution="[CENSORED]")
def text_producer():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum."""