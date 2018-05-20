#!/usr/bin/python3

import time
pilihan_menu = ['kabuli', 'bakso', 'gado-gado', 'rujak','soto','tahu campur']
print list(enumerate(pilihan_menu))
time.sleep(2)
for index, item in enumerate(pilihan_menu, start = 1):
    print index, item
time.sleep(2)
for index, item in enumerate(pilihan_menu, 1):
    print index, item
time.sleep(2)
for index, item in enumerate(pilihan_menu):
    print index + 1, item

