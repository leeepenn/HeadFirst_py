# encoding utf-8
import os
from nester import *
man = []
ohter = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                ohter.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('this file is missing !')
try:
    with open('man_data.txt', 'w') as man_file:
        print_lol(man, fn=man_file)
    with open('other_data.txt', 'w') as other_file:
        print_lol(ohter, fn=other_file)
except IOError as err:
    print('file error: ' + str(err))
