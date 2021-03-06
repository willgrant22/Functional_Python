#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================
import os

nl = '\n'
cr = '\r'
lbox = '='
uscore = '.'
space = ' '
title = "Terminal dimentions"
actionrows = "Number of rows:"
actioncols = "Number of columns:"

cols, rows = os.get_terminal_size()
x = round(cols/3)
y = cols % 3

span = (cols - (x + len(title)))
print(cols,span, x, y)
box = (lbox)
dims = (
	f"{nl}{space * (x + (y*y)) }{(lbox * (len(title)))}"
	f"{nl}{space * (x + (y*y)) }{title}"
	f"{nl}{space * (x + (y*y)) }{(lbox * (len(title)))}{nl}"
	f"{nl}{space * (round(x / len(actioncols)+2))}{actioncols}{uscore * ( (x) + round((cols-x-12) - len(actioncols)))}{cols}{nl}"
	f"{nl}{space * (round((x / len(actioncols)+2)))}{actionrows}{uscore * ( (x) + round((cols-x-12) - len(actionrows)))}{rows}"
	)

print(dims)
with open('terminal_size.txt', 'w') as file:
	data = dims
	file.write(data)

# Slopy way to do it
'''
rows, columns = os.popen('stty size', 'r').read().split()
print(columns, rows)
'''